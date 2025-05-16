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