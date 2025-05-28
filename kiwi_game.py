import os
import tkinter as tk
from PIL import Image, ImageTk,ImageOps
from add_bug import add_bugs

if not os.path.exists("UserInformation/setting.txt"):
    from FirstTime import setup_goal
    setup_goal()


root=tk.Tk()
root.title("奇異鳥飼養遊戲")

canvas = tk.Canvas(root, width=800, height=600, highlightthickness=0)
canvas.pack()

#background
bg_img=Image.open("images/Background.png").resize((800,600))
bg_photo=ImageTk.PhotoImage(bg_img)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

#kiwi
from PIL import Image, ImageTk

kiwi_img=Image.open(f"images/kiwi_initial.png").resize((472,328))
kiwi_photo=ImageTk.PhotoImage(kiwi_img)
kiwi = canvas.create_image(100, 170, image=kiwi_photo, anchor="nw")

#Turn
def kiwiTurn1(target_x,target_y,after_turn_callback=None):
    global kiwi, image_cache

    if "image_cache" not in globals():
        image_cache = {}

    frames_turn = []
    for i in range(1, 6):
        img = Image.open(f"images/turn/turn{i}.png").resize((472, 328))
        frame = ImageTk.PhotoImage(img)
        frames_turn.append(frame)
        image_cache[f"turn{i}"] = frame

    frame_index = 0

    def animate_turn():
        nonlocal frame_index
        canvas.itemconfig(kiwi, image=frames_turn[frame_index])
        frame_index += 1
        if frame_index < len(frames_turn):
            root.after(150, animate_turn)
        else:
            if after_turn_callback:
                after_turn_callback()

    animate_turn()

def kiwiTurn2(target_x,target_y,after_turn_callback=None):
    global kiwi, image_cache

    if "image_cache" not in globals():
        image_cache = {}

    frames_turn = []
    for i in reversed(range(1, 6)):
        img = Image.open(f"images/turn/turn{i}.png").resize((472, 328))
        frame = ImageTk.PhotoImage(img)
        frames_turn.append(frame)
        image_cache[f"turn{i}"] = frame

    frame_index = 0

    def animate_turn():
        nonlocal frame_index
        canvas.itemconfig(kiwi, image=frames_turn[frame_index])
        frame_index += 1
        if frame_index < len(frames_turn):
            root.after(50, animate_turn)
        else:
            if after_turn_callback:
                after_turn_callback()

    animate_turn()

def kiwiTurn3(target_x,target_y,after_turn_callback=None):
    global kiwi, image_cache

    if "image_cache" not in globals():
        image_cache = {}

    frames_turn = []
    for i in range(1, 6):
        img = Image.open(f"images/turn/turn{i}.png").resize((472, 328))
        flipped_img = ImageOps.mirror(img)
        frame = ImageTk.PhotoImage(flipped_img )
        frames_turn.append(frame)
        image_cache[f"turn{i}"] = frame

    frame_index = 0

    def animate_turn():
        nonlocal frame_index
        canvas.itemconfig(kiwi, image=frames_turn[frame_index])
        frame_index += 1
        if frame_index < len(frames_turn):
            root.after(50, animate_turn)
        else:
            if after_turn_callback:
                after_turn_callback()

    animate_turn()

def kiwiTurn4(target_x,target_y,after_turn_callback=None):
    global kiwi, image_cache

    if "image_cache" not in globals():
        image_cache = {}

    frames_turn = []
    for i in reversed(range(1, 6)):
        img = Image.open(f"images/turn/turn{i}.png").resize((472, 328))
        flipped_img = ImageOps.mirror(img)
        frame = ImageTk.PhotoImage(flipped_img )
        frames_turn.append(frame)
        image_cache[f"turn{i}"] = frame

    frame_index = 0

    def animate_turn():
        nonlocal frame_index
        canvas.itemconfig(kiwi, image=frames_turn[frame_index])
        frame_index += 1
        if frame_index < len(frames_turn):
            root.after(50, animate_turn)
        else:
            if after_turn_callback:
                after_turn_callback()

    animate_turn()

#Run
def kiwirunR(target_x,on_arrival_callback=None):
    global kiwi  

    current_coords = canvas.coords(kiwi)
    x, y = current_coords[0], current_coords[1]

    global image_cache
    if "image_cache" not in globals():
        image_cache = {}
    
    def start_run():
        m1_img=Image.open(f"images/move/move1.png").resize((472,328))
        m1_photo=ImageTk.PhotoImage(m1_img)
        image_cache["m1"]=m1_photo
        canvas.itemconfig(kiwi, image=m1_photo)

        def show_move2():
            m2_img=Image.open(f"images/move/move2.png").resize((472,328))
            m2_photo=ImageTk.PhotoImage(m2_img)
            image_cache["m2"]=m2_photo
            canvas.itemconfig(kiwi, image=m2_photo)
            root.after(25,start_animate)
        
        root.after(50,show_move2)

        def start_animate():
            frames_move = []
            for i in range(3, 8):
                moveR_img = Image.open(f"images/move/move{i}.png").resize((472, 328))
                frames_move.append(ImageTk.PhotoImage(moveR_img))

            frame_index = 0
            step = 5

            def animate_and_move():
                
                nonlocal frame_index
                current_x, current_y = canvas.coords(kiwi)
                canvas.itemconfig(kiwi, image=frames_move[frame_index])
                frame_index = (frame_index + 1) % len(frames_move)

                if abs(target_x-current_x-236) <= step:
                    canvas.coords(kiwi, target_x-236, current_y)
                    if on_arrival_callback:
                        on_arrival_callback()
                    return
                else:
                    dx = step if target_x-236 > current_x else -step
                    canvas.move(kiwi, dx, 0)
                    root.after(50, animate_and_move)

            animate_and_move()
    
    kiwiTurn2(target_x, 0, after_turn_callback=start_run)

def kiwirunL(target_x,on_arrival_callback=None):
    global kiwi  

    current_coords = canvas.coords(kiwi)
    x, y = current_coords[0], current_coords[1]

    global image_cache
    if "image_cache" not in globals():
        image_cache = {}
    
    def start_run():
        m1_img=Image.open(f"images/move/move1.png").resize((472,328))
        flipped_m1_img=ImageOps.mirror(m1_img)
        m1_photo=ImageTk.PhotoImage(flipped_m1_img)
        image_cache["m1"]=m1_photo
        canvas.itemconfig(kiwi, image=m1_photo)

        def show_move2():
            m2_img=Image.open(f"images/move/move2.png").resize((472,328))
            flipped_m2_img=ImageOps.mirror(m2_img)
            m2_photo=ImageTk.PhotoImage(flipped_m2_img)
            image_cache["m2"]=m2_photo
            canvas.itemconfig(kiwi, image=m2_photo)
            root.after(25,start_animate)
        
        root.after(50,show_move2)

        def start_animate():
            frames_move = []
            for i in range(3, 8):
                moveL_img = Image.open(f"images/move/move{i}.png").resize((472, 328))
                flipped_moveL_img=ImageOps.mirror(moveL_img)
                frames_move.append(ImageTk.PhotoImage(flipped_moveL_img))

            frame_index = 0
            step = 5

            def animate_and_move():
                nonlocal frame_index
                current_x, current_y = canvas.coords(kiwi)

                canvas.itemconfig(kiwi, image=frames_move[frame_index])
                frame_index = (frame_index + 1) % len(frames_move)

                if abs(target_x-current_x-236) <= step:
                    canvas.coords(kiwi, target_x-236, current_y)
                    if on_arrival_callback:
                        on_arrival_callback()
                    return

                dx = step if target_x-236 > current_x else -step
                canvas.move(kiwi, dx, 0)
                root.after(50, animate_and_move)

            animate_and_move()

    kiwiTurn4(target_x, 0, after_turn_callback=start_run)

#回復初始
def make_back_to_initial(turn_func):
    def back_to_initial():
        initial_img = Image.open("images/kiwi_initial.png").resize((472, 328))
        initial_photo = ImageTk.PhotoImage(initial_img)
        image_cache["kiwi_initial"] = initial_photo
        canvas.itemconfig(kiwi, image=initial_photo)

        current_x, current_y = canvas.coords(kiwi)
        turn_func(current_x, current_y)
    return back_to_initial

#點擊反應
def point_in_rect(x, y, rect_x, rect_y, width, height):
    return rect_x <= x <= rect_x + width and rect_y <= y <= rect_y + height

def on_click(event):
    current_x = canvas.coords(kiwi)[0]+236
    if (
        point_in_rect(event.x, event.y, 10, 434, 220, 132) or  # btn_log
        point_in_rect(event.x, event.y, 289, 434, 222, 132) or  # btn_feed
        point_in_rect(event.x, event.y, 570, 423, 220, 153)     # btn_diary
    ):
        return
    if event.x > current_x:
        kiwirunR(event.x, on_arrival_callback=make_back_to_initial(kiwiTurn1))
    else:
        kiwirunL(event.x, on_arrival_callback=make_back_to_initial(kiwiTurn3))
    
#eat
def kiwiEatR(after_callback=None, bug=None):
    frames_eat = []
    for i in range(1, 11):
        eatR_img = Image.open(f"images/eat/eat{i}.png").resize((472, 328))
        frames_eat.append(ImageTk.PhotoImage(eatR_img))
        image_cache[f"eatR{i}"] = frames_eat[-1]

    frame_index=0

    def animate_eatR():
        nonlocal frame_index
        canvas.itemconfig(kiwi, image=frames_eat[frame_index])

        if frame_index == 4:
            canvas.delete(bug)

        frame_index += 1
        if frame_index < len(frames_eat):
            root.after(100, animate_eatR)
        else:
            if after_callback:
                after_callback()

    animate_eatR()

def kiwiEatL(after_callback=None,bug=None):
    frames_eat = []
    for i in range(1, 11):
        eatL_img = Image.open(f"images/eat/eat{i}.png").resize((472, 328))
        flipped_eatL_img=ImageOps.mirror(eatL_img)
        frames_eat.append(ImageTk.PhotoImage(flipped_eatL_img))
        image_cache[f"eatL{i}"] = frames_eat[-1]
    frame_index=0
    def animate_eatL():
        nonlocal frame_index
        canvas.itemconfig(kiwi, image=frames_eat[frame_index])

        if frame_index == 4:
            canvas.delete(bug)

        frame_index += 1
        if frame_index < len(frames_eat):
            root.after(100, animate_eatL)
        else:
            if after_callback:
                after_callback()

    animate_eatL()
        

#偵測點擊
canvas.bind("<Button-1>", on_click)

#buttons
dailyLog_img=Image.open("images/button/button_log.png").convert("RGBA").resize((220,132))
diary_img=Image.open("images/button/button_diary.png").convert("RGBA").resize((220,153))
feed_img=Image.open("images/button/button_feed.png").convert("RGBA").resize((222, 132))

dailyLog_photo=ImageTk.PhotoImage(dailyLog_img)
diary_photo=ImageTk.PhotoImage(diary_img)
feed_photo=ImageTk.PhotoImage(feed_img)

def open_log():
    from DailyLogGUI import logToday
    logToday()

def open_diary():
    from DiaryViewer import viewDiary
    viewDiary()

def open_feed():
    def start_feeding():
        try:
            total = add_bugs(-1)
        except:
            print("無法載入蟲的資料")
            return

        if total < 0:
            print("你沒有足夠的蟲可以餵食")
            add_bugs(1)  # 補回
            return

        bug_frames = []
        for i in range(1, 6): 
            img = Image.open(f"images/bug/bug{i}.png").resize((230,160 ))
            bug_frames.append(ImageTk.PhotoImage(img))

        bug_frame_index = 0

        bug_x, bug_y = 350, 320
        bug= canvas.create_image(bug_x, bug_y, image=bug_frames[0], anchor="nw")

        def animate_bug():
            nonlocal bug_frame_index
            canvas.itemconfig(bug, image=bug_frames[bug_frame_index])
            bug_frame_index = (bug_frame_index + 1) % len(bug_frames)
            canvas.after(150, animate_bug)


        animate_bug()

        kiwi_x = canvas.coords(kiwi)[0] 

        def after_eating():
            canvas.delete(bug)
            print(f"餵食完成！剩餘蟲數：{total}")
            make_back_to_initial(kiwiTurn1 if bug_x > kiwi_x else kiwiTurn3)()

        if bug_x > kiwi_x:
            kiwirunR(bug_x, on_arrival_callback=lambda: kiwiEatR(after_callback=after_eating,bug=bug))
        else:
            kiwirunL(bug_x+236, on_arrival_callback=lambda: kiwiEatL(after_callback=after_eating,bug=bug))
    start_feeding()

btn_log = canvas.create_image(120, 500, image=dailyLog_photo)
btn_feed = canvas.create_image(400, 500, image=feed_photo)
btn_diary = canvas.create_image(680, 500, image=diary_photo)

canvas.tag_bind(btn_log, "<Button-1>", lambda e: open_log())
canvas.tag_bind(btn_feed, "<Button-1>", lambda e: open_feed())
canvas.tag_bind(btn_diary, "<Button-1>", lambda e: open_diary())


root.mainloop()