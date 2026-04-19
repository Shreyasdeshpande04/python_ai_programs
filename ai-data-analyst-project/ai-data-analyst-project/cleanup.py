import os
import shutil
import pathlib

def deep_clean():
    # 1. Get the path where this script is located
    root_dir = pathlib.Path(__file__).parent.resolve()
    print(f"🧹 Starting Deep Clean in: {root_dir}")

    # 2. Folders to empty (Delete the files inside them)
    folders_to_empty = [
        'uploads', 
        'exports/charts', 
        'exports/reports', 
        'exports'
    ]

    # 3. Process of deleting files
    for folder_name in folders_to_empty:
        folder_path = os.path.join(root_dir, folder_name)
        if os.path.exists(folder_path):
            files_deleted = 0
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)
                try:
                    if os.path.isfile(item_path):
                        os.unlink(item_path)
                        files_deleted += 1
                    elif os.path.isdir(item_path) and item != "__init__.py":
                        shutil.rmtree(item_path)
                        files_deleted += 1
                except Exception as e:
                    print(f"Could not delete {item}: {e}")
            print(f"✅ Cleared {folder_name} ({files_deleted} items removed)")

    # 4. Remove all __pycache__ folders (The binary files you saw)
    pycache_count = 0
    for p in root_dir.rglob('__pycache__'):
        try:
            shutil.rmtree(p)
            pycache_count += 1
        except Exception:
            pass
    print(f"✅ Removed {pycache_count} __pycache__ folders")

    print("\n✨ PROJECT IS NOW CLEAN! Ready for a new demo.")

if __name__ == "__main__":
    deep_clean()