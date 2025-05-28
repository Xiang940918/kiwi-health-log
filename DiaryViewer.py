import tkinter as tk
from PIL import Image, ImageTk
from datetime import date

def viewDiary():
    diary_window = tk.Toplevel()
    diary_window.title("查看日記")
    import os

    files = os.listdir("date")
    dates = [f.replace(".txt", "") for f in files]

    selected_date=tk.StringVar()  
    selected_date.set(dates[0])   

    menu = tk.OptionMenu(diary_window, selected_date, *dates)
    menu.pack(pady=10)

    text_display = tk.Text(diary_window, width=50, height=15)
    text_display.pack(pady=10)

    def load_diary():
        filename = f"date/{selected_date.get()}.txt"
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
        content = lines[:4]
        text_display.delete("1.0", tk.END)
        text_display.insert(tk.END, ''.join(content))
        
    btn = tk.Button(diary_window, text="查看內容", command=load_diary)
    btn.pack()
    

root = tk.Tk()
root.withdraw() 
viewDiary()
root.mainloop()