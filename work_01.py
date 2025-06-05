import random
while True:
    N = random.randint(1,100)
    print("チャンスは5回です！")
    a = input("１〜100までの数字をん入力してください")
    print(a)
    print("入力された文字列",a)
    for i in range(5):
        if N == int(a):
            print("正解です!")
            break
        elif i == 4:
            if N == int(a):
                print("正解です!")
            else:
                print(f"残念...答えは{N}でした！")
            break
        else:
            if N > int(a):
                print(a,"より大きいです！")
            elif N < int(a):
                print(a,"より小さいです！")
            a = input(f"もう一度挑戦しましょう！残り{4 - i}回です！数字を入力してください")
            print("入力された文字列",a)
    b = input("もう一度挑戦しますか？挑戦する場合はyesを辞める場合はnoを入力してください")
    if b == "no":
        break

        