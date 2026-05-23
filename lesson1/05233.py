import random #內建的module,package

# 隨機產生 1~100 的答案
answer = random.randint(1, 100)
print(answer)

guess_count = 0

print("=== 猜數字遊戲 ===")
print("我已經想好一個 1~100 的數字，來猜猜看！")

while True:
    try:
        guess = int(input("請輸入你的猜測："))
        guess_count += 1

        if guess < answer:
            print("太小了！")
        elif guess > answer:
            print("太大了！")
        else:
            print(f"恭喜猜對！答案是 {answer}")
            print(f"你總共猜了 {guess_count} 次")
            break

    except ValueError:
        print("請輸入有效的整數！")