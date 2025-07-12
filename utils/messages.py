# messages.py

def show_metadata_summary(duration: float, size_mb: float, bitrate_kbps: float):
    print(f"🕒 Duration : {duration:.2f} seconds")
    print(f"💾 Size     : {size_mb:.2f} MB")
    print(f"📶 Bitrate  : {bitrate_kbps:.0f} kbps")


def show_split_duration_summary(video_size_mb: float, target_mb: float, telegram_mode: bool):
    print("\n📝 Summary:")
    print(f"  - Video Size      : {video_size_mb:.2f} MB")
    print(f"  - Target per Part : {target_mb:.2f} MB")
    print(f"  - Telegram Mode   : {'Yes' if telegram_mode else 'No'}")


def print_part_duration_report(part_durations: list[str], total_duration: str, original_duration: str, difference: str):
    print("\n📊 Duration per Part:")
    for i, dur in enumerate(part_durations, 1):
        print(f"  • Part {i:03}: {dur}")

    print(f"\n🧮 Total Part Duration : {total_duration}")
    print(f"🎞️ Original Video      : {original_duration}")
    print(f"✅ Difference          : {difference}")
