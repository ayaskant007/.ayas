from reader import apply_comic_effect, save_ayas, load_ayas
import tkinter as tk
from tkinter import filedialog, messagebox, font
import os
from PIL import Image, ImageTk
import customtkinter


class AyasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AYAS Image Studio")
        self.root.geometry("1920x1080")
        self.root.configure(bg='black')


        # Sidebar Frame (Left)
        self.sidebar = tk.Frame(self.root, bg="#1e1e1e", width=250)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)  # Prevents sidebar from shrinking

        # Main Content Container (Right)
        self.main_area = tk.Frame(self.root, bg="black")
        self.main_area.pack(side="right", fill="both", expand=True)
        # Configure the grid so pages stack directly on top of each other
        self.main_area.grid_rowconfigure(0, weight=1)
        self.main_area.grid_columnconfigure(0, weight=1)



        # App Title in Sidebar
        self.title_font = font.Font(family="Segoe UI", size=20, weight="bold")
        self.sidebar_title = tk.Label(
            self.sidebar, text=".ayas Studio", font=self.title_font, bg="#1e1e1e", fg="white")
        self.sidebar_title.pack(pady=40)

        # Navigation Buttons
        self.nav_font = font.Font(family="Segoe UI", size=14)

        # self.btn_nav_convert = tk.Button(self.sidebar, text="Converter", font=self.nav_font,
        #                                  bg="#333333", fg="white", bd=0, cursor="hand2",
        #                                  command=self.show_converter_page)
        self.btn_nav_convert = customtkinter.CTkButton(
            self.sidebar,
            text="Converter",
            command=self.show_converter_page,
            fg_color="#333333",
            hover_color="#1E1E1E",
            height=50,
            font=("Segoe UI", 20, "bold"),
            border_color='black',
            border_width=3,
            border_spacing=10,
            corner_radius=30,
        )
        self.btn_nav_convert.pack(fill="x", pady=5, padx=10, ipady=10)

        # self.btn_nav_view = tk.Button(self.sidebar, text="Viewer", font=self.nav_font,
        #                               bg="#333333", fg="white", bd=0, cursor="hand2",
        #                               command=self.show_viewer_page)
        self.btn_nav_view = customtkinter.CTkButton(
            self.sidebar,
            text="Viewer",
            command=self.show_viewer_page,
            fg_color="#333333",
            hover_color="#1E1E1E",
            height=50,
            font=("Segoe UI", 20, "bold"),
            border_color='black',
            border_width=3,
            border_spacing=10,
            corner_radius=30,
        )
        self.btn_nav_view.pack(fill="x", pady=5, padx=10, ipady=10)



        # Create the frames for the two pages
        self.page_converter = tk.Frame(self.main_area, bg="black")
        self.page_viewer = tk.Frame(self.main_area, bg="black")

        # Put both pages in the exact same grid spot (row 0, column 0)
        for frame in (self.page_converter, self.page_viewer):
            frame.grid(row=0, column=0, sticky="nsew")

        # Build the contents of each page
        self.build_converter_page()
        self.build_viewer_page()

        # Start the app showing the converter page by default
        self.show_converter_page()



    def build_converter_page(self):
        lbl = tk.Label(self.page_converter, text="Convert Image to .ayas", font=(
            "Segoe UI", 28), bg="black", fg="white")
        lbl.pack(pady=(100, 30))

        btn = customtkinter.CTkButton(
            self.page_converter, 
            text="Select File & Convert", 
            command=self.convert,
            fg_color="#2ecc71",
            hover_color="#21a257",
            width=500, 
            height=100, 
            font=("Segoe UI", 26, "bold"),
            border_color='black',
            border_width=3,
            border_spacing=10,
            corner_radius=35,
        )
        # btn = tk.Button(self.page_converter, text="Select File & Convert", command=self.convert,
        #                 bg="#2ecc71", fg="black", width=25, height=2, font=("Segoe UI", 12, "bold"))
        btn.pack(pady=10)



        # btn1.grid(row=1, column=1)

    def build_viewer_page(self):
        lbl = tk.Label(self.page_viewer, text="Open .ayas File",
                       font=("Segoe UI", 28), bg="black", fg="white")
        lbl.pack(pady=(50, 20))
        btn = customtkinter.CTkButton(
            self.page_viewer,
            text="Select .ayas File",
            command=self.view,
            fg_color="#3498db",
            hover_color="#2a76a9",
            width=500,
            height=100,
            font=("Segoe UI", 26, "bold"),
            border_color='black',
            border_width=3,
            border_spacing=10,
            corner_radius=35,
        )
        # btn = tk.Button(self.page_viewer, text="Select .ayas File", command=self.view,
        #                 bg="#3498db", fg="black", width=25, height=2, font=("Segoe UI", 12, "bold"))
        btn.pack(pady=10)

        # Added explicit height to canvas
        self.canvas = tk.Canvas(
            self.page_viewer, width=700, height=500, bg="#222222", highlightthickness=0)
        self.canvas.pack(pady=30)

    def show_converter_page(self):
        # Bring the converter frame to the top of the stack
        self.page_converter.tkraise()

    def show_viewer_page(self):
        # Bring the viewer frame to the top of the stack
        self.page_viewer.tkraise()



    def convert(self):
        path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if path:
            try:
                styled = apply_comic_effect(path)
                out_path = os.path.splitext(path)[0] + ".ayas"
                save_ayas(styled, out_path)
                messagebox.showinfo("Done!", f"Saved as:\n{out_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to convert: {e}")

    def view(self):
        path = filedialog.askopenfilename(filetypes=[("Ayas Files", "*.ayas")])
        if path:
            try:
                img_array = load_ayas(path)
                img_pil = Image.fromarray(img_array)
                img_pil.thumbnail((600, 600))
                self.tk_img = ImageTk.PhotoImage(img_pil)
                # Clear previous image if any, then draw new one
                self.canvas.delete("all")
                self.canvas.create_image(350, 250, image=self.tk_img)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = AyasApp(root)
    root.mainloop()
