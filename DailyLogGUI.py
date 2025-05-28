import os

os.makedirs("date", exist_ok=True)

import tkinter as tk
from PIL import Image, ImageTk
from datetime import date

def logToday():
    today = date.today()

    diary_file = f"date/{today}.txt"

    if os.path.exists(diary_file):
        with open(f"date/{today}.txt", "r", encoding="utf-8")as f:
            lines = f.readlines()
            print(lines)
            water=int(float(lines[0].split(":")[1].split()[0]))
            steps=int(float(lines[1].split(":")[1].split()[0]))
            exercise_result=str((lines[2].split()[0]))
            diary=diary = lines[3].split(":", 1)[1].strip()
            w=int(float(lines[4].split("=")[1].split()[0]))
            s=int(float(lines[5].split("=")[1].split()[0]))
            e=int(float(lines[6].split("=")[1].split()[0]))
            bugs_today=int(float(lines[7].split("=")[1].split()[0]))
    else:
        w=0
        s=0
        e=0
        bugs_today=0
        water = 0
        steps = 0
        exercise_result = "尚未紀錄"
        diary = "尚未紀錄"

    add_bug=bugs_today

    log_window = tk.Toplevel()
    log_window.title(f"{today}今日紀錄")
    tk.Label(log_window, text="Hello").pack()

    label = tk.Label(log_window, text=f"今天是 {today}", font=("微軟正黑體", 14))
    label.pack(pady=10)

    with open("UserInformation/setting.txt", "r", encoding="utf-8")as f:
        lines = f.readlines()
        print(lines)

        water_goal = int(float(lines[1].split("：")[1].split()[0])) #讀取目標水量
        steps_goal = int(float(lines[2].split("：")[1].split()[0])) #讀取目標步數

    label_water = tk.Label(log_window, text="今天喝了多少水呢?", font=("微軟正黑體", 10))
    label_water.pack(pady=5)

    entry_water = tk.Entry(log_window)
    entry_water.pack(pady=5)
    entry_water.insert(0, str(water))
    water = float(entry_water.get())

    def water_log(event=None):
        nonlocal water, add_bug,w
        water = float(entry_water.get())

        if water>=water_goal:
            label_Wover=tk.Label(log_window, text="恭喜達成目標水量!", font=("微軟正黑體", 10))
            label_Wover.pack(pady=5)
            if w==0:
                add_bug+=1
            w=1
        else:
            label_Wlow=tk.Label(log_window, text=f"今日差{water_goal-water}ml就達標了!明天再加油!", font=("微軟正黑體", 10))
            label_Wlow.pack(pady=5)
        
    entry_water.bind("<Return>", water_log)


    label_steps= tk.Label(log_window, text="今天走了多少步呢? ", font=("微軟正黑體", 10))
    label_steps.pack(pady=5)

    entry_steps = tk.Entry(log_window)
    entry_steps.pack(pady=5)
    entry_steps.insert(0, str(steps))
    steps = float(entry_steps.get())

    def steps_log(event=None):
        nonlocal steps,add_bug,s
        steps = float(entry_steps.get())
        if steps>=steps_goal:
            label_Sover=tk.Label(log_window, text="恭喜今日達目標步數!", font=("微軟正黑體", 10))
            label_Sover.pack(pady=5)
            if s==0:
                add_bug+=1
            s=1
        else:
            label_Slow=tk.Label(log_window, text=f"今日差{steps_goal-steps}步就達標了!明天再加油!", font=("微軟正黑體", 10))
            label_Slow.pack(pady=5)

    entry_steps.bind("<Return>", steps_log)


    label_exe= tk.Label(log_window, text="今天有運動嗎？", font=("微軟正黑體", 10))
    label_exe.pack(pady=(5, 60))

    yes_img = Image.open("images/button/yes_button.png").resize((60,60))
    no_img = Image.open("images/button/no_button.png").resize((60, 60))

    yes_photo = ImageTk.PhotoImage(yes_img)
    no_photo = ImageTk.PhotoImage(no_img)

    log_window.yes_photo = yes_photo
    log_window.no_photo = no_photo

    def clicked_yes():
        nonlocal exercise_result,add_bug,e
        exercise_result="有運動"
        label_yes= tk.Label(log_window, text="✅ 今天有運動！", font=("微軟正黑體", 10))
        label_yes.pack(pady=5)
        if e==0:
            add_bug += 2
        e=1

    def clicked_no():
        nonlocal exercise_result
        exercise_result="沒有運動"
        label_no= tk.Label(log_window, text="❌ 今天沒有運動！", font=("微軟正黑體", 10))
        label_no.pack(pady=5)


    btn_yes = tk.Button(log_window, image=yes_photo, command=clicked_yes, borderwidth=0)
    btn_yes.place(x=85, y=225)

    btn_no = tk.Button(log_window, image=no_photo, command=clicked_no, borderwidth=0)
    btn_no.place(x=215, y=225)



    label_diary= tk.Label(log_window, text="寫一段日記記錄今天吧:", font=("微軟正黑體", 10))
    label_diary.pack(pady=5)
    text_diary = tk.Text(log_window, height=3, width=50)
    text_diary.pack(pady=5)
    text_diary.insert("1.0", diary)


    def submit_log():
        nonlocal bugs_today,add_bug,diary

        diary = text_diary.get("1.0", tk.END).strip()
        user_input = text_diary.get("1.0", tk.END).strip()

        if user_input: 
            diary = user_input
        
        from add_bug import add_bugs
        add_bug-=bugs_today
        bugs_total=add_bugs(add_bug)
        diary = text_diary.get("1.0", tk.END).strip()
        bugs_today+=add_bug

        label_bugToday= tk.Label(log_window, text=f"今日獲得{bugs_today}隻蟲!", font=("微軟正黑體", 10))
        label_bugToday.pack(pady=5)
        label_bug= tk.Label(log_window, text=f"目前總共有{bugs_total}隻蟲!", font=("微軟正黑體", 10))
        label_bug.pack(pady=5)

        with open(f"date/{today}.txt", "w", encoding="utf-8") as f:
            f.write(f"今日喝水量:{water} ml\n")
            f.write(f"今日步數:{steps} 步\n")
            f.write(f"{exercise_result} \n")
            f.write(f"今日小記:{diary} \n")
            f.write(f"w={w} \n")
            f.write(f"s={s} \n")
            f.write(f"e={e} \n")
            f.write(f"bugs_today={bugs_today} ")

        label_bye= tk.Label(log_window, text="今日記錄完成!繼續跟你的奇異鳥玩吧!", font=("微軟正黑體", 12))
        label_bye.pack(pady=5)

        

    submit_button = tk.Button(log_window, text="提交紀錄", font=("微軟正黑體", 12), command=submit_log)
    submit_button.pack(pady=5)





    log_window.mainloop()