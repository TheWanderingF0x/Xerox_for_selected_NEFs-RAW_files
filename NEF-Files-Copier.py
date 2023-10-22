import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from ttkthemes import ThemedTk
import webbrowser

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.data = []

    def create_widgets(self):
        self.jpg_path = tk.StringVar()
        self.jpg_path.trace("w", self.update_data)
        self.nef_src_path = tk.StringVar()
        self.nef_dst_path = tk.StringVar()

        self.select_files_label = tk.Label(self, text="JPG files path")
        self.select_files_label.pack(side="top")

        self.select_files_frame = tk.Frame(self)
        self.select_files_frame.pack(side="top", pady=5)
        self.select_files_entry = tk.Entry(self.select_files_frame, textvariable=self.jpg_path, width=50)
        self.select_files_entry.pack(side="left")
        self.select_files_button = tk.Button(self.select_files_frame, text="Browse", command=self.select_files)
        self.select_files_button.pack(side="left")

        self.nef_src_label = tk.Label(self, text="NEF source path")
        self.nef_src_label.pack(side="top")

        self.nef_src_frame = tk.Frame(self)
        self.nef_src_frame.pack(side="top", pady=5)
        self.nef_src_entry = tk.Entry(self.nef_src_frame, textvariable=self.nef_src_path, width=50)
        self.nef_src_entry.pack(side="left")
        self.nef_src_button = tk.Button(self.nef_src_frame, text="Browse", command=self.select_nef_src)
        self.nef_src_button.pack(side="left")

        self.nef_dst_label = tk.Label(self, text="NEF destination path")
        self.nef_dst_label.pack(side="top")

        self.nef_dst_frame = tk.Frame(self)
        self.nef_dst_frame.pack(side="top", pady=5)
        self.nef_dst_entry = tk.Entry(self.nef_dst_frame, textvariable=self.nef_dst_path, width=50)
        self.nef_dst_entry.pack(side="left")
        self.nef_dst_button = tk.Button(self.nef_dst_frame, text="Browse", command=self.select_nef_dst)
        self.nef_dst_button.pack(side="left")

        self.start_button = tk.Button(self, text="Start Copy", command=self.copy_files)
        self.start_button.pack(side="top", pady=5)

        self.reset_button = tk.Button(self, text="Reset", command=self.reset_app)
        self.reset_button.pack(side="top", pady=5)

        self.progress = ttk.Progressbar(self, length=400, mode='determinate')
        self.progress.pack(side="top", pady=5)

        self.made_by = tk.Label(self, text="Made by Vulpea Hoinara", cursor="hand2")
        self.made_by.pack(side="top")
        self.made_by.bind("<Button-1>", self.open_instagram)

    def update_data(self, *args):
        path = self.jpg_path.get()
        if os.path.isdir(path):
            self.files = os.listdir(path)
            f = '-'.join(self.files)
            fJPG2NEF = f.replace(".JPG", ".NEF")
            self.data = []
            for line in fJPG2NEF.split('-'):
                first_part = line[:+12]
                self.data.append(first_part)

    def select_files(self):
        self.path = filedialog.askdirectory()
        self.jpg_path.set(self.path)

    def select_nef_src(self):
        self.src = filedialog.askdirectory()
        self.nef_src_path.set(self.src)

    def select_nef_dst(self):
        self.trg = filedialog.askdirectory()
        self.nef_dst_path.set(self.trg)

    def copy_files(self):
        if not self.jpg_path.get() or not self.nef_src_path.get() or not self.nef_dst_path.get():
            messagebox.showerror("Error", "Please provide all paths before starting the copy process.")
            return

        self.progress['value'] = 0
        self.update_idletasks()

        for i, fname in enumerate(self.data):
            try:
                shutil.copy2(os.path.join(self.nef_src_path.get(), fname), self.nef_dst_path.get())
            except FileNotFoundError as e:
                messagebox.showerror("Error", f"File {fname} not found.")
                return

            self.progress['value'] = ((i+1)/len(self.data))*100
            self.update_idletasks()

        messagebox.showinfo("Info", "Copy completed")

    def reset_app(self):
        self.jpg_path.set("")
        self.nef_src_path.set("")
        self.nef_dst_path.set("")
        self.data = []
        self.progress['value'] = 0

    def open_instagram(self, event):
        webbrowser.open_new("https://www.instagram.com/vulpeahoinara")

def main():
    root = ThemedTk(theme="radiance")
    root.geometry('500x400')
    root.title('NEF Files Copier')
    root.iconbitmap('./assets/vh_1x1_512px_transparent_Fa5_icon.ico')
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
