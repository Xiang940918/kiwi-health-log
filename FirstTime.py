import tkinter as tk
import os

def setup_goal():
    root = tk.Tk()
    root.title("首次設定")
    root.geometry("300x200")

    label_w = tk.Label(root, text="請輸入你的體重（公斤）", font=("微軟正黑體", 12))
    label_w.pack(pady=10)

    entry_weight = tk.Entry(root)
    entry_weight.pack(pady=5)

    label_s = tk.Label(root, text="請輸入你的目標步數", font=("微軟正黑體", 12))
    label_s.pack(pady=10)

    entry_steps = tk.Entry(root)
    entry_steps.pack(pady=5)

    def save_goal():
        weight = float(entry_weight.get())

        water_goal = round(weight * 35, 2)

        steps_goal = float(entry_steps.get())

        os.makedirs("UserInformation", exist_ok=True)
        with open("UserInformation/setting.txt", "w", encoding="utf-8") as f:
            f.write(f"體重：{weight} 公斤\n")
            f.write(f"每日建議水量：{water_goal} ml\n")
            f.write(f"每日步數目標：{steps_goal} 步\n")

        label_done = tk.Label(root, text="✅ 設定完成！請重新開啟遊戲", font=("微軟正黑體", 10))
        label_done.pack(pady=10)
        root.after(2000, root.destroy) 

    btn = tk.Button(root, text="儲存設定", command=save_goal, font=("微軟正黑體", 12))
    btn.pack(pady=10)

    root.mainloop()
