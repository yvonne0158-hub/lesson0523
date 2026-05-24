import tkinter as tk
from tkinter import messagebox
import random   # 內建 module

# 隨機產生 1~100 答案
answer = random.randint(1, 100)

guess_count = 0


# 按下按鈕後執行
def check_guess():
    global guess_count
    global answer

    try:
        guess = int(entry_guess.get())
        guess_count += 1

        if guess < answer:
            result_label.config(
                text="太小了！",
                fg="orange"
            )

        elif guess > answer:
            result_label.config(
                text="太大了！",
                fg="orange"
            )

        else:
            result_label.config(
                text=f"恭喜猜對！答案是 {answer}",
                fg="green"
            )

            messagebox.showinfo(
                "成功",
                f"恭喜猜對！\n答案：{answer}\n共猜了 {guess_count} 次"
            )

        count_label.config(
            text=f"猜測次數：{guess_count}"
        )

        entry_guess.delete(0, tk.END)

    except ValueError:
        messagebox.showwarning(
            "輸入錯誤",
            "請輸入有效整數！"
        )


# 重新開始
def reset_game():
    global answer
    global guess_count

    answer = random.randint(1, 100)
    guess_count = 0

    count_label.config(
        text="猜測次數：0"
    )

    result_label.config(
        text="請開始猜數字",
        fg="black"
    )

    entry_guess.delete(0, tk.END)


# 建立視窗
window = tk.Tk()
window.title("猜數字遊戲")
window.geometry("400x300")
window.resizable(False, False)
window.configure(bg="#F5F5F5")


# 標題
title = tk.Label(
    window,
    text="🎯 猜數字遊戲",
    font=("微軟正黑體", 20, "bold"),
    bg="#F5F5F5"
)

title.pack(pady=15)


# 說明
info = tk.Label(
    window,
    text="我已經想好 1~100 的數字",
    font=("微軟正黑體", 11),
    bg="#F5F5F5"
)

info.pack()


# 輸入框
entry_guess = tk.Entry(
    window,
    font=("Arial", 16),
    justify="center",
    width=10
)

entry_guess.pack(pady=15)

# Enter 直接送出
entry_guess.bind(
    "<Return>",
    lambda event: check_guess()
)


# 按鈕
btn = tk.Button(
    window,
    text="猜看看",
    font=("微軟正黑體", 12),
    bg="#4CAF50",
    fg="white",
    width=10,
    command=check_guess
)

btn.pack()


# 結果文字
result_label = tk.Label(
    window,
    text="請開始猜數字",
    font=("微軟正黑體", 12),
    bg="#F5F5F5"
)

result_label.pack(pady=15)


# 次數
count_label = tk.Label(
    window,
    text="猜測次數：0",
    font=("微軟正黑體", 11),
    bg="#F5F5F5"
)

count_label.pack()


# 重新開始
reset_btn = tk.Button(
    window,
    text="重新開始",
    font=("微軟正黑體", 10),
    bg="#2196F3",
    fg="white",
    command=reset_game
)

reset_btn.pack(pady=15)


window.mainloop()