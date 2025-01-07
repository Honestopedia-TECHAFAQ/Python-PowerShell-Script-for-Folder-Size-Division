import os
import shutil
import math

def divide_folders_into_sets(source_dir, target_dir, set_size):
    if not os.path.exists(source_dir):
        raise ValueError(f"Source directory '{source_dir}' does not exist.")

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    all_folders = [f for f in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, f))]

    if not all_folders:
        raise ValueError(f"No folders found in the source directory '{source_dir}'.")

    total_folders = len(all_folders)
    num_sets = math.ceil(total_folders / set_size)

    for set_index in range(num_sets):
        set_start = set_index * set_size
        set_end = set_start + set_size
        set_folders = all_folders[set_start:set_end]

        set_dir = os.path.join(target_dir, f"Set_{set_index + 1}")
        os.makedirs(set_dir, exist_ok=True)

        for folder in set_folders:
            src_path = os.path.join(source_dir, folder)
            dst_path = os.path.join(set_dir, folder)

            shutil.copytree(src_path, dst_path)

    return {
        "total_folders": total_folders,
        "num_sets": num_sets,
        "folders_per_set": set_size
    }

def main():
    source_directory = "C:\\path\\to\\source\\directory"
    target_directory = "C:\\path\\to\\target\\directory"
    folders_per_set = 10

    try:
        result = divide_folders_into_sets(source_directory, target_directory, folders_per_set)
        print(f"Process completed successfully.")
        print(f"Total Folders: {result['total_folders']}")
        print(f"Number of Sets: {result['num_sets']}")
        print(f"Folders per Set: {result['folders_per_set']}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
