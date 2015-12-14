

class Keep_accounts:

    def register(number, name, money):
        line1 = " "
        opentxt = open("記帳.txt", "r")
        for line in opentxt:
            line1 = line1+line
        opentxt.close()
        dats = line1.split("|")
        x = name + ":" + money
        dats[number] = dats[number] + x
        if number == 0:
            line1 = dats[0] + "\n" + "|" + dats[1] + "|" + dats[2]
        if number == 1:
            line1 = dats[0] + "|" + dats[1] + "\n" + "|" + dats[2]
        if number == 2:
            line1 = dats[0] + "|" + dats[1] + "|" + dats[2]
        R = open("記帳.txt", "w")
        R.write(line1)
        R.close()
        print("\n"+"記帳成功!!\n")

    def Inquire(number):
        line1 = " "
        opentxt = open("記帳.txt", "r")
        for line in opentxt:
            line1 = line1+line
        opentxt.close()
        dats = line1.split("|")
        print(dats[number])
        print("\n"+"查詢成功!!!"+"\n\n")

    def search(Categories):
        i = 0
        total_money = 0
        opentxt = open("記帳.txt", "r")
        for line in opentxt.readlines():
            line = line.strip()
            dats = line.split(":")
            if dats[0].find(Categories) >= 0:
                i = 1
                total_money += int(dats[1])
                print(line)
        if i == 1:
            print("\n總計:", total_money, "元")
            print("\n"+"查詢成功!!!"+"\n\n")
            i = 0
        elif i == 0:
            print("\n"+"查無此項!!!"+"\n\n")

if __name__ == "__main__":
    while(True):
        print("請選擇所需功能")
        choose = input("1.記帳 2.查帳 3.尋找 4.離開\n")

        if str.isdigit(choose):

            if int(choose) == 1:
                print("請選擇記帳類別")
                while(True):
                    number = input("1.食 2.衣 3.行\n")
                    if str.isdigit(number):
                        break
                number = int(number)
                number -= 1
                name = input("\n"+"請輸入名稱\n")
                money = input("請輸入金錢\n")
                Keep_accounts.register(number, name, money)

            elif int(choose) == 2:
                print("請選擇查帳類別")
                while(True):
                    number = input("1.食 2.衣 3.行\n")
                    if str.isdigit(number):
                        break
                number = int(number)
                number -= 1
                Keep_accounts.Inquire(number)

            elif int(choose) == 3:
                Categories = input("請輸入要查詢的關鍵字\n")
                print("\n")
                Keep_accounts.search(Categories)
            elif int(choose) == 4:
                exit()
