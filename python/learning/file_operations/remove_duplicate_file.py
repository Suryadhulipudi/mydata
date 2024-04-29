import os
import subprocess

def delete_duplicate_files_in_dirs(path):
    unique_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if file not in unique_files:
                unique_files.append(file)
            else:
                os.remove(file_path)
    return unique_files

print(delete_duplicate_files_in_dirs('/tmp/exmaples'))



