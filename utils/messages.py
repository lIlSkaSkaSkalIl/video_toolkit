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


def show_part_duration_summary(part_durations: list[float], original_duration: float):
    import math

    def format_duration(seconds: float) -> str:
        seconds = int(round(seconds))
        hours = seconds // 3600
        minutes = (seconds % 3600) % 60
        secs = seconds % 60

        parts = []
        if hours > 0:
            parts.append(f"{hours}h")
        if minutes > 0:
            parts.append(f"{minutes}m")
        if secs > 0 or not parts:
            parts.append(f"{secs}s")
        return " ".join(parts)

    total_duration = sum(part_durations)
    difference = math.ceil(abs(original_duration - total_duration))

    print("\n📊 Duration per Part:")
    for i, dur in enumerate(part_durations, 1):
        print(f"  • Part {i:03}: {format_duration(dur)}")

    print(f"\n🧮 Total Part Duration : {format_duration(total_duration)}")
    print(f"🎞️ Original Video      : {format_duration(original_duration)}")
    print(f"✅ Difference          : {format_duration(difference)}")
