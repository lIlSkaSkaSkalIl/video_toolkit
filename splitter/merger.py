# merger.py

import os
import subprocess

def get_file_size(path):
    return os.path.getsize(path) / (1024 * 1024)

def group_chunks_by_size(chunks, target_mb):
    groups = []
    current_group = []
    current_size = 0

    for chunk in chunks:
        size = get_file_size(chunk)
        if current_size + size > target_mb and current_group:
            groups.append(current_group)
            current_group = []
            current_size = 0
        current_group.append(chunk)
        current_size += size

    if current_group:
        groups.append(current_group)

    return groups

def merge_chunks(chunk_paths, output_path, temp_dir="/content/temp_chunks"):
    list_path = os.path.join(temp_dir, "merge_list.txt")
    with open(list_path, "w") as f:
        for chunk in chunk_paths:
            f.write(f"file '{chunk}'\n")
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", list_path, "-c", "copy", output_path
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
