import os
import shutil

DOWNLOADS_PATH = os.path.expanduser("~/Downloads")

EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".m4a"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Executables": [".exe", ".msi", ".apk"],
    "Unity": [".unitypackage"],
    "Scripts/c#": [".cs"],
}

def sort_downloads():
    for filename in os.listdir(DOWNLOADS_PATH):
        file_path = os.path.join(DOWNLOADS_PATH, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            for folder, exts in EXTENSIONS.items():
                if ext in exts:
                    target_folder = os.path.join(DOWNLOADS_PATH, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f"Перемещено: {filename} → {folder}")
                    break

if __name__ == "__main__":
    sort_downloads()
