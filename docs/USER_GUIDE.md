# Batch Renamer PRO: User Guide

Version 3.8.8 · Build BR261126 · The same content is available inside the program (press `F1` for shortcuts, or open the User guide from the Menu).

## Contents

- [Install and run](#install-and-run)
- [Getting started](#getting-started)
- [Rename rules](#rename-rules)
- [Preview & statuses](#preview--statuses)
- [Metadata & SEO](#metadata--seo)
- [Create files](#create-files)
- [Undo & safety](#undo--safety)
- [Placeholders](#placeholders)
- [Settings](#settings)
- [Troubleshooting](#troubleshooting)

## Install and run

Download `BatchRenamer.exe` from the [latest release](https://github.com/NihadSquare/BatchRenamer/releases/latest) and double-click it. The EXE is not code-signed, so Windows SmartScreen or antivirus software may warn on first launch. Run it only if you downloaded it from the official page.

The audio tag placeholders `{artist}`, `{title}` and `{album}` are not available in this build.

> Some status text and example values below depend on your settings. Date examples show the day this guide was generated.

## Getting started


### Quick start

1. Click Browse… (Ctrl+O) and pick the folder that holds the files or folders you want to rename.
2. Choose Files or Folders (top right of the Source card). Switch on Include subfolders to reach everything below the folder.
3. Open a rules page from the sidebar (Name & Serial, Chars & Words, Regex, Pattern, CSV). The preview updates while you type.
4. Read the New name column and the status pills. Untick any item to leave it alone, or double-click a New name to type your own.
5. Press Rename Files (Ctrl+R). Changed your mind? Undo (Ctrl+Z) puts every name back.


### Finding your way around

- Sidebar: the rules pages, Statistics, Reset, the Theme window and the Menu. Ctrl+1…7 jumps between pages; Ctrl+B collapses the sidebar to icons.
- Source card: folder, Files / Folders switch, subfolders, hidden-file filter, “Copy to RenamedFiles”, conflict handling and the file-type filter.
- Rules card: the step chips show which rules are active and in which order they run.
- Preview table: current name, new name and a status pill per item. Search, filter, sort and Inspector live above it.
- Action bar: progress, Undo, Redo, Export CSV and the big Rename button.


### Good to know

- Nothing on disk changes until you press the Rename (or Write Metadata) button.
- Your settings, theme, accent color, recent folders and undo history are remembered between sessions.
- Reset in the sidebar clears every field and the preview, but keeps your theme and undo history.


### Keyboard shortcuts


**Files**

| Keys | Action |
|---|---|
| `Ctrl` + `O` | Select folder |
| `F5` | Refresh the folder and preview |
| `Ctrl` + `I` | Import CSV |
| `Ctrl` + `E` | Export CSV |

**Rename**

| Keys | Action |
|---|---|
| `Ctrl` + `R` | Rename — or write metadata on the Metadata page |
| `Ctrl` + `Z` | Undo |
| `Ctrl` + `Y` | Redo |
| `Ctrl` + `Shift` + `Z` | Redo (alternative) |
| `Ctrl` + `1…7` | Jump to a rules page |

**Table**

| Keys | Action |
|---|---|
| `Ctrl` + `F` | Search the preview |
| `Ctrl` + `A` | Select all rows |
| `Space` | Tick / untick the highlighted rows |
| `Double-click` | Edit a new name — or a file’s metadata on the Metadata page |
| `Delete` | Remove manual names from highlighted rows |
| `Right-click` | Row menu: open, show in Explorer, copy… |
| `Esc` | Clear the highlighted rows |
| `Click a header` | Sort (again = reverse, again = off) |

**App**

| Keys | Action |
|---|---|
| `Ctrl` + `B` | Collapse / expand the sidebar |
| `Ctrl` + `D` | Switch to the next color theme |
| `Ctrl` + `,` | Open Settings |
| `F1` | Show this window |

## Rename rules

Rules run top to bottom in a fixed order, shown by the chips above the rules: CSV › Characters › Words › Regex › Clean-up › Name / Pattern › Case › Serial › Extension. A chip lights up while its step is in use.


### Name & Serial

- Common name replaces the whole name (the extension stays). Case changes capitalization: lowercase, UPPERCASE, Title Case, Sentence case.
- New extension swaps the extension (files only). Leave it at No Change to keep it.
- “Add Serial” numbers the ticked items, restarting in every folder. Start at sets the first number, Position is Before or After the name.
- Serial formats: 1, 2, 3   •   01, 02, 03   •   001, 002, 003   •   0001, 0002, 0003   •   A, B, C   •   a, b, c   •   I, II, III   •   i, ii, iii.

- Common name “Trip”, Add Serial, format 01, After Name:: `IMG_5012.jpg   IMG_5013.jpg` → `Trip 01.jpg   Trip 02.jpg`

### Chars & Words

- Remove characters deletes (or replaces) every listed character. Remove words works on whole words only, separated by commas, and ignores case.
- Auto Clean-up collapses runs of spaces, dashes, underscores and dots into a single space and trims the ends.

- Remove characters “_”, replace with a space:: `holiday_photo_01.jpg` → `holiday photo 01.jpg`

### Regex

- Find takes a regular expression, Replace with can use \1, \2 … for groups. It works on the name without the extension. Ignore Case is on by default.
- An invalid pattern is shown in red and blocks renaming until you fix it.

- Find (\d+)_(\w+)  →  Replace \2_\1:: `2024_report.pdf` → `report_2024.pdf`

### Pattern

- Build a name from placeholders such as {name}, {counter}, {date_Y-m-D} or {parent_folder}. A pattern overrides Common name.
- Insert placeholder lists every placeholder. Unknown data (for example a missing EXIF date) becomes “Unknown”. See the Placeholders tab for the full list.

- Pattern {parent_folder}_{counter}:: `a.jpg   b.jpg   (folder “Holiday”)` → `Holiday_01.jpg   Holiday_02.jpg`

### CSV

- Import CSV… (Ctrl+I): the first column is the current name, another column holds the new name. Pick that column in New-name column.
- Matching is by current name (with or without extension). Files not in the CSV simply fall through to the other rules.


## Preview & statuses


### Reading the preview

- Click the box in the first column to tick or untick an item; click the header box to flip all visible rows. Space toggles the highlighted rows.
- Double-click a New name to edit it by hand. Right-click for Open, Show in Explorer, Copy names and Reset.
- Search (Ctrl+F) and the status filter narrow what you see. Click a column header to sort: once ascending, twice descending, three times off.
- Select ▾ offers select all / none / invert / only matching the search. Inspector shows the metadata stored inside the highlighted file.
- The summary above the table counts items, selected items, items to rename and any conflicts or invalid names.


### What the status pills mean

These are drawn by the same code as the table, so they look exactly like the real thing (colors follow your theme).


**Rename and copy pills**

| Status | Meaning |
|---|---|
| Rename | The item will be renamed when you press Rename. |
| Copy | “Copy to RenamedFiles” is on: a renamed copy is written and the original stays untouched. |
| Manual | You typed this New name yourself (double-click the cell). It overrides the rules. Delete removes it again. |
| Conflict → $1 | Another item would get the same name. The extra item gets a space, the symbol ($) and a number; the first keeps its clean name. |
| Conflict – skipped | Same clash, but “Resolve conflicts with” is off, so this item is left out. |
| Empty name | The rules produce a name with nothing in it. |
| Reserved name | Windows does not allow names like CON, PRN, AUX, NUL, COM1… |
| Name too long | More than 255 characters. |
| Path too long (260+) | Folder path plus new name would pass the Windows 260-character limit. |
| Unchanged | The rules give the same name as now, so nothing will happen to this item. |
| Skipped | The tick box in front of the item is off. It is ignored completely. |

**Metadata pills**

| Status | Meaning |
|---|---|
| Will write | Metadata will be written to this file. |
| Will write · edited | Same, using values you edited for this file only (double-click it). |
| No change | The file already contains exactly these values. |
| Nothing to write | All metadata fields are empty, so there is nothing to add. |
| Unsupported type | Metadata is not supported for this kind of file (JPG, PNG, WebP, SVG, DOCX, XLSX, PPTX are). |
| Skipped | Unticked, so it is ignored. |

## Metadata & SEO

The Metadata page writes titles, descriptions, keywords and credits straight into your files so search engines, stock sites and file managers can read them. File names are never changed here.


### Fields

- Title
- Description
- Keywords
- Author
- Copyright
- Website / credit
- Empty fields are never touched. Filled fields replace what is inside the file; everything else in the file’s metadata is kept.
- Fields accept placeholders such as {title_name} and {name_words} (see the Placeholders tab). Fill from file name sets sensible defaults in one click.
- Supported files: JPG, PNG, WebP, SVG, DOCX, XLSX, PPTX.


### Per-file values

- Double-click a file (or right-click › Edit metadata) to change values for that file only. Reset returns it to the page’s values.
- Import CSV… reads per-file values from a spreadsheet with columns File, Folder, Title, Description, Keywords, Author, Copyright, URL. Filled CSV cells win over the fields above.
- Export CSV saves everything shown, including SEO scores and warnings.


### When writing

- “Back up originals first (undoable)” copies each original to _metadata_backup\<date-time> first, so Undo can restore it.
- “Write copies to “RenamedFiles”” leaves originals alone and writes new files there.
- “Write in place (no backup, no undo)” changes the originals directly; it cannot be undone.


### SEO score

- Every file gets a score out of 100 and a list of warnings in the Inspector.
- Title: 30–60 characters. Description: 70–160 characters. Keywords: 3–10 (more than 15 looks like stuffing).
- Author, copyright and website / credit should be filled. Identical titles or descriptions on several files are flagged.
- Use the status filter “SEO issues” to list files scoring below 85.


## Create files

Create makes real, valid, empty files or folders in the selected folder: handy for templates, tests and placeholders.

- Type: Folder, TXT, CSV, PNG, JPG, PDF, DOCX, XLSX. PNG, JPG, PDF, DOCX and XLSX open in their normal programs.
- Base name and Count (1 to 1000). To create more than one item, Serial must be on.
- Start at, Position and Format work like the Serial settings on the rename page.
- Preview & Create shows every name first. Names that already exist are skipped, never overwritten.

- Base name “Invoice”, count 3, format 001, After Name:: `(empty folder)` → `Invoice 001.docx   Invoice 002.docx   Invoice 003.docx`

## Undo & safety


### Built-in protection

- Renaming is two-phase: when names swap or chain (a→b, b→c) items pass through a temporary name, so nothing is overwritten.
- Conflicts are resolved or skipped, invalid names are skipped, and an item that vanished or is locked is reported without stopping the rest.
- Batches above the size set in Settings (100 by default), and system folders (drive roots, Windows, Program Files, your profile folder), ask for an extra confirmation.
- Folders are renamed deepest first, and the RenamedFiles and _metadata_backup folders are never scanned.


### Undo and redo

- Undo (Ctrl+Z) and Redo (Ctrl+Y or Ctrl+Shift+Z) work on whole operations. The last 100 steps are kept even after you close the program (Settings › History & safety sets the limit).
- Undoing a Copy deletes the copies from RenamedFiles. Undoing metadata with a backup restores the original files.
- Menu › Clear undo history forgets the saved steps; it does not touch your files.


### If something goes wrong

- If the program is closed or crashes mid-rename, the next start repairs leftover temporary names and adds the finished items to Undo.
- Items that failed are listed after the run; the rest are still done.
- Preferences (theme, accent, animation speed, startup behavior, table look, undo limit, confirmation size…) are in Settings (Ctrl+,). Settings and history files live in the settings folder (Menu › Open settings folder).


## Placeholders

Use placeholders in the Pattern box (rename) or in Metadata fields. They are replaced for every file. This page is generated from the program’s own lists, so it is always complete.


### Rename › Pattern placeholders


**Basic**

| Placeholder | Meaning | Example |
|---|---|---|
| `{name}` | file name after the rules above, without the extension |  |
| `{ext}` | extension without the dot |  |
| `{counter}` | serial number from the Serial settings (per folder) |  |
| `{random_str}` | 8 random letters / digits (stable while you preview) |  |
| `{parent_folder}` | name of the folder the file is in |  |

**File info**

| Placeholder | Meaning | Example |
|---|---|---|
| `{size_kb}` | file size, e.g. 512KB |  |
| `{date_modified}` | date the file was last changed (YYYY-MM-DD) |  |
| `{time_modified}` | time the file was last changed (HH-MM-SS) |  |
| `{date_created}` | date the file was created |  |
| `{time_created}` | time the file was created |  |

**Date & time (now)**

| Placeholder | Meaning | Example |
|---|---|---|
| `{date_Y-M-D}` | current date / time format | `2026-November-25` |
| `{date_Y-m-D}` | current date / time format | `2026-11-25` |
| `{date_D-M-Y}` | current date / time format | `25-November-2026` |
| `{date_D-m-Y}` | current date / time format | `25-11-2026` |
| `{date_M-D-Y}` | current date / time format | `November-25-2026` |
| `{date_m-D-Y}` | current date / time format | `11-25-2026` |
| `{YmD_HMS}` | current date / time format | `2026-11-25_23-06-18` |
| `{YMD_HMS}` | current date / time format | `2026-November-25_23-06-18` |
| `{YmD_IMSp}` | current date / time format | `2026-11-25_11-06-18PM` |
| `{YMD_IMSp}` | current date / time format | `2026-November-25_11-06-18PM` |
| `{time_24hr}` | current date / time format | `23-06-18` |
| `{time_12hr}` | current date / time format | `11-06-18PM` |
| `{year}` | current date / time format | `2026` |
| `{month_n}` | current date / time format | `11` |
| `{month_w}` | current date / time format | `November` |
| `{day}` | current date / time format | `25` |

**Image  (EXIF, size)**

| Placeholder | Meaning | Example |
|---|---|---|
| `{date_taken}` | photo date from EXIF (YYYY-MM-DD) |  |
| `{time_taken}` | photo time from EXIF |  |
| `{camera_model}` | camera model from EXIF |  |
| `{width}` | image width in pixels |  |
| `{height}` | image height in pixels |  |

**Audio  (tags)**

| Placeholder | Meaning | Example |
|---|---|---|
| `{artist}` | artist tag of an audio file |  |
| `{title}` | title tag of an audio file |  |
| `{album}` | album tag of an audio file |  |

### Metadata placeholders


**Metadata fields**

| Placeholder | Meaning | Example |
|---|---|---|
| `{title_name}` | file name as readable text (IMG_trip-2024 → Img Trip 2024) |  |
| `{name_words}` | the words of the file name, comma separated |  |
| `{name}` | file name without extension |  |
| `{filename}` | full file name |  |
| `{ext}` | extension without the dot |  |
| `{folder}` | name of the containing folder |  |
| `{counter}` | 1, 2, 3 … per folder |  |
| `{year}` | current year |  |
| `{month_w}` | current month name |  |
| `{month_n}` | current month number |  |
| `{day}` | current day |  |
| `{date}` | today’s date |  |
| `{date_modified}` | date the file was last changed |  |
| `{date_created}` | date the file was created |  |
| `{size_kb}` | file size, e.g. 512KB |  |
## Settings

Open with `Ctrl+,`. Settings are grouped into **Appearance**, **Startup & Folders**, **Preview Table**, **History & Safety** and **Data**. Eight color themes are included (Midnight, Cobalt, Dracula, Forest, Sunset, Solarized, Ivory Orange, Blush Red), with an optional custom accent color. `Ctrl+D` switches to the next theme. Settings can be exported to and imported from a JSON file.

Settings and undo history are stored in `%APPDATA%\BatchRenamer`.

## Troubleshooting

| Problem | What to check |
|---|---|
| No items in the preview | File-type filter, Files / Folders switch, hidden-file filter, search box and status filter. |
| An item fails to rename | Close any program using the file and check folder permissions. Other items are still processed. |
| Placeholder gives “Unknown” | The file has no such data, or the placeholder is not available in this build (see Install and run). |
| Conflicts | Turn on “Resolve conflicts with”, or change the rules so names are unique. |
| Program closed mid-rename | Start it again: leftover temporary names are repaired. |

Still stuck? [Open an issue](https://github.com/NihadSquare/BatchRenamer/issues) with your version, Windows version, steps and a screenshot.
