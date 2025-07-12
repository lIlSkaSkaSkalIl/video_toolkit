# video_splitter.py

import os
import math
import subprocess
from tqdm import tqdm

def split_video_by_duration(video_path, output_dir, base_filename, total_duration, chunk_duration):
    chunk_paths = []

    for i in tqdm(range(0, math.ceil(total_duration), chunk_duration), desc="🎞️ Splitting"):
        chunk_path = os.path.join(output_dir, f"{base_filename}_chunk_{i}.mp4")
        subprocess.run([
            "ffmpeg", "-y", "-i", video_path, "-ss", str(i),
            "-t", str(chunk_duration), "-c", "copy", chunk_path
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        chunk_paths.append(chunk_path)

    return chunk_paths
