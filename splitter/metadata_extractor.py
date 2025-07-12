# metadata_extractor.py

import subprocess
import json

def extract_metadata(video_path: str) -> dict:
    result = subprocess.run([
        "ffprobe", "-v", "error", "-print_format", "json",
        "-show_format", "-show_streams", video_path
    ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return json.loads(result.stdout)

def save_metadata(metadata: dict, output_path: str):
    with open(output_path, "w") as f:
        json.dump(metadata, f, indent=2)

def summarize_metadata(metadata: dict):
    duration = float(metadata["format"]["duration"])
    size_mb = float(metadata["format"]["size"]) / (1024 * 1024)
    bitrate_kbps = float(metadata["format"]["bit_rate"]) / 1000
    return duration, size_mb, bitrate_kbps
