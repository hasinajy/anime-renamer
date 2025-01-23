Here’s the updated **GitHub README** with an **alternative usage section** for the `.exe` file:

---

# Anime File Renamer

A Python script (and standalone `.exe`) to rename anime files with custom delimiters and advanced formatting. This tool is designed to clean up and organize anime filenames by adding season numbers, episode numbers, and removing unwanted tags like `(Dub)` or `[Subbed]`.

---

## Features

- **Custom Delimiters**: Remove unwanted parts of filenames (e.g., `(Dub)`, `[Subbed]`).
- **Season Support**: Add season numbers to filenames (e.g., `S01`, `S02`).
- **Episode Numbering**: Start episode numbering from a specified value.
- **Batch Processing**: Rename all files in a directory that match the expected format.
- **Standalone Executable**: No Python installation required!

---

## Usage

### Prerequisites

- **For the Python script**: Python 3.x installed on your system.
- **For the `.exe` file**: No prerequisites needed. Just download and run!

---

### **Option 1: Using the Python Script**

1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/hasinajy/anime-renamer.git
   cd anime-renamer
   ```

2. Run the script:
   ```bash
   python rename-anime.py -p <directory> -s <start_episode> -S <season> -d <delimiter>
   ```

---

### **Option 2: Using the Standalone `.exe` File**

1. Download the `.exe` file from the [Releases](https://github.com/hasinajy/anime-renamer/releases) page:
   - [rename-anime.exe](https://github.com/hasinajy/anime-renamer/releases/download/v1.0.0/rename-anime.exe)

2. Place the `.exe` file in the directory containing your anime files (or any directory of your choice).

3. Run the tool:
   - **Double-click**: Double-click the `.exe` file to run it with default settings.
   - **Command Line**: Open a command prompt and run:
     ```bash
     rename-anime.exe -p <directory> -s <start_episode> -S <season> -d <delimiter>
     ```

4. **Global Access (Optional)**:
   If you want to use the `.exe` file globally (from any directory), add its location to your system's **Environment Variables**:
   - **Windows**:
     1. Right-click on **This PC** or **My Computer** and select **Properties**.
     2. Click on **Advanced system settings** > **Environment Variables**.
     3. Under **System Variables**, find the `Path` variable and click **Edit**.
     4. Add the full path to the directory containing `rename-anime.exe`.
     5. Click **OK** to save changes.
   - Now, you can run the tool from any directory:
     ```bash
     rename-anime.exe -p <directory> -s <start_episode> -S <season> -d <delimiter>
     ```

---

#### Arguments

| Argument            | Description                                                      |
| ------------------- | ---------------------------------------------------------------- |
| `-p`, `--path`      | Directory containing anime files (default: current directory).   |
| `-s`, `--start`     | Starting episode number (default: 1).                            |
| `-S`, `--season`    | Season number (optional, adds `S<season>` to the filename).      |
| `-d`, `--delimiter` | Custom delimiter to truncate titles (e.g., `(Dub)`, `[Subbed]`). |

---

#### Examples

1. **Basic Usage**:
   Rename files in the current directory, starting from episode 1:
   ```bash
   rename-anime.exe
   ```

2. **Custom Delimiter**:
   Remove `(Dub)` from filenames:
   ```bash
   rename-anime.exe -d "(Dub)"
   ```

3. **Season and Episode**:
   Rename files for Season 2, starting from episode 10:
   ```bash
   rename-anime.exe -S 2 -s 10
   ```

4. **Complex Example**:
   Rename files in a specific directory, starting from episode 5, for Season 1, and remove `[Subbed]`:
   ```bash
   rename-anime.exe -p "C:\path\to\anime" -s 5 -S 1 -d " [Subbed]"
   ```

---

## Input and Output

### Input File Format
The script expects filenames in the following format:
```
Watch <Title> Episode <Episode Number>.<extension>
```
Example:
```
Watch Naruto Shippuden Episode 1.mp4
```

### Output File Format
The script renames files in the following format:
```
<Title> - S<Season> - E<Episode Number>.<extension>
```
Example:
```
Naruto Shippuden - S01 - E01.mp4
```

---

## Error Handling

- The script skips files that do not match the expected format.
- Errors are logged to the console for debugging.

---

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## Author

[Hasina JY](https://github.com/hasinajy)