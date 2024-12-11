import tkinter as tk
from tkinter import ttk
import random
import time

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Visualizer")
        self.root.geometry("800x600")

        # UI Elements
        self.algorithm = tk.StringVar()
        self.speed = tk.DoubleVar(value=0.5)
        self.data = []

        self.create_ui()

    def create_ui(self):
        control_frame = tk.Frame(self.root, padx=10, pady=10)
        control_frame.pack(side=tk.TOP, fill=tk.X)

        # Algorithm selection dropdown
        tk.Label(control_frame, text="Algorithm:").pack(side=tk.LEFT, padx=5)
        self.algorithm_menu = ttk.Combobox(control_frame, textvariable=self.algorithm,
                                           values=["Bubble Sort", "Insertion Sort", "Selection Sort"],
                                           state="readonly")
        self.algorithm_menu.pack(side=tk.LEFT, padx=5)
        self.algorithm_menu.current(0)

        # Speed scale
        tk.Label(control_frame, text="Speed:").pack(side=tk.LEFT, padx=5)
        self.speed_scale = ttk.Scale(control_frame, from_=0.1, to=1.0, variable=self.speed,
                                     orient=tk.HORIZONTAL, length=200)
        self.speed_scale.pack(side=tk.LEFT, padx=5)

        # Buttons
        self.generate_button = tk.Button(control_frame, text="Generate Data", command=self.generate_data)
        self.generate_button.pack(side=tk.LEFT, padx=5)

        self.start_button = tk.Button(control_frame, text="Start", command=self.start_sorting)
        self.start_button.pack(side=tk.LEFT, padx=5)

        # Canvas for visualization
        self.canvas = tk.Canvas(self.root, width=780, height=400, bg="white")
        self.canvas.pack(pady=20)

    def generate_data(self):
        self.data = [random.randint(10, 300) for _ in range(50)]
        self.draw_data(self.data, ["blue" for _ in range(len(self.data))])

    def draw_data(self, data, colors):
        self.canvas.delete("all")
        canvas_width = 780
        canvas_height = 400
        bar_width = canvas_width / len(data)

        for i, value in enumerate(data):
            x0 = i * bar_width
            y0 = canvas_height - value
            x1 = (i + 1) * bar_width
            y1 = canvas_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=colors[i])

        self.root.update_idletasks()

    def start_sorting(self):
        algorithm = self.algorithm.get()
        if algorithm == "Bubble Sort":
            self.bubble_sort(self.data)
        elif algorithm == "Insertion Sort":
            self.insertion_sort(self.data)
        elif algorithm == "Selection Sort":
            self.selection_sort(self.data)

    def bubble_sort(self, data):
        for i in range(len(data)):
            for j in range(len(data) - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    self.draw_data(data, ["green" if x == j or x == j + 1 else "blue" for x in range(len(data))])
                    time.sleep(self.speed.get())
        self.draw_data(data, ["green" for _ in range(len(data))])

    def insertion_sort(self, data):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
                self.draw_data(data, ["green" if x == j or x == j + 1 else "blue" for x in range(len(data))])
                time.sleep(self.speed.get())
            data[j + 1] = key
        self.draw_data(data, ["green" for _ in range(len(data))])

    def selection_sort(self, data):
        for i in range(len(data)):
            min_idx = i
            for j in range(i + 1, len(data)):
                if data[j] < data[min_idx]:
                    min_idx = j
                self.draw_data(data, ["green" if x == j or x == min_idx else "blue" for x in range(len(data))])
                time.sleep(self.speed.get())
            data[i], data[min_idx] = data[min_idx], data[i]
            self.draw_data(data, ["green" if x <= i else "blue" for x in range(len(data))])
        self.draw_data(data, ["green" for _ in range(len(data))])

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
