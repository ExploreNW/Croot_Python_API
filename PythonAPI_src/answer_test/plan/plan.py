import re, os

# 打开文件
file_line = """

"""
# 添加excel中的筛选字段
list_tt = []
pat=re.compile(r'[\u4e00-\u9fa5]+')
result=pat.findall(file_line)
for item in result:
    if item not in list_tt:
        list_tt.append(item)

# 判断文件是否已经存在
if os.path.exists("excel_tt.txt"):
    os.remove("excel_tt.txt")

# 保存进文件中
for i in list_tt:
    with open("56-65plan1woman.txt","a")as f:
        f.write(i)
        f.write("\n")

print("list_tt :保存成功")
