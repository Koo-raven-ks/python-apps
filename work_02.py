import random
import time
li = []
while True:
    n = random.randint(5,15)
    print("合図（！！！！！）と表示されたらEnter Keyを押してください!")
    time.sleep(n)
    start_time = time.time()
    o = input("！！！！！")
    end_time = time.time()
    a = (end_time - start_time)
    s = round(a,4)
    li.append(s)
    if a < 0.01:
        print(f"{a:.4f}ズルすんなカス")        
    else:
        print(f"{a:.4f}秒です！")
    b = input("もう一度挑戦しますかYES/NO(入力)")
    if b == "NO":
        print(f"最高記録は{min(li)}秒でした")
        break


