import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import cv2
import numpy as np
import joblib

class BoikotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Deteksi Produk Boikot")
        self.root.geometry("700x600")
        self.root.configure(bg="#f0f4f7")

        self.cap = None
        self.frame = None

        # Load model machine learning
        try:
            self.model = joblib.load("model_boikot.pkl")
            print("[INFO] Model berhasil dimuat.")
        except Exception as e:
            print(f"[ERROR] Gagal memuat model: {e}")
            self.model = None

        # Judul aplikasi
        self.title = Label(root, text="Aplikasi Deteksi Produk Boikot", font=("Helvetica", 18, "bold"),
                           bg="#f0f4f7", fg="#333")
        self.title.pack(pady=20)

        # Preview kamera
        self.video_label = Label(root, bg="#ccc", width=500, height=350)
        self.video_label.pack()

        # Tombol buka kamera
        self.btn_open_camera = Button(root, text="Buka Kamera", command=self.open_camera,
                                      font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.btn_open_camera.pack(pady=10)

        # Tombol analisis
        self.btn_scan = Button(root, text="Analisis Produk", command=self.analyze_product,
                               font=("Helvetica", 12), bg="#2196F3", fg="white")
        self.btn_scan.pack(pady=10)

        # Label hasil
        self.result_label = Label(root, text="", font=("Helvetica", 16, "bold"), bg="#f0f4f7")
        self.result_label.pack(pady=20)

    def open_camera(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("[ERROR] Kamera tidak tersedia")
            self.result_label.config(text="Kamera tidak tersedia", fg="red")
        else:
            self.update_frame()

    def update_frame(self):
        if self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                self.frame = frame
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(cv2image)
                imgtk = ImageTk.PhotoImage(image=img)
                self.video_label.imgtk = imgtk
                self.video_label.configure(image=imgtk)
        self.root.after(10, self.update_frame)

    def analyze_product(self):
        if self.frame is not None and self.model is not None:
            try:
                # Ubah ukuran sesuai model
                img = cv2.resize(self.frame, (64, 64))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img = img / 255.0  # Normalisasi
                img = img.flatten().reshape(1, -1)  # Untuk model scikit-learn

                # Prediksi
                prediction = self.model.predict(img)[0]

                # Tampilkan hasil
                color = "red" if prediction.lower() == "boikot" else "green"
                self.result_label.config(text=f"Hasil: {prediction}", fg=color)

            except Exception as e:
                self.result_label.config(text=f"Error saat prediksi: {e}", fg="red")
        else:
            self.result_label.config(text="Kamera belum aktif atau model gagal dimuat", fg="orange")

    def on_close(self):
        if self.cap and self.cap.isOpened():
            self.cap.release()
        self.root.destroy()

# Jalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = BoikotApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
