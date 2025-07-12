# duration_calculator.py

def calculate_max_duration(metadata: dict, target_size_mb: float, telegram_mode=False):
    if telegram_mode and target_size_mb > 1900:
        target_size_mb = 1900

    video_size_mb = float(metadata["format"]["size"]) / (1024 * 1024)
    if video_size_mb <= target_size_mb:
        return float(metadata["format"]["duration"]), video_size_mb, target_size_mb, False
    else:
        bitrate_kbps = float(metadata["format"]["bit_rate"]) / 1000
        max_duration = (target_size_mb * 8 * 1024) / bitrate_kbps
        return max_duration, video_size_mb, target_size_mb, True
