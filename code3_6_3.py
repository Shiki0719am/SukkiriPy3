isError = False
n = 99

if isError == False and n < 100:
    print("やったね！")
num = int(input("数字を入力＞＞"))
if num%2 == 0:
    print("偶数")
else:
    print("奇数です")

text = input("挨拶文＞＞")
if text == "こんにちは":
    print("ようこそ！")
elif text == "景気は":
    print("ぼちぼちです")
elif text == " さようなら":
    print("お元気で")
else:
    print("どうしましたか？")


# 1,3,5,7,8,10,12
# 4,6,9,11
# 2