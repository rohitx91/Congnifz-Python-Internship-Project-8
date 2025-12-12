# Level 3 - Task 3: Automation Script
# Author: Rohit Pandit
# Task: Automate File Organization Based on File Type

import os
import shutil

# Folder you want to organize
TARGET_FOLDER = "to_sort"

# File type mapping
FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
}

def create_folders():
    """Create category folders if not exist"""
    for folder in FILE_TYPES.keys():
        path = os.path.join(TARGET_FOLDER, folder)
        os.makedirs(path, exist_ok=True)

def organize_files():
    """Move files into category folders"""
    for file in os.listdir(TARGET_FOLDER):
        file_path = os.path.join(TARGET_FOLDER, file)

        if os.path.isdir(file_path):
            continue  # ignore folders

        _, ext = os.path.splitext(file)

        moved = False
        for category, extensions in FILE_TYPES.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(TARGET_FOLDER, category, file))
                print(f"Moved: {file} → {category}")
                moved = True
                break

        if not moved:
            print(f"Unknown type (skipped): {file}")

def main():
    if not os.path.exists(TARGET_FOLDER):
        print(f"❌ Folder '{TARGET_FOLDER}' not found. Create it and add files to organize.")
        return

    print("\n🚀 Starting Automation: File Organizer\n")
    create_folders()
    organize_files()
    print("\n✅ All files organized successfully!")

if __name__ == "__main__":
    main()
