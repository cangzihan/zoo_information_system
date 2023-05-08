from animal import*
import json


def createFile(aniList):  # 建立初始的数据文件，返回为空
    with open('animal.txt', 'w', encoding='UTF-8') as file:
        tab = ','
        for oneAni in aniList:  # 将刚才读入的数据一次性写入文件
            s = oneAni.getNum() + tab + oneAni.getName() + tab + \
                oneAni.getGender() + tab + oneAni.getAge() + tab + oneAni.getBreeder() + tab + \
                oneAni.getWeight() + tab + oneAni.getLength() + tab + oneAni.getDiet() + tab + \
                oneAni.getHealth() + tab + oneAni.getType() + '\n'
            file.write(s)
        return


def readFile(file_path):  # 将文件内容读出，输入为数据文件路径，返回数据列表
    aniList = []  # 定义一个列表储存动物记录
    with open(file_path, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            if line != "":
                s = line.replace('\n', '').split(',')
                num, name, gender, age, breeder, weight, length, diet, health, aniType = s[0], s[1], s[2], s[3], s[4],\
                                                                                        s[5], s[6], s[7], s[8], s[9]
                oneAni = Animal(num, name, gender, age, breeder, weight, length, diet, health, aniType)
                aniList.append(oneAni)
        return aniList               # 返回数据列表


# 存储Json文件的函数
def json_save(user_dict, save_path, indent=None):
    with open(save_path, 'w') as f:
        json.dump(user_dict, f, indent=indent)    # 将字典存储到文件中


# 读取Json文件的函数
def json_load(file_path):
    with open(file_path, 'r') as f:
        my_dict = json.load(f)                    # 读取字典
    return my_dict

