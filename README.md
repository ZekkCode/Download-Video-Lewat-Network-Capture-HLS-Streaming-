# 📥 Cara Download Video Streaming dari Situs Tanpa Tombol Download (HLS Network Capture)

Situs streaming film (misal: bioskop online, layanan streaming gratis, dll) sering tidak menyediakan akses langsung untuk mengunduh video. Namun, banyak dari mereka menggunakan metode **HLS (HTTP Live Streaming)** yang memecah video menjadi segmen-segmen kecil (`.ts`). Dengan sedikit trik menggunakan Developer Tools di browser, kamu bisa menemukan URL video dan mendownloadnya!

---

## 🚦 Langkah Umum

1. 🔎 **Temukan URL playlist `.m3u8`** melalui Network tab di browser.
2. 💾 **Download video** menggunakan `yt-dlp` atau script Python sederhana.

---

## 🕵️‍♂️ Cara Menemukan URL `.m3u8` di Situs Streaming

> **Tips:**  
> Cocok untuk situs web yang tidak menyediakan tombol download, misal: bioskopkeren, nontonxxi, LK21, dll.

1. **Buka halaman video** yang ingin kamu download.
2. Tekan `F12` untuk membuka **Developer Tools**.
3. Masuk ke tab **Network**.
4. Filter ke `Media` atau ketik `.m3u8` di kolom filter.
5. **Refresh** halaman jika perlu.
6. Cari file dengan ekstensi `.m3u8` di daftar request.
7. Klik kanan pada URL tersebut dan pilih **Copy link address**.

> 💡 **Catatan:**  
> Jika tidak muncul file `.m3u8`, play dulu videonya beberapa detik lalu cek ulang di Network tab.

---

## ⚡ Download Video dengan [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)

1. Install yt-dlp & ffmpeg:
   - **Windows**: Download yt-dlp.exe, install [ffmpeg](https://ffmpeg.org/download.html)
   - **Linux/macOS**: `pip install -U yt-dlp` dan install ffmpeg via package manager

2. Jalankan perintah:
   ```bash
   yt-dlp "URL_m3u8_yang_kamu_dapat"
   ```

---

## 🐍 Alternatif: Download dengan Script Python

Jalankan script di bawah ini untuk mendownload video dari file `.m3u8` menggunakan ffmpeg (pastikan ffmpeg sudah terpasang):

```python
import sys
import subprocess

def download_hls(url, output="output.mp4"):
    command = [
        "ffmpeg",
        "-i", url,
        "-c", "copy",
        "-bsf:a", "aac_adtstoasc",
        output
    ]
    print(f"Downloading video dari: {url}")
    subprocess.run(command)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_download.py <URL_m3u8>")
        sys.exit(1)
    download_hls(sys.argv[1])
```

> **Jalankan di terminal:**
> ```bash
> python script_download.py "URL_m3u8"
> ```

---

## 📋 Tips & Catatan

- **Legalitas:**  
  Gunakan hanya untuk konsumsi pribadi dan video yang memang Anda punya hak aksesnya. Jangan reupload atau distribusi ulang tanpa izin.
- **DRM:**  
  Jika video menggunakan DRM (Digital Rights Management), metode ini tidak akan berhasil.
- **Subtitle:**  
  Untuk subtitle, biasanya ada file `.vtt` atau `.srt` di Network tab, bisa juga didownload.

---

## 🔗 Referensi & Tools

- [yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg.org](https://ffmpeg.org/)
- [HLS Streaming (Wikipedia)](https://en.wikipedia.org/wiki/HTTP_Live_Streaming)

---

> 🎬 Selamat mencoba! Jika repo ini bermanfaat, silakan ⭐ (star) ya.
>
> &copy; 2025 ZekkCode
