import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Reproductor de Videos TEMU.YT")

        self.video_label = tk.Label(root)
        self.video_label.pack()

        self.play_button = tk.Button(root, text="Reproducir", command=self.play_video)
        self.play_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = tk.Button(root, text="Pausar", command=self.pause_video)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.load_button = tk.Button(root, text="Cargar Video", command=self.load_video)
        self.load_button.pack(side=tk.LEFT, padx=10)

        self.video_file = None
        self.is_playing = False

    def load_video(self):
        self.video_file = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg")])
        if self.video_file:
            self.display_image(self.video_file)
        else:
            messagebox.showerror("Error", "No se seleccionó ningún archivo.")

    def display_image(self, image_path):
        image = Image.open(image_path)
        image = image.resize((640, 480), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image)
        self.video_label.config(image=self.photo)

    def play_video(self):
        if self.video_file:
            self.is_playing = True
            self.update_video()
        else:
            messagebox.showerror("Error", "No hay ningún video cargado.")

    def pause_video(self):
        self.is_playing = False

    def update_video(self):
        if self.is_playing:

            self.display_image(self.video_file)
            self.root.after(1000, self.update_video)

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayer(root)
    root.mainloop()
