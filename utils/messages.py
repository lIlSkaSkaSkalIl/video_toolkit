# messages.py

def tampilkan_ringkasan_metadata(duration: float, size_mb: float, bitrate_kbps: float):
    print(f"🕒 Durasi     : {duration:.2f} detik")
    print(f"💾 Ukuran     : {size_mb:.2f} MB")
    print(f"📶 Bitrate    : {bitrate_kbps:.0f} kbps")
