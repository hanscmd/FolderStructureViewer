```markdown
# 📁 Folder Structure Viewer

Folder Structure Viewer is a Python script that displays the hierarchical structure of a given folder and optionally exports it to a `.txt` file.

> Currently a simple CLI tool, open for future enhancements.

## ✅ Features

- 📂 Visualizes folder and file hierarchy  
- 📝 Exports structure to a `.txt` file  
- 🚫 Handles permission and missing folder errors gracefully  

## 📦 Installation

Clone the repository and navigate to the project folder:

```bash
git clone https://github.com/hanscmd/FolderStructureViewer.git
cd FolderStructureViewer
```

No external dependencies required — uses Python's built-in libraries.

## 🛠️ Usage

Run the script using Python:

```bash
python Structure.py
```

Enter the full path to the folder when prompted:

```text
Enter the full path to the folder: C:\Users\Documents\MyFolder
```

You’ll see the folder structure printed in the terminal, like this:

```text
MyFolder/
├── Subfolder1/
│   └── file1.txt
├── Subfolder2/
│   └── file2.docx
└── file3.pdf
```

Then choose whether to export the structure to a `.txt` file.

## 🧪 Development

You can test the script by creating a sample folder with nested files and running:

```bash
python Structure.py
```

Feel free to fork the repo and contribute improvements!

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
```
