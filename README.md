# 🖥 Batch Renamer v2.7

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![Made by](https://img.shields.io/badge/Made%20By-NihadSquare-blue)
![Version](https://img.shields.io/badge/version-2.7.10-green)

> A professional, feature-rich batch file and folder renaming tool with advanced pattern matching, CSV support, dark mode, and comprehensive file analytics — built in Python for Windows. Completely **FREE** and now available as a standalone executable.

---

## 🚀 What's New in v2.7

### ✨ Major New Features
- **🎯 Dual Mode Support**: Rename both files AND folders with separate modes
- **📊 Advanced File Statistics**: Comprehensive analytics with storage insights and file type analysis
- **🎨 Theme System**: Toggle between dark and light modes
- **🔤 Pattern-Based Renaming**: Smart placeholders for metadata (date, time, size, EXIF, etc.)
- **📈 CSV Import/Export**: Bulk rename using CSV files and export rename data
- **🎪 Enhanced Serial Formats**: Roman numerals, letters, and custom numbering systems
- **🔍 Smart Filtering**: Search, filter by status, and selective file processing

### 🛠 Enhanced Functionality
- **📁 Folder Renaming**: Complete support for folder structures
- **🎯 Selective Processing**: Choose individual files to rename with checkboxes
- **🔧 Conflict Resolution**: Automatic duplicate name handling with custom symbols
- **📋 Context Menu**: Right-click options for file preview, properties, and location
- **⌨️ Keyboard Shortcuts**: Full keyboard navigation and quick actions
- **📱 Responsive UI**: Improved layout with better scaling and organization

---

## 🌟 Key Features

### 🗂 Core Renaming
- **Multiple Renaming Modes**: New naming, character cleanup, word replacement, pattern-based, and CSV-based
- **Smart Serial Numbers**: Custom formats (1, 01, 001, A, a, I, i) with flexible positioning
- **Auto Cleanup**: Remove extra spaces, dots, and special characters automatically
- **Case Conversion**: lowercase, UPPERCASE, Title Case, and Sentence case
- **Extension Control**: Change file extensions while keeping names intact

### 🔍 Advanced Capabilities
- **Pattern Placeholders**: 
  - `{name}`, `{ext}`, `{counter}`, `{random_str}`
  - `{date_created}`, `{time_modified}`, `{size_kb}`
  - `{parent_folder}`, `{year}`, `{month_Jan}`, `{day}`
  - EXIF data: `{date_taken}`, `{camera_model}`, `{width}x{height}`
  - Audio tags: `{artist}`, `{title}`, `{album}`

### 📊 File Management
- **Live Preview**: Real-time changes before applying
- **Selective Processing**: Checkbox system for individual file selection
- **Subfolder Support**: Process files in nested directories
- **System File Protection**: Skip hidden and system files
- **Conflict Resolution**: Automatic duplicate name handling

### 🎨 User Experience
- **Dark/Light Themes**: Toggle between modern dark and clean light interfaces
- **Context Menus**: Right-click for quick actions (preview, copy, properties)
- **Keyboard Shortcuts**: Full keyboard navigation support
- **Progress Tracking**: Real-time progress bar with time estimates
- **Undo/Redo**: Complete operation history with unlimited undo/redo

### 📈 Analytics & Export
- **File Statistics**: Comprehensive storage analytics and file type breakdowns
- **CSV Import**: Bulk rename using spreadsheet data
- **CSV Export**: Save rename previews and operations
- **Storage Analytics**: Size distribution, file categories, and efficiency metrics

---

## 🖼 SCREENSHOTS
<div align="center">
  <img src="https://github.com/NihadSquare/BatchRenamer/blob/main/Screenshots/BR-Screenshot-5.jpg" width="500"/>
  <p><em>Modern interface with dark theme and advanced controls</em></p>
</div>

---

## 🖥 Installation & Usage

### ✅ Standalone Executable (Recommended)
**No Python required!** Simply download and run:
```bash
# Double-click to run:
BatchRenamer.exe
```

**Requirements for .exe version:**
- Windows 10 or later
- 50MB free space
- No additional dependencies

### 🔧 Python Script Version
If running the source code:
```bash
# Install dependencies:
pip install pillow

# Run the application:
python BatchRenamer.py
```

**Requirements for .py version:**
- Python 3.8+
- Pillow library
- tkinter (usually included with Python)

---

## 📖 Quick Start Guide

1. **Launch** the application
2. **Select Folder** containing files/folders to rename
3. **Choose Mode**: File or Folder renaming
4. **Select Method** from tabs:
   - 🆕 **New Name & Serial**: Common name with sequential numbers
   - 🔤 **Character Cleanup**: Remove/replace specific characters
   - 📝 **Word Cleanup**: Replace or remove specific words
   - 🎯 **Pattern**: Advanced placeholders for metadata
   - 📊 **CSV-Based**: Import names from spreadsheet
5. **Preview** changes in the live table
6. **Select** specific files using checkboxes
7. **Click "Rename 🚀"** to apply changes

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+O` | Open folder |
| `Ctrl+I` | Import CSV |
| `Ctrl+P` | Preview renames |
| `Ctrl+R` | Execute rename |
| `Ctrl+Z` | Undo |
| `Ctrl+Y` | Redo |
| `Ctrl+D` | Toggle dark mode |
| `F1` | Show shortcuts help |
| `Tab` | Next field |
| `Shift+Tab` | Previous field |
| `Esc` | Clear field/Deselect |

---

## 🗂 File Structure

```
BatchRenamer/
├── 🚀 BatchRenamer.exe         # Main executable
├── 📁 resources/               # Required resources
│   ├── 🖼️ BatchRenamer.png     # Application icon
│   ├── 🎯 BR.ico               # Window icon
│   └️── 📄 ReadMe.txt           # This file
└── 
```

**Important**: Keep the `resources` folder with the `.exe` file for proper functionality.

---

## 🔧 Technical Details

### Supported File Systems
- NTFS, FAT32, exFAT
- Local drives, network shares, external drives
- Long path names (with Windows support)

### Performance
- Handles thousands of files efficiently
- Background processing with live progress updates
- Low memory footprint
- Fast preview generation

### Safety Features
- Preview before any changes
- Complete undo/redo system
- Conflict detection and resolution
- System file protection
- No overwriting without confirmation

---

## 🤝 Support & Community

- **Report Issues**: GitHub Issues page
- **Feature Requests**: Welcome via GitHub
- **Documentation**: Included in application help

---

## 📄 License

MIT License - Free for personal and commercial use.

---

## 🏆 Credits

**Developed by Nihad Square**  
*Batch Renamer v2.7.10 - Professional File Management Made Simple*

---

<div align="center">

**💫 Transform your file management workflow with Batch Renamer v2.7!**

</div>
