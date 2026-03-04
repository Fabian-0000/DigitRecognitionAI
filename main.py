import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageGrab, ImageTk
import ctypes
import matplotlib.pyplot as plt
import numpy as np

import ai

class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("Handwritten Digit Recognition AI")
        self.root.geometry("1000x700")

        # Set up menu bar (like Notepad)
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        self.menu_bar.add_cascade(label="Clear", command=self.clear_canvas)
        self.menu_bar.add_cascade(label="Load", command=self.load_image)
        self.menu_bar.add_cascade(label="Evaluate", command=self.show_result)
        self.menu_bar.add_cascade(label="Exit", command=root.quit)

        # Canvas
        self.canvas = tk.Canvas(root, bg="white", cursor="crosshair", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Drawing variables
        self.last_x = None
        self.last_y = None
        self.loaded_image = None

        # Mouse bindings for drawing
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)

    def start_draw(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        if self.last_x is not None and self.last_y is not None:
            self.canvas.create_line(
                self.last_x, self.last_y, event.x, event.y,
                width=12, fill="#111827", capstyle="round", smooth=True
            )
        self.last_x = event.x
        self.last_y = event.y

    def clear_canvas(self):
        self.canvas.delete("all")

    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
        )
        if file_path:
            img = Image.open(file_path)
            self.loaded_image = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, anchor="nw", image=self.loaded_image)

    def show_result(self):
        # Get the widget coordinates
        x = self.canvas.winfo_rootx()
        y = self.canvas.winfo_rooty()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()

        # Capture canvas as PIL Image
        img = ImageGrab.grab((x, y, x1, y1))

        try:
            prediction = ai.evaluate(img)
            probs = prediction[0]

            digits = np.arange(10)
            predicted_digit = np.argmax(probs)

            plt.figure("Probabilities")
            plt.bar(digits, probs)
            plt.xticks(digits)
            plt.xlabel("Digit")
            plt.ylabel("Probability")
            plt.title(f"Prediction: {predicted_digit}")
            plt.ylim(0, 1)

            plt.show()
        except:
            messagebox.showerror("Error", "Nothing drawn")

if __name__ == "__main__":
    # Make the process DPI aware
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)  # 1 = SYSTEM_AWARE
    except Exception:
        pass

    root = tk.Tk()
    app = UI(root)
    root.mainloop()