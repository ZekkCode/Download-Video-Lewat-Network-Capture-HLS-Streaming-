# 📥 Cara Download Video Lewat Network Capture (HLS Streaming)

Streaming video di website seperti `spicevids.com` biasanya menggunakan metode **HLS (HTTP Live Streaming)** yang memecah video menjadi segmen-segmen kecil (`.ts`). Untuk mendownload video tersebut, kita perlu:

1. 🔎 **Menemukan URL playlist `.m3u8`** dari tab Network di browser Developer Tools.
2. 💾 **Menggunakan tool seperti `yt-dlp` atau script Python** untuk mendownload semua segmen dan menggabungkannya.

---

## 🚩 Cara menemukan URL `.m3u8`

> **Langkah-langkah:**
>
> 1. Buka halaman video di browser.
> 2. Tekan `F12` untuk membuka Developer Tools, lalu pergi ke tab **Network**.
> 3. Filter ke `Media` atau `XHR`.
> 4. Refresh/Reload halaman.
> 5. Cari file dengan ekstensi `.m3u8`.
> 6. Klik kanan dan **Copy URL** file tersebut.

---

## ⚡ Download dengan `yt-dlp`

Cukup jalankan perintah berikut di terminal:

```bash
yt-dlp "URL_m3u8_yang_kamu_dapat"
```
- Pastikan sudah install `yt-dlp` dan `ffmpeg` di sistemmu.

---

## 🐍 Alternatif: Download dengan Python

Jalankan script `script_download.py` dengan argumen URL `.m3u8`:

```bash
python script_download.py "URL_m3u8"
```

---

### 📝 Contoh script_download.py (otomatis pakai `ffmpeg`):

```python
import sys
import subprocess

def download_hls(url, output="output.mp4"):
    # Perintah ffmpeg untuk download dan gabung HLS
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

---

## 📤 Cara upload ke GitHub

1. Buat repo baru di GitHub, misal: `cara-download-video-lewat-network`
2. Upload file berikut:
    - `README.md`
    - `script_download.py`
    - `panduan_pakai_yt-dlp.txt`
3. Commit dan push ke repo.

---

**Referensi & Tools:**
- [yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg.org](https://ffmpeg.org/)
- [HLS Streaming (Wikipedia)](https://en.wikipedia.org/wiki/HTTP_Live_Streaming)

---

> 🎉 Selamat mencoba! Jika bermanfaat, silakan ⭐ repo ini.
