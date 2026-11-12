import os
import shutil

def categorize_file(filename: str) -> str:
    extension = filename.split(".")[-1].lower()
    if extension in ("pdf", "doc", "docx", "txt"):
        return "Documents"
    elif extension in ("jpg", "jpeg", "png", "gif"):
        return "Images"
    elif extension in ("mp3", "wav"):
        return "Audio"
    else:
        return "Other"

def confirmation():
    answer = input("Move the given files? Type yes to confirm")
    return answer.strip().lower() == "yes"

def move_files(folder_path, filenames):
    if not confirmation():
        print("Ok. No files moved.")
        return
    for filename in filenames:
        category = categorize_file(filename)
        category_folder = os.path.join(folder_path, category)
        os.makedirs(category_folder, exist_ok=True)
        source = os.path.join(folder_path,filename)
        destination = os.path.join(category_folder, filename)

        if os.path.exists(destination):
            print("A file with that name already exists in:", destination)
            continue
        shutil.move(source, destination)
        print("Successfully moved", filename, "to", category)
def preview_files(filenames):
    counts = {}
    for filename in filenames:
        category = categorize_file(filename)
        print(filename,"-->", category)
        counts[category] = counts.get(category, 0) + 1
    print("\nSummary:")
    for category, count in counts.items():
        print(category, ":", count)

def preview_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("That folder does not currently exist:", folder_path)
        return
    filenames = []
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path):
            filenames.append(filename)
    if not filenames:
        print("No files to organize.")
        return
    preview_files(filenames)
    move_files(folder_path, filenames)
if __name__ == "__main__":
    folder_path = input("Enter a folder path(ex: practice_files): ").strip()
    preview_folder(folder_path)

