# helpers.py

import math

def format_duration(seconds: float) -> str:
    seconds = int(round(seconds))
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    parts = []
    if hours > 0:
        parts.append(f"{hours}h")
    if minutes > 0:
        parts.append(f"{minutes}m")
    if secs > 0 or not parts:
        parts.append(f"{secs}s")
    return " ".join(parts)


def calculate_max_duration(metadata: dict, target_mb: float, telegram_mode: bool):
    size_mb = float(metadata["format"]["size"]) / (1024 * 1024)

    if telegram_mode and target_mb > 1900:
        target_mb = 1900

    if size_mb <= target_mb:
        return float(metadata["format"]["duration"]), size_mb, target_mb, False
    else:
        bitrate_kbps = float(metadata["format"]["bit_rate"]) / 1000
        max_duration_sec = (target_mb * 8 * 1024) / bitrate_kbps
        return max_duration_sec, size_mb, target_mb, True
