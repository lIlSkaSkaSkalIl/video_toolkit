# messages.py

def tampilkan_ringkasan_metadata(duration: float, size_mb: float, bitrate_kbps: float):
    print(f"🕒 Durasi     : {duration:.2f} detik")
    print(f"💾 Ukuran     : {size_mb:.2f} MB")
    print(f"📶 Bitrate    : {bitrate_kbps:.0f} kbps")

def tampilkan_ringkasan_durasi_split(video_size_mb: float, target_mb: float, telegram_mode: bool):
    print("\n📝 Ringkasan:")
    print(f"  - Ukuran video   : {video_size_mb:.2f} MB")
    print(f"  - Target per part: {target_mb:.2f} MB")
    print(f"  - Mode Telegram  : {'Ya' if telegram_mode else 'Tidak'}")
