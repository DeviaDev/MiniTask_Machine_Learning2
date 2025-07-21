# 📵 Aplikasi Deteksi Boikot Real-Time

Aplikasi ini menggunakan kamera dan deep learning untuk mendeteksi apakah sebuah produk termasuk dalam daftar boikot hanya dengan mengarahkannya ke kamera. Cocok untuk meningkatkan kesadaran sosial dan edukasi konsumen berbasis teknologi.

[Notebook di Kaggle](https://www.kaggle.com/code/devianestnarendra/analisis-product-boikot)

## Fitur Utama

- Deteksi produk boikot secara real-time menggunakan kamera
- Transfer learning dengan MobileNetV2
- Visualisasi hasil pelatihan (akurasi dan loss)
- Dataset terbagi dua: `Boikot` dan `Non Boikot`
- Ringan dan bisa dijalankan tanpa GPU

## Teknologi yang Digunakan

- Python 3.x
- TensorFlow / Keras
- OpenCV (untuk future real-time use)
- Numpy, Pandas, Matplotlib

## Struktur Dataset

dataset/
├── Boikot/
│ ├── produk1.jpg
│ ├── produk2.jpg
│ └── ...
└── Non Boikot/
├── produk1.jpg
├── produk2.jpg
└── ...

## Arsitektur Model

Model berbasis MobileNetV2 dari ImageNet (pre-trained), lalu ditambahkan layer kustom untuk klasifikasi biner (`boikot` vs `non-boikot`).

## Cara Menjalankan

1. Clone repository atau buka via Kaggle
2. Pastikan struktur dataset sudah sesuai
3. Jalankan notebook `analisis-product-boikot.ipynb`
4. Lihat visualisasi akurasi dan hasil evaluasi model

## Contoh Output

- Akurasi pelatihan mencapai ~90%
- Akurasi validasi konsisten di ~85%
- Grafik training & validation loss
- Hasil prediksi terhadap contoh gambar

## Hasil & Evaluasi

- Model bekerja baik meskipun dataset kecil
- Potensi untuk dikembangkan lebih lanjut ke aplikasi mobile / embedded system
- Akurasi bisa meningkat dengan dataset yang lebih beragam dan banyak

## Catatan

- Dataset hanya 25 gambar per kelas → disarankan ekspansi untuk hasil lebih robust
- Saat ini hanya klasifikasi, belum bounding box (deteksi area objek)
- Real-time inference dengan kamera masih dalam pengembangan lanjutan

## Saran Pengembangan

- Implementasi model dengan YOLO untuk deteksi lebih presisi
- Tambahkan fitur "Lihat alasan boikot" dan "Rekomendasi alternatif"
- Integrasi dengan aplikasi Android (TensorFlow Lite)

## Referensi

- [Transfer Learning dengan MobileNetV2 – TensorFlow Docs](https://www.tensorflow.org/tutorials/images/transfer_learning)
- [Keras Applications – MobileNet](https://keras.io/api/applications/mobilenet/)

---
