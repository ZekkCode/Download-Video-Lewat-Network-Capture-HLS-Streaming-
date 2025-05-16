# 💡 Panduan Download Video HLS dengan `yt-dlp`

Ingin mendownload video HLS (.m3u8) dari website streaming? Ikuti langkah mudah berikut!

---

## 1. 📥 Download & Install `yt-dlp`

- **Windows:**  
  [Download yt-dlp.exe](https://github.com/yt-dlp/yt-dlp/releases)
- **Linux/macOS:**  
  Install via pip:
  ```bash
  pip install -U yt-dlp
  ```

---

## 2. 🔗 Temukan URL `.m3u8`

Cari URL playlist `.m3u8` dari Network tab di browser.  
Lihat panduan lengkap di [README.md](./README.md).

---

## 3. 🚀 Download Video

Jalankan perintah berikut di terminal/command prompt:

```bash
yt-dlp "URL_m3u8_yang_kamu_dapat"
```

---

## 4. 🎬 Hasil Download

- Video akan otomatis didownload dan digabungkan menjadi file `.mp4`
- File akan berada di folder tempat kamu menjalankan perintah

---

## ⚠️ Catatan Penting

- Pastikan `ffmpeg` sudah ter-install di sistemmu  
  (yt-dlp membutuhkan ffmpeg untuk menggabungkan segmen)
- Untuk opsi lanjutan, cek dokumentasi: [yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp)

---

> 🔒 **Legalitas:**  
> Gunakan hanya untuk video yang kamu punya hak aksesnya.
