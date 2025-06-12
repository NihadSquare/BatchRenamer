import os
import stat
import shutil
import tkinter as tk
from tkinter import filedialog, ttk, messagebox, Menu
import time
import re
import webbrowser

try:
    from idlelib.tooltip import Hovertip
except ImportError:
    Hovertip = lambda widget, text: None  # Fallback if idlelib is missing


class FileRenamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Batch Renamer v1.8.5 - Developed by Nihad Square")
        self.original_names = []
        self.renamed_names = []
        self.undo_data = None
        
        self.build_gui()
        self.update_rename_button_state()

        style = ttk.Style()
        style.theme_use("clam")  # Switch to a more customizable theme like 'default' or 'clam'

        #Reset Button Style
        style.configure("Reset.TButton",
            background="#dc3545",
            foreground="white",
            padding=4,
            font=("Segoe UI", 10, "bold"))

        style.map("Reset.TButton",
            background=[("active", "#c82333"), ("disabled", "#cccccc")])
        #Rename Button Style
        style.configure("Custom.TButton",
                        background="#005F99",   # Button color
                        foreground="white",     # Text color
                        font=("Segoe UI", 11, "bold"),
                        padding=6)

        style.map("Custom.TButton",
                  background=[('active', '#00AEEF'), ('disabled', '#cccccc')])
        # Configure progress bar style
        style.configure("green.Horizontal.TProgressbar",
                        troughcolor="#DBFCE3",   # background of the track
                        background="#0AE23C",    # actual bar color (green)
                        thickness=25)

    def open_about(self):
        webbrowser.open("https://github.com/NihadSquare/BatchRenamer")  # Replace with your GitHub link

    def open_tutorial(self):
        webbrowser.open("https://www.youtube.com/watch?v=your_tutorial_id")  # Replace with your video/tutorial URL

    def open_contact(self):
        webbrowser.open("https://nihad.carrd.co")  # Replace with your email


    def build_gui(self):
        self.folder_path = tk.StringVar()
        self.include_subfolders = tk.BooleanVar()
        self.save_in_folder = tk.BooleanVar()
        self.remove_chars = tk.StringVar()
        self.replace_with = tk.StringVar()
        self.word_remove = tk.StringVar()
        self.word_replace = tk.StringVar()
        self.auto_cleanup = tk.BooleanVar()
        self.common_name = tk.StringVar()
        self.add_serial = tk.BooleanVar()
        self.serial_position = tk.StringVar(value='After')
        self.start_number = tk.IntVar(value=1)
        self.conflict_resolve = tk.BooleanVar(value=True)
        self.file_type_filter = tk.StringVar(value="All Files")
        self.case_option = tk.StringVar(value="No Change")
        self.skip_hidden = tk.BooleanVar(value=True)
        

        heading = ttk.Label(self.root, text="📁 Batch Renamer",
                            font=("Segoe UI", 22, "bold"), foreground="#00395d")
        heading.pack(pady=(15, 5))

        
        # Menu dropdown (top right)
        menu_button = tk.Menubutton(self.root, text="☰", fg="#979797",
                                    font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2")
        menu = Menu(menu_button, tearoff=0, bg="white", fg="black")

        menu.add_command(label="About", command=self.open_about)
        menu.add_command(label="Tutorial", command=self.open_tutorial)
        menu.add_command(label="Contact", command=self.open_contact)

        menu_button.config(menu=menu)
        menu_button.place(relx=0.98, y=10, anchor="ne")
        
        # Reset Button (to the left of menu button)
        reset_button = tk.Button(self.root, text="↺", command=self.reset_all_fields,
            font=("Roboto", 10, "bold"),
            bg="#979797",          # red background
            fg="white",            # white text
            activebackground="#d32f2f",  # darker red on click
            activeforeground="white",
            relief="flat", cursor="hand2",         # or "raised", "groove"
            bd=2,                  # border thickness
            padx=0,               # horizontal padding
            pady=0                 # vertical padding
        )
        reset_button.place(relx=0.94, y=12, anchor="ne")
        Hovertip(reset_button, "Reset form")


        # Section 1: Folder Selection
        frame1 = ttk.LabelFrame(self.root, text="1. Folder Selection")
        frame1.pack(fill="x", padx=10, pady=5)
        entry = ttk.Entry(frame1, textvariable=self.folder_path, state='readonly', width=50)
        entry.pack(side="left", fill="x", expand=True, padx=5)
        Hovertip(entry, "Select the folder containing files to rename")
        ttk.Button(frame1, text="Browse", command=self.select_folder).pack(side="left", padx=5)
        self.include_subfolders = tk.BooleanVar(value=False)
        self.include_checkbox = tk.Label(frame1, text="⬜ Include Subfolders", font=("Segoe UI", 9), cursor="hand2")
        self.include_checkbox.pack(side="left", padx=10)

        def toggle_include():
            if self.include_subfolders.get():
                self.include_checkbox.config(text="⬜ Include Subfolders")
                self.include_subfolders.set(False)
            else:
                self.include_checkbox.config(text="✅ Include Subfolders")
                self.include_subfolders.set(True)

        self.include_checkbox.bind("<Button-1>", lambda e: toggle_include())

        self.save_in_folder = tk.BooleanVar(value=False)
        self.save_checkbox = tk.Label(frame1, text="⬜ Save in Folder", font=("Segoe UI", 9), cursor="hand2")
        self.save_checkbox.pack(side="left", padx=5)

        def toggle_save():
            if self.save_in_folder.get():
                self.save_checkbox.config(text="⬜ Save in Folder")
                self.save_in_folder.set(False)
            else:
                self.save_checkbox.config(text="✅ Save in Folder")
                self.save_in_folder.set(True)

        self.save_checkbox.bind("<Button-1>", lambda e: toggle_save())


        # Section 2a: Character Cleanup
        frame2 = ttk.LabelFrame(self.root, text="2a. Character Cleanup")
        frame2.pack(fill="x", padx=10, pady=5)
        ttk.Label(frame2, text="Characters to Remove:").grid(row=0, column=0, padx=5)
        ttk.Entry(frame2, textvariable=self.remove_chars).grid(row=0, column=1, padx=5)
        ttk.Label(frame2, text="Replace With:").grid(row=0, column=2, padx=5)
        ttk.Entry(frame2, textvariable=self.replace_with).grid(row=0, column=3, padx=5)
        cleanup_chk = ttk.Checkbutton(frame2, text="Auto Cleanup", variable=self.auto_cleanup)
        cleanup_chk.grid(row=0, column=4, padx=40)
        Hovertip(cleanup_chk, "Remove multiple dots/spaces/symbols")

        # Section 2b: Word-Based Cleanup
        frame2b = ttk.LabelFrame(self.root, text="2b. Word-Based Cleanup")
        frame2b.pack(fill="x", padx=10, pady=5)
        ttk.Label(frame2b, text="Words to Remove:").grid(row=0, column=0, padx=5)
        ttk.Entry(frame2b, textvariable=self.word_remove).grid(row=0, column=1, padx=5)
        ttk.Label(frame2b, text="Replace With:").grid(row=0, column=2, padx=5)
        ttk.Entry(frame2b, textvariable=self.word_replace).grid(row=0, column=3, padx=5)
        ttk.Checkbutton(frame2b, text="Add $ if conflict", variable=self.conflict_resolve).grid(row=0, column=4, padx=40)

        # Section 3: New Naming Options
        frame3 = ttk.LabelFrame(self.root, text="3. New Naming Options")
        frame3.pack(fill="x", padx=10, pady=5)
        ttk.Label(frame3, text="Common Name:").grid(row=0, column=0, padx=5)
        ttk.Entry(frame3, textvariable=self.common_name).grid(row=0, column=1, padx=5)
        ttk.Checkbutton(frame3, text="Add Serial Number", variable=self.add_serial).grid(row=0, column=2, padx=5)
        ttk.Label(frame3, text="Start From:").grid(row=0, column=3, padx=5)
        ttk.Entry(frame3, textvariable=self.start_number, width=5).grid(row=0, column=4, padx=5)
        ttk.Label(frame3, text="Position:").grid(row=0, column=5, padx=5)
        ttk.Combobox(frame3, textvariable=self.serial_position, values=["Before", "After"], width=7, state="readonly").grid(row=0, column=6, padx=5)

        # Section 4: Filters and Case
        frame4 = ttk.LabelFrame(self.root, text="4. File Type and Filters")
        frame4.pack(fill="x", padx=10, pady=5)
        ttk.Label(frame4, text="File Types:").pack(side="left", padx=5)
        ttk.Combobox(frame4, textvariable=self.file_type_filter, values=["All Files", ".png", ".jpg", ".jpeg", ".webp", ".pdf", ".docx", ".svg", ".ai", ".psd", ".txt", ".csv"], width=10, state="readonly").pack(side="left", padx=5)
        ttk.Label(frame4, text="Case:").pack(side="left", padx=5)
        ttk.Combobox(frame4, textvariable=self.case_option, values=["No Change", "lowercase", "UPPERCASE", "Title Case"], width=15, state="readonly").pack(side="left", padx=5)
        ttk.Checkbutton(frame4, text="Skip Hidden/System Files", variable=self.skip_hidden).pack(side="right", padx=40)

        # Section 5: Preview and Rename
        frame5 = ttk.LabelFrame(self.root, text="5. Preview and Rename")
        frame5.pack(fill="both", expand=True, padx=10, pady=5)
        self.tree = ttk.Treeview(frame5, columns=("old", "new"), show="headings")
        self.tree.heading("old", text="Old Name")
        self.tree.heading("new", text="New Name")
        self.tree.tag_configure("changed", foreground="green")
        self.tree.tag_configure("unchanged", foreground="red")
        self.tree.pack(fill="both", expand=True, padx=5, pady=5)

        progress_frame = ttk.Frame(self.root)
        progress_frame.pack(fill="x", padx=20, pady=(5, 7))
        self.progress = ttk.Progressbar(progress_frame, mode='determinate',
                                style="green.Horizontal.TProgressbar")
        self.progress.pack(side="left", fill="x", expand=True)
        self.progress_label = ttk.Label(progress_frame, text="", width=25, anchor="e")
        self.progress_label.pack(side="right")
        Hovertip(progress_frame, "Progress Bar")
        self.rename_count_label = ttk.Label(self.root, text="", anchor="center", font=("Segoe UI", 10, "bold"))
        self.rename_count_label.pack(fill="x", padx=20, pady=(0, 10))

        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=5)
        self.preview_btn = ttk.Button(btn_frame, text="Preview", command=self.preview_renames)
        self.preview_btn.pack(side="left", padx=10)
        self.rename_btn = ttk.Button(btn_frame, text="Rename 🚀", style="Custom.TButton", command=self.rename_files)
        self.rename_btn.pack(side="left", padx=10)
        self.undo_btn = ttk.Button(btn_frame, text="Undo", command=self.undo_last_rename, state="disabled")
        self.undo_btn.pack(side="left", padx=10)

        self.status_label = ttk.Label(self.root, text="")
        self.status_label.pack(fill="x", padx=10)

        ttk.Label(self.root, text="Developed by Nihad Square  |  Batch Renamer v1.8.5",
                  font=("Roboto", 7, "bold"), foreground="#979797").pack(pady=(10, 5))

        for var in [self.folder_path, self.remove_chars, self.word_remove, self.common_name, self.auto_cleanup, self.add_serial]:
            var.trace_add('write', lambda *args: self.update_rename_button_state())

    def update_rename_button_state(self):
        folder_selected = bool(self.folder_path.get())
        cleanup_active = bool(self.remove_chars.get() or self.word_remove.get() or self.auto_cleanup.get())
        naming_active = bool(self.common_name.get() or self.add_serial.get())
        self.rename_btn.config(state='normal' if folder_selected and (cleanup_active or naming_active) else 'disabled')

    def select_folder(self):
        path = filedialog.askdirectory()
        if path:
            self.folder_path.set(path)
            
        folder = self.folder_path.get()

        matched_files = []
        for root, dirs, files in os.walk(folder):
            if not self.include_subfolders.get() and root != folder:
                continue
            for file in files:
                file_path = os.path.join(root, file)
                if self.skip_hidden.get() and self.is_hidden(file_path):
                    continue
                if self.file_type_filter.get() != "All Files" and not file.endswith(self.file_type_filter.get()):
                    continue
                matched_files.append(file_path)

        self.progress_label.config(text=f"{len(matched_files)} Files Found")
        for old_path in matched_files:
            file = os.path.basename(old_path)
            root = os.path.dirname(old_path)
            name, ext = os.path.splitext(file)
            new_name = name

    def apply_case(self, name):
        opt = self.case_option.get()
        return name.lower() if opt == "lowercase" else name.upper() if opt == "UPPERCASE" else name.title() if opt == "Title Case" else name

    def is_hidden(self, file_path):
        name = os.path.basename(file_path)
        if name.startswith("."):
            return True
        try:
            attrs = os.stat(file_path).st_file_attributes
            return bool(attrs & (stat.FILE_ATTRIBUTE_HIDDEN | stat.FILE_ATTRIBUTE_SYSTEM))
        except AttributeError:
            return False

    def preview_renames(self):
        folder = self.folder_path.get()
        if not folder:
            messagebox.showwarning("Warning", "Please select a folder.")
            return
        self.tree.delete(*self.tree.get_children())
        self.original_names.clear()
        self.renamed_names.clear()
        counter = self.start_number.get()

        matched_files = []
        for root, dirs, files in os.walk(folder):
            if not self.include_subfolders.get() and root != folder:
                continue
            for file in files:
                file_path = os.path.join(root, file)
                if self.skip_hidden.get() and self.is_hidden(file_path):
                    continue
                if self.file_type_filter.get() != "All Files" and not file.endswith(self.file_type_filter.get()):
                    continue
                matched_files.append(file_path)

        self.progress_label.config(text=f"{len(matched_files)} Files Found")
        for old_path in matched_files:
            file = os.path.basename(old_path)
            root = os.path.dirname(old_path)
            name, ext = os.path.splitext(file)
            new_name = name

            for ch in self.remove_chars.get():
                new_name = new_name.replace(ch, self.replace_with.get())

            words = [w.strip() for w in self.word_remove.get().split(",") if w.strip()]
            replace_with = self.word_replace.get()
            for word in words:
                pattern = re.compile(rf'\b{re.escape(word)}\b', flags=re.IGNORECASE)
                new_name = pattern.sub(replace_with, new_name)


            if self.auto_cleanup.get():
                new_name = re.sub(r'[\s\-_.]{2,}', ' ', new_name).strip()

            if self.common_name.get():
                new_name = self.common_name.get()

            new_name = self.apply_case(new_name)

            if self.add_serial.get():
                serial = str(counter)
                counter += 1
                new_name = f"{serial} {new_name}" if self.serial_position.get() == "Before" else f"{new_name} {serial}"

            final_name = f"{new_name}{ext}"
            if os.path.exists(os.path.join(root, final_name)) and final_name != file and self.conflict_resolve.get():
                final_name = f"{new_name}${ext}"

            self.original_names.append(old_path)
            self.renamed_names.append(os.path.join(root, final_name))
            tag = "changed" if file != final_name else "unchanged"
            self.tree.insert('', 'end', values=(file, final_name), tags=(tag,))


    def rename_files(self):
        if not self.original_names:
            messagebox.showwarning("Warning", "Please preview the changes first.")
            return
        self.undo_data = list(zip(self.renamed_names, self.original_names))
        total = len(self.original_names)
        start_time = time.time()

        for i, (old, new) in enumerate(zip(self.original_names, self.renamed_names)):
            new_dir = os.path.dirname(new)
            if self.save_in_folder.get():
                base_dir = os.path.join(self.folder_path.get(), "RenamedFiles")
                rel_path = os.path.relpath(new_dir, self.folder_path.get())
                target_dir = os.path.join(base_dir, rel_path)
                os.makedirs(target_dir, exist_ok=True)
                new = os.path.join(target_dir, os.path.basename(new))

            os.rename(old, new)
            percent = ((i + 1) / total) * 100
            elapsed = time.time() - start_time
            eta = (elapsed / (i + 1)) * (total - i - 1)
            self.progress['value'] = percent
            self.progress_label.config(text=f"{int(percent)}% | ETA: {int(eta)}s")
            self.root.update_idletasks()

        total_time = int(time.time() - start_time)
        # Count how many files were actually renamed (name changed)
        actual_renamed = sum(
            1 for old, new in zip(self.original_names, self.renamed_names)
            if os.path.basename(old) != os.path.basename(new))

        self.rename_count_label.config(
            text=f"{actual_renamed} files renamed out of {total} files.")
        self.progress_label.config(text=f"100% Completed in {total_time}s")
        self.undo_btn.config(state="normal")
        messagebox.showinfo("Success!", f"{actual_renamed} files renamed in {total_time} seconds.")
        self.preview_renames()

    def undo_last_rename(self):
        if not self.undo_data:
            messagebox.showinfo("Undo", "Nothing to undo.")
            return
        for old, new in self.undo_data:
            if os.path.exists(old):
                os.rename(old, new)
        self.undo_data = None
        self.undo_btn.config(state="disabled")
        self.status_label.config(text="Undo complete.")
        self.rename_count_label.config(text="")
        messagebox.showinfo("Undo", "Last rename operation undone.")
        self.preview_renames()

    def reset_all_fields(self):
        # Clear all input fields and selections
        self.folder_path.set("")
        self.remove_chars.set("")
        self.replace_with.set("")
        self.word_remove.set("")
        self.word_replace.set("")
        self.common_name.set("")
        self.start_number.set(1)
        self.serial_position.set("After")
        self.file_type_filter.set("All Files")
        self.case_option.set("No Change")
        self.include_subfolders.set(False)
        self.save_in_folder.set(False)
        self.auto_cleanup.set(False)
        self.add_serial.set(False)
        self.conflict_resolve.set(True)
        self.skip_hidden.set(True)
        self.progress['value'] = 0


        # Update any custom checkbox visuals (if you're using Unicode labels)
        try:
            self.include_checkbox.config(text="⬜ Include Subfolders")
            self.save_checkbox.config(text="⬜ Save in Folder")
        except: pass

        self.tree.delete(*self.tree.get_children())
        self.progress_label.config(text="")
        self.rename_count_label.config(text="")
        self.status_label.config(text="")
        self.undo_btn.config(state="disabled")
        self.update_rename_button_state()


if __name__ == '__main__':
    root = tk.Tk()
    root.iconbitmap("BatchRenamer.ico")
    app = FileRenamerApp(root)
    root.mainloop()


