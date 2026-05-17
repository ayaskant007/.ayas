from reader import apply_comic_effect, save_ayas, load_ayas
import tkinter as tk
from tkinter import filedialog, messagebox, font
import os
from PIL import Image, ImageTk
import customtkinter


class AyasApp:
    def __init__(self, wnd):
        self.wnd = wnd
        self.wnd.title("AYAS Image Studio")
        self.wnd.geometry("1920x1080")
        self.wnd.configure(bg='black')

        self.side_pane_z = tk.Frame(self.wnd, bg="#1e1e1e", width=250)
        self.side_pane_z.pack(side="left", fill="y")
        self.side_pane_z.pack_propagate(False)

        self.main_zone_q = tk.Frame(self.wnd, bg="black")
        self.main_zone_q.pack(side="right", fill="both", expand=True)
        self.main_zone_q.grid_rowconfigure(0, weight=1)
        self.main_zone_q.grid_columnconfigure(0, weight=1)

        self.hdr_font_k = font.Font(family="Segoe UI", size=20, weight="bold")
        self.lbl_title_m = tk.Label(self.side_pane_z, text=".ayas Studio", font=self.hdr_font_k, bg="#1e1e1e", fg="white")
        self.lbl_title_m.pack(pady=40)

        self.nav_font_p = font.Font(family="Segoe UI", size=14)

        self.btn_conv_x = customtkinter.CTkButton(
            self.side_pane_z,
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
        self.btn_conv_x.pack(fill="x", pady=5, padx=10, ipady=10)

        self.btn_view_y = customtkinter.CTkButton(
            self.side_pane_z,
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
        self.btn_view_y.pack(fill="x", pady=5, padx=10, ipady=10)

        self.pg_conv_a = tk.Frame(self.main_zone_q, bg="black")
        self.pg_view_b = tk.Frame(self.main_zone_q, bg="black")

        for frame in (self.pg_conv_a, self.pg_view_b):
            frame.grid(row=0, column=0, sticky="nsew")

        self.build_converter_page()
        self.build_viewer_page()
        self.show_converter_page()

    def build_converter_page(self):
        heading_conv = tk.Label(self.pg_conv_a, text="Convert Image to .ayas", font=("Segoe UI", 28), bg="black", fg="white")
        heading_conv.pack(pady=(100, 30))

        conv_btn = customtkinter.CTkButton(
            self.pg_conv_a,
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
        conv_btn.pack(pady=10)

    def build_viewer_page(self):
        heading_view = tk.Label(self.pg_view_b, text="Open .ayas File", font=("Segoe UI", 28), bg="black", fg="white")
        heading_view.pack(pady=(50, 20))
        select_btn = customtkinter.CTkButton(
            self.pg_view_b,
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
        select_btn.pack(pady=10)

        self.view_canvas = tk.Canvas(self.pg_view_b, width=700, height=500, bg="#222222", highlightthickness=0)
        self.view_canvas.pack(pady=30)

    def show_converter_page(self):
        self.pg_conv_a.tkraise()

    def show_viewer_page(self):
        self.pg_view_b.tkraise()

    def convert(self):
        file_choice_x = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_choice_x:
            try:
                result_img_u = apply_comic_effect(file_choice_x)
                save_path_r = os.path.splitext(file_choice_x)[0] + ".ayas"
                save_ayas(result_img_u, save_path_r)
                messagebox.showinfo("Done!", f"Saved as:\n{save_path_r}")
            except Exception as err_v:
                messagebox.showerror("Error", f"Failed to convert: {err_v}")

    def view(self):
        file_choice_y = filedialog.askopenfilename(filetypes=[("Ayas Files", "*.ayas")])
        if file_choice_y:
            try:
                arr_img_s = load_ayas(file_choice_y)
                pil_img_t = Image.fromarray(arr_img_s)
                pil_img_t.thumbnail((600, 600))
                self.tk_img = ImageTk.PhotoImage(pil_img_t)
                self.view_canvas.delete("all")
                self.view_canvas.create_image(350, 250, image=self.tk_img)
            except Exception as err_w:
                messagebox.showerror("Error", f"Failed to load: {err_w}")


if __name__ == "__main__":
    wnd_main = tk.Tk()
    app = AyasApp(wnd_main)
    wnd_main.mainloop()
