import os
import sys

def display_structure(folder, indent=0, structure=None):
    if structure is None:
        structure = []

    try:
        items = os.listdir(folder)
    except PermissionError:
        line = " " * indent + "[ACCESS DENIED]"
        print(line)
        structure.append(line)
        return structure
    except FileNotFoundError:
        line = " " * indent + "[FOLDER NOT FOUND]"
        print(line)
        structure.append(line)
        return structure

    for item in items:
        path = os.path.join(folder, item)
        if os.path.isdir(path):
            line = " " * indent + f"📁 {item}/"
            print(line)
            structure.append(line)
            display_structure(path, indent + 4, structure)
        else:
            line = " " * indent + f"📄 {item}"
            print(line)
            structure.append(line)

    return structure

def get_valid_path():
    while True:
        folder = input("Enter the full path to the folder: ")
        if os.path.isdir(folder):
            return folder
        else:
            print(f"\n[FOLDER NOT FOUND]: '{folder}'\nPlease try again.\n")

def ask_export():
    while True:
        choice = input("\nDo you want to export the structure to a TXT file? (yes/no): ").strip().lower()
        if choice in ["yes", "no"]:
            return choice
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def export_to_txt(structure, folder):
    folder_name = os.path.basename(os.path.normpath(folder))
    file_name = f"structure_{folder_name}.txt"
    script_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_path, file_name)

    try:
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(f'File structure for "{folder_name}" folder\n\n')
            f.write(f"{folder}\n\n")
            for line in structure:
                f.write(line + "\n")
        print(f"\n✅ Structure successfully exported to '{file_name}'")
        print(f"📂 File location: {full_path}")
    except Exception as e:
        print(f"\n❌ Error during export: {e}")

def main():
    folder = get_valid_path()
    print(f"\nFile structure for: {folder}\n")
    structure = display_structure(folder)

    choice = ask_export()
    if choice == "yes":
        export_to_txt(structure, folder)

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
