import re, os

# 这部分需要将数据库中的数据直接复制粘贴到此处注意内容在""" ：成功：成功"""内存放

with open(os.path.join("1030.txt"))as f:
    file_lines = f.read()
    print(file_lines)

# 非贪婪匹配
pattern = re.compile(r'answerContent":"(.*?)"',re.S)
r_list = pattern.findall(file_lines)

# 制定所有的excel中的字段
excel_list = []
excel_tt = open("excel_tt.txt")
for item in excel_tt:
    pattern = re.compile(r'(.*?)\n', re.S)
    excel_list += pattern.findall(item)

# 定义选择套餐类别并保存相关选择信息到TXT文本中
choice_excel = {
    "1":"方案一",
    "2":"方案二",
    "3":"方案三",
}

# 判断条件是否满足
for answer in r_list:
# 判断女性
    if answer in excel_list and r_list[0] == "女性" and r_list[1] == "45-55岁":
        print(r_list[0],r_list[1],answer)
        choice = input("请选择套餐种类（1，2，3）：")
        if choice in ["1","2","3"]:
            excel_plan = []
            plan = open("45-55plan%dwoman.txt"%int(choice))
            for item in plan:
                pattern = re.compile(r'(.*?)\n', re.S)
                excel_plan += pattern.findall(item)
            msg = r_list[0] + r_list[1] + answer + "\n" + choice_excel[choice] + str(excel_plan)
            num = 1
            while True:
                if os.path.exists("%s-%s-%d.txt"%(r_list[0],r_list[1],num)):
                    num += 1
                else:
                    with open("%s-%s-%d.txt"%(r_list[0],r_list[1],num),"w")as f:
                        f.write(msg)
                        print("数据已经存入文件%s" % "：成功")
                    break
            break
        else:
            print("输入套餐有误，请重新输入")
    elif answer in excel_list and r_list[0] == "女性" and r_list[1] == "56-65岁":
        print(r_list[0],r_list[1],answer)
        choice = input("请选择套餐种类（1，2，3）：")
        if choice in ["1","2","3"]:
            excel_plan = []
            plan = open("56-65plan%dwoman.txt"%int(choice))
            for item in plan:
                pattern = re.compile(r'(.*?)\n', re.S)
                excel_plan += pattern.findall(item)
            msg = r_list[0] + r_list[1] + answer + "\n" + choice_excel[choice] + str(excel_plan)
            num = 1
            while True:
                if os.path.exists("%s-%s-%d.txt"%(r_list[0],r_list[1],num)):
                    num += 1
                else:
                    with open("%s-%s-%d.txt"%(r_list[0],r_list[1],num),"w")as f:
                        f.write(msg)
                        print("数据已经存入文件%s" % "：成功")
                    break
            break
        else:
            print("输入套餐有误，请重新输入")
    elif answer in excel_list and r_list[0] == "女性" and r_list[1] == "66-75岁":
        print(r_list[0],r_list[1],answer)
        choice = input("请选择套餐种类（1，2，3）：")
        if choice in ["1","2","3"]:
            excel_plan = []
            plan = open("66-75plan%dwoman.txt"%int(choice))
            for item in plan:
                pattern = re.compile(r'(.*?)\n', re.S)
                excel_plan += pattern.findall(item)
            msg = r_list[0] + r_list[1] + answer + "\n" + choice_excel[choice] + str(excel_plan)
            num = 1
            while True:
                if os.path.exists("%s-%s-%d.txt"%(r_list[0],r_list[1],num)):
                    num += 1
                else:
                    with open("%s-%s-%d.txt"%(r_list[0],r_list[1],num),"w")as f:
                        f.write(msg)
                        print("数据已经存入文件%s" % "：成功")
                    break
            break
        else:
            print("输入套餐有误，请重新输入")
    elif answer in excel_list and r_list[0] == "女性" and r_list[1] == "75以上":
        print(r_list[0],r_list[1],answer)
        choice = input("请选择套餐种类（1，2，3）：")
        if choice in ["1","2","3"]:
            excel_plan = []
            plan = open("75plan%dwoman.txt"%int(choice))
            for item in plan:
                pattern = re.compile(r'(.*?)\n', re.S)
                excel_plan += pattern.findall(item)
            msg = r_list[0] + r_list[1] + answer + "\n" + choice_excel[choice] + str(excel_plan)
            num = 1
            while True:
                if os.path.exists("%s-%s-%d.txt"%(r_list[0],r_list[1],num)):
                    num += 1
                else:
                    with open("%s-%s-%d.txt"%(r_list[0],r_list[1],num),"w")as f:
                        f.write(msg)
                        print("数据已经存入文件%s" % "：成功")
                    break
            break
        else:
            print("输入套餐有误，请重新输入")
# 判断男性
    elif answer in excel_list and r_list[0] == "男性" and r_list[1] == "45-55岁":
        print(r_list[0],r_list[1],answer)
        choice = input("请选择套餐种类（1，2，3）：")
        if choice in ["1","2","3"]:
            excel_plan = []
            plan = open("45-55plan%dman.txt"%int(choice))
            for item in plan:
                pattern = re.compile(r'(.*?)\n', re.S)
                excel_plan += pattern.findall(item)
            msg = r_list[0] + r_list[1] + answer + "\n" + choice_excel[choice] + str(excel_plan)
            num = 1
            while True:
                if os.path.exists("%s-%s-%d.txt"%(r_list[0],r_list[1],num)):
                    num += 1
                else:
                    with open("%s-%s-%d.txt"%(r_list[0],r_list[1],num),"w")as f:
                        f.write(msg)
                        print("数据已经存入文件%s" % "：成功")
                    break
            break
        else:
            print("输入套餐有误，请重新输入")
    elif answer in excel_list and r_list[0] == "男性" and r_list[1] == "56-65岁":
        print(r_list[0],r_list[1],answer)
        choice = input("请选择套餐种类（1，2，3）：")
        if choice in ["1","2","3"]:
            excel_plan = []
            plan = open("56-65plan%dman.txt"%int(choice))
            for item in plan:
                pattern = re.compile(r'(.*?)\n', re.S)
                excel_plan += pattern.findall(item)
            msg = r_list[0] + r_list[1] + answer + "\n" + choice_excel[choice] + str(excel_plan)
            num = 1
            while True:
                if os.path.exists("%s-%s-%d.txt"%(r_list[0],r_list[1],num)):
                    num += 1
                else:
                    with open("%s-%s-%d.txt"%(r_list[0],r_list[1],num),"w")as f:
                        f.write(msg)
                        print("数据已经存入文件%s" % "：成功")
                    break
            break
        else:
            print("输入套餐有误，请重新输入")
    elif answer in excel_list and r_list[0] == "男性" and r_list[1] == "66-75岁":
        print(r_list[0],r_list[1],answer)
        choice = input("请选择套餐种类（1，2，3）：")
        if choice in ["1","2","3"]:
            excel_plan = []
            plan = open("66-75plan%dman.txt"%int(choice))
            for item in plan:
                pattern = re.compile(r'(.*?)\n', re.S)
                excel_plan += pattern.findall(item)
            msg = r_list[0] + r_list[1] + answer + "\n" + choice_excel[choice] + str(excel_plan)
            num = 1
            while True:
                if os.path.exists("%s-%s-%d.txt"%(r_list[0],r_list[1],num)):
                    num += 1
                else:
                    with open("%s-%s-%d.txt"%(r_list[0],r_list[1],num),"w")as f:
                        f.write(msg)
                        print("数据已经存入文件%s" % "：成功")
                    break
            break
        else:
            print("输入套餐有误，请重新输入")
    elif answer in excel_list and r_list[0] == "男性" and r_list[1] == "75以上":
        print(r_list[0],r_list[1],answer)
        choice = input("请选择套餐种类（1，2，3）：")
        if choice in ["1","2","3"]:
            excel_plan = []
            plan = open("75plan%dman.txt"%int(choice))
            for item in plan:
                pattern = re.compile(r'(.*?)\n', re.S)
                excel_plan += pattern.findall(item)
            msg = r_list[0] + r_list[1] + answer + "\n" + choice_excel[choice] + str(excel_plan)
            num = 1
            while True:
                if os.path.exists("%s-%s-%d.txt"%(r_list[0],r_list[1],num)):
                    num += 1
                else:
                    with open("%s-%s-%d.txt"%(r_list[0],r_list[1],num),"w")as f:
                        f.write(msg)
                        print("数据已经存入文件%s" % "：成功")
                    break
            break
        else:
            print("输入套餐有误，请重新输入")
