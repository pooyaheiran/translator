from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import messagebox

def translate_to_fa():
        try:
                get_input = entry_en.get()
                persian = GoogleTranslator(target="fa").translate(get_input)
                output_fa.config(text=persian)

        except Exception as e:
                messagebox.showerror(f"error: {e}")


root = tk.Tk()
root.title("مترجم هر زبانی به فارسی")
root.geometry("600x300")

large_font = "arial 14"

label = tk.Label(root, text="یک متن به زبان دلخواه وارد کنید تا به فارسی ترجمه شود ", font=large_font)
label.pack(pady=10)

entry_en = tk.Entry(root, width="40", font=large_font)
entry_en.pack(pady=10)

translate_button = tk.Button(root,text="ترجمه", command=translate_to_fa, font=large_font)
translate_button.pack(pady=10)

output_fa = tk.Label(root, text="", font=large_font)
output_fa.pack(pady=10)

root.mainloop()