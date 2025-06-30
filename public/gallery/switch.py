import os
import sys

def switch_filenames(file1, file2):
    # Get absolute paths
    dir_path = os.path.dirname(os.path.abspath(__file__))
    path1 = os.path.join(dir_path, file1)
    path2 = os.path.join(dir_path, file2)

    # Check if both files exist
    if not os.path.exists(path1) or not os.path.exists(path2):
        print("❌ One or both files do not exist.")
        return

    # Create a temporary name to avoid collision
    temp_name = "__temp_swap_file__"

    temp_path = os.path.join(dir_path, temp_name)
    os.rename(path1, temp_path)
    os.rename(path2, path1)
    os.rename(temp_path, path2)

    print(f"✅ Switched '{file1}' and '{file2}' successfully!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python switch.py file1 file2")
    else:
        switch_filenames(sys.argv[1], sys.argv[2])
