import tkinter as tk
from tkinter import messagebox, scrolledtext
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
import os

# Load pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# File to store notes
NOTES_FILE = 'notes.json'

# Load or create notes
if os.path.exists(NOTES_FILE):
    with open(NOTES_FILE, 'r') as f:
        notes = json.load(f)
else:
    notes = []

def save_notes():
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f)

def add_note():
    note = note_text.get("1.0", tk.END).strip()
    if note:
        notes.append(note)
        save_notes()
        messagebox.showinfo("Success", "Note saved!")
        note_text.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Warning", "Note is empty!")

def search_notes():
    query = search_entry.get().strip()
    if not query:
        messagebox.showwarning("Warning", "Search query is empty!")
        return
    if not notes:
        messagebox.showinfo("Info", "No notes available to search.")
        return

    note_embeddings = model.encode(notes)
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, note_embeddings)[0]

    best_idx = similarities.argmax()
    similarity_score = similarities[best_idx]

    if similarity_score < 0.3:
        result_text.config(state='normal')
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "No good matches found.")
        result_text.config(state='disabled')
    else:
        result_text.config(state='normal')
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Best match (score: {similarity_score:.2f}):\n\n{notes[best_idx]}")
        result_text.config(state='disabled')

# Create main window
root = tk.Tk()
root.title("📝 AI-Powered Personal Notes Searcher")
root.geometry("600x550")
root.configure(bg="#2c3e50")

# Fonts and colors
header_font = ("Helvetica", 18, "bold")
label_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")
bg_color = "#34495e"
input_bg = "#ecf0f1"
btn_color = "#27ae60"
btn_hover_color = "#2ecc71"
text_color = "#ecf0f1"

# Header Label
header = tk.Label(root, text="AI-Powered Personal Notes Searcher", font=header_font, bg=bg_color, fg=text_color, pady=10)
header.pack(fill=tk.X)

# Note input section
note_label = tk.Label(root, text="Enter a note:", font=label_font, bg=bg_color, fg=text_color)
note_label.pack(pady=(15, 5))

note_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=6, font=("Arial", 11), bg=input_bg)
note_text.pack(padx=20, fill=tk.X)

add_button = tk.Button(root, text="Add Note", font=button_font, bg=btn_color, fg="white", activebackground=btn_hover_color, command=add_note)
add_button.pack(pady=10, ipadx=10, ipady=5)

# Search section
search_label = tk.Label(root, text="Search your notes:", font=label_font, bg=bg_color, fg=text_color)
search_label.pack(pady=(20, 5))

search_entry = tk.Entry(root, font=("Arial", 12), bg=input_bg)
search_entry.pack(padx=20, fill=tk.X)

search_button = tk.Button(root, text="Search", font=button_font, bg=btn_color, fg="white", activebackground=btn_hover_color, command=search_notes)
search_button.pack(pady=10, ipadx=10, ipady=5)

# Result display area
result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=8, font=("Arial", 12), bg=bg_color, fg=text_color, state='disabled', relief=tk.FLAT)
result_text.pack(padx=20, pady=(10, 20), fill=tk.BOTH, expand=True)

root.mainloop()
