import random
dict = {"明太子":"福岡",
         "豚骨ラーメン":"福岡",
         "馬刺し":"熊本",
         "辛子蓮根":"熊本",
         "かぼす":"大分",
         "黒牛":"鹿児島",
         "焼酎":"鹿児島",
         "カステラ":"長崎",
         "五島うどん":"長崎",
         "羊羹":"佐賀",
         "イカ":"佐賀",
         "きゅうり":"宮崎",
         "向日葵":"宮崎",
         "ちんすこう":"沖縄",
         "シークワーサー":"沖縄"
         }

seikai = 0
toitakazu = 0
while True:
    v = list(dict)
    R = random.randint(0,len(v) - 1)
    keys = list(dict.keys())
    valuse = list(dict.values())
    m = keys[R]
    k = valuse[R]
    print("特産品が当てはまる九州の県名を入力してください")
    ans = input(f"{keys[R]}が特産品の県名を答えてください！→")
    if toitakazu == 0 and ans == "exit":
        print("おつ")
        break
    else:
        toitakazu += 1
        if ans == (k):
            print("当たり！")
            del keys[R]
            del valuse[R]
            seikai += 1
        elif ans == "exit":
            if toitakazu == 1:
                toitakazu -= 1
            hensuu = (seikai % toitakazu * 100)
            print(f"正解率は{hensuu}%です！")
            break
        else:
            print("ハズレ...")
       
