import os


def clean_temp_files():

    # ask user for folder path
    folder_path = input("Enter folder to clean: ")

# validate folder exists
    if not os.path.isdir(folder_path):
        print(f" Error: folder '{folder_path}' does not exist")
        return

        deleted_count = 0

# open log file for writing
        with open("deleted_files.log", "a") as log_file:

            # loop through all the files in the folder
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)

# check if its a file with .tmp or .log extension
                if os.path.isfile(file_path) and (filename.endswith('.tmp') or filename.endswith('.log')):

                    try:

                        # delete the file
                        os.remove(file_path)

# log the deletion
                        log_file.write(f" Deleted: {filename}\n")
                        print(f" Deleted: {filename}")
                        deleted_count += 1

                    except Exception as e:

                        log_file.write(
                            f" Failed to Delete {filename}: {str(e)}\n")
                        print(f" failed to delete {filename}:{str(e)}")

# print summary
                        print(
                            f" Cleanup complete. {deleted_count} files deleted.")


if __name__ == "__main__":
    clean_temp_files()
