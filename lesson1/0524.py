import tkinter as tk
from tkinter import messagebox
import random

# 隨機答案
answer = random.randint(1, 100)
guess_count = 0


# 滑鼠移入效果
def hover_in(event):
    event.widget.config(bg="#5AA9FF")


def hover_out(event):
    event.widget.config(bg="#4C8DFF")


# 猜數字
def check_guess():
    global guess_count
    global answer

    try:
        guess = int(entry_guess.get())
        guess_count += 1

        count_label.config(
            text=f"🎯 猜測次數：{guess_count}"
        )

        # 進度條效果
        bars = min(guess_count, 10)
        progress.config(
            text="🟦" * bars + "⬜" * (10-bars)
        )

        if guess < answer:

            result_label.config(
                text="📉 太小了！",
                fg="#FF9800"
            )

        elif guess > answer:

            result_label.config(
                text="📈 太大了！",
                fg="#FF9800"
            )

        else:

            result_label.config(
                text="🎉 猜對了！",
                fg="#4CAF50"
            )

            messagebox.showinfo(
                "恭喜",
                f"""
🏆 猜對了！

答案：{answer}

總共猜了 {guess_count} 次
"""
            )

        entry_guess.delete(0, tk.END)

    except ValueError:

        messagebox.showwarning(
            "錯誤",
            "請輸入有效整數"
        )


# 重新開始
def reset_game():

    global answer
    global guess_count

    answer = random.randint(1, 100)
    guess_count = 0

    result_label.config(
        text="✨ 新遊戲開始",
        fg="#333333"
    )

    count_label.config(
        text="🎯 猜測次數：0"
    )

    progress.config(
        text="⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜"
    )

    entry_guess.delete(0, tk.END)


# 視窗
window = tk.Tk()
window.title("🎯 猜數字挑戰")
window.geometry("520x500")
window.configure(bg="#DCEEFF")
window.resizable(False, False)


# 外框卡片
card = tk.Frame(
    window,
    bg="white",
    width=450,
    height=420,
    highlightbackground="#BFDFFF",
    highlightthickness=2
)

card.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)


# 標題
title = tk.Label(
    card,
    text="🎯 猜數字挑戰 🎯",
    font=("微軟正黑體",22,"bold"),
    bg="white",
    fg="#2266CC"
)

title.pack(pady=20)


# 說明
info = tk.Label(
    card,
    text="系統已產生 1 ~ 100 的數字",
    font=("微軟正黑體",11),
    bg="white",
    fg="#666666"
)

info.pack()


# 圖示
icon = tk.Label(
    card,
    text="🎲",
    font=("Arial",36),
    bg="white"
)

icon.pack(pady=5)


# 輸入框
entry_guess = tk.Entry(
    card,
    font=("Arial",18),
    width=10,
    justify="center",
    relief="flat",
    bg="#F0F7FF"
)

entry_guess.pack(
    pady=15,
    ipady=8
)

entry_guess.bind(
    "<Return>",
    lambda e: check_guess()
)


# 猜按鈕
guess_btn = tk.Button(
    card,
    text="🚀 猜看看",
    font=("微軟正黑體",12,"bold"),
    bg="#4C8DFF",
    fg="white",
    width=14,
    relief="flat",
    cursor="hand2",
    command=check_guess
)

guess_btn.pack()

guess_btn.bind("<Enter>", hover_in)
guess_btn.bind("<Leave>", hover_out)


# 結果
result_label = tk.Label(
    card,
    text="開始挑戰吧！",
    font=("微軟正黑體",13),
    bg="white",
    fg="#333333"
)

result_label.pack(pady=20)


# 次數
count_label = tk.Label(
    card,
    text="🎯 猜測次數：0",
    font=("微軟正黑體",11),
    bg="white"
)

count_label.pack()


# 進度圖示
progress = tk.Label(
    card,
    text="⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
    font=("Arial",14),
    bg="white"
)

progress.pack(
    pady=15
)


# 重設按鈕
reset_btn = tk.Button(
    card,
    text="🔄 重新開始",
    font=("微軟正黑體",11),
    bg="#FF6666",
    fg="white",
    width=12,
    relief="flat",
    cursor="hand2",
    command=reset_game
)

reset_btn.pack(
    pady=10
)


window.mainloop()