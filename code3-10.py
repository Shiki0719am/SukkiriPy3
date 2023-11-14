print("全ての質問に y または n で答えて下さい")
has_money = input("お金に余裕はありますか？")
if has_money == "y":
    is_hangry = input("お腹がすごくすいていますか？")
    is_drink = input("ビールを飲みたいですか？")
    if is_hangry == "y" and is_drink == "y":
        print("焼肉はいかがですか？")
    elif is_hangry == "y":
        print("カレーはいかがですか？")
    elif is_drink == "y":
        print("焼き鳥はいかがですか？")
    else:
        print("パスタはいかがです？")
    is_snack = input("夜食はいかがですか？")
    if is_snack == "y":
        print("コンビニのチキンはいかがですか？")
else:
    print("家で食べましょう！")