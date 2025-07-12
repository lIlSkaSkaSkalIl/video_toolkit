# 🎞️ Video Toolkit

Video Toolkit adalah kumpulan alat bantu modular berbasis Python + FFmpeg untuk memproses video di Google Colab secara efisien dan praktis. Cocok untuk membagi video ke beberapa part, memeriksa metadata, serta menyesuaikan ukuran file agar cocok diunggah ke platform seperti Telegram.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lIlSkaSkaSkalIl/video_toolkit/blob/main/video_splitter_colab.ipynb)

---

## 🚀 Fitur Utama

- ✅ **Ambil metadata video** (durasi, ukuran, bitrate)  
- ✂️ **Split video berdasarkan durasi** otomatis sesuai target ukuran  
- 📦 **Gabungkan chunk menjadi part** siap upload  
- 📊 **Laporan durasi per part & selisih total**  
- 📁 Struktur direktori otomatis: semua file tersimpan rapi dalam `media_toolkit/`

---

## 🛠️ Cara Penggunaan (di Google Colab)

1. **Buka Notebook Colab**  
   Klik tombol **"Open in Colab"** di atas atau akses langsung:
   ```
   https://colab.research.google.com/github/lIlSkaSkaSkalIl/video_toolkit/blob/main/video_splitter_colab.ipynb
   ```

2. **Clone Repositori**  
   Jalankan cell pertama untuk mengkloning repo dan menyiapkan folder:
   ```
   /content/media_toolkit/
       ├── input/
       ├── temp_chunks/
       ├── output_parts/
       └── metadata/
   ```

3. **Masukkan File Video**  
   Upload dari Google Drive, lalu jalankan cell "📂 Ambil Video".

4. **Ambil Metadata**  
   Jalankan cell "📋 Ambil Metadata" untuk melihat durasi, ukuran, dan bitrate.

5. **Hitung Durasi Maksimum per Part**  
   Masukkan batas ukuran (GB), aktifkan "mode Telegram" jika perlu.

6. **Split & Merge**  
   Jalankan satu cell gabungan untuk memotong video menjadi chunk, lalu menggabungkannya kembali menjadi part berdasarkan target ukuran.

7. **Ringkasan Durasi**  
   Tampilkan total durasi part vs durasi asli, termasuk selisihnya.

---

## 📁 Struktur Proyek

```
video_toolkit/
├── splitter/
│   ├── metadata_extractor.py
│   ├── video_splitter.py
│   └── merger.py
├── utils/
│   ├── helpers.py
│   ├── messages.py
│   └── ...
```

---

## 💡 Teknologi yang Digunakan

- Python 3.10+
- FFmpeg
- tqdm
- Google Colab

---

## 🔍 Contoh Output Ringkasan
```
📊 Duration per Part:
  • Part 001: 20m 15s
  • Part 002: 20m 12s
  • Part 003: 10m 05s

🧮 Total Part Duration : 50m 32s
🎞️ Original Video      : 50m 30s
✅ Difference          : 2s
```

---

## 🧑‍💻 Kontribusi

Sangat terbuka untuk kontribusi!  
Silakan fork repo, buat branch baru, dan kirimkan pull request.  
Atau ajukan fitur baru via [issue](https://github.com/lIlSkaSkaSkalIl/video_toolkit/issues).

---

## 📄 Lisensi

Proyek ini menggunakan lisensi MIT.
