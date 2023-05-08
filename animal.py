class Animal(object):
    # 创建一个动物类
    def __init__(self, num, name, gender, age, breeder, weight, length, diet, health, aniType):
        self.__num = num  # 编号
        self.__name = name  # 名称
        self.__gender = gender  # 性别
        self.__age = age  # 年龄
        self.__breeder = breeder  # 饲养员
        self.__weight = weight  # 体重
        self.__length = length  # 体长
        self.__diet = diet  # 饮食
        self.__health = health  # 健康状况
        self.__type = aniType  # 动物种类


    def getInfo(self):
            info = {}
            info["num"]=self.__num
            info["name"]=self.__name
            info["gender"]=self.__gender
            info["age"]=self.__age
            info["breeder"]=self.__breeder
            info["weight"]=self.__weight
            info["length"]=self.__length
            info["diet"]=self.__diet
            info["health"]=self.__health
            return info

    def getNum(self):
        return self.__num

    def getName(self):
        return self.__name

    def getGender(self):
        return self.__gender

    def getAge(self):
        return self.__age

    def getBreeder(self):
        return self.__breeder

    def getWeight(self):
        return self.__weight

    def getLength(self):
        return self.__length

    def getDiet(self):
        return self.__diet

    def getHealth(self):
        return self.__health

    def getType(self):
        return self.__type


def readAni(aniList,n=20):
    #输入动物数据记录值，编号为零或读满规定条数时停止
    while n>0:
        print("请输入一个动物的详细信息（编号为0时结束输入）:")
        num=input("编号：")           #输入编号
        if num=="0":
            break
        else:
            if find(aniList,num,"编号")!=[]:             #编号相同，不允许插入，确保编号的唯一性
                print("列表中存在相同编号，禁止插入！")
                return len(stu)
        name=input("姓名：")             #输入名字
        gender=input("性别：")           #输入性别
        age=input("年龄：")
        breeder=input("饲养员：")
        weight=input("体重：")
        length=input("体长：")
        diet=input("饮食：")
        health=input("健康：")
        oneAni=Animal(num,name,gender,age,breeder,weight,length,diet,health)
        aniList.append(oneAni)
        print("-"*30)
        n=n-1
    return len(aniList)                   #返回实际读入的记录条数


# 输入动物对象的列表，返回所有动物记录的值
def printAni(aniList):
    print_str = ""
    for ani in aniList:
        print_str += ani.getNum() + '\t'
        print_str += ani.getName() + '\t'
        print_str += ani.getGender() + '\t'
        print_str += ani.getAge() + '\t'
        print_str += ani.getBreeder() + '\t'
        print_str += ani.getWeight() + '\t'
        print_str += ani.getLength() + '\t'
        print_str += ani.getDiet() + '\t'
        print_str += ani.getHealth() + '\t'
        print_str += ani.getType()
        print_str += '\n'
    return print_str


def find(aniList,keyword,condition):
    result=[]
    for ani in range(len(aniList)):
        if condition=="编号" and aniList[ani].getNum()==keyword:
            result.append(ani)
        elif condition=="姓名" and aniList[ani].getName()==keyword:
            result.append(ani)
        elif condition=="性别" and aniList[ani].getGender()==keyword:
            result.append(ani)
        elif condition=="年龄" and aniList[ani].getAge()==keyword:
            result.append(ani)
        elif condition=="饲养员" and aniList[ani].getBreeder()==keyword:
            result.append(ani)
        elif condition=="体重" and aniList[ani].getWeight()==keyword:
            result.append(ani)
        elif condition=="体长" and aniList[ani].getLength()==keyword:
            result.append(ani)
        elif condition=="饮食" and aniList[ani].getDiet()==keyword:
            result.append(ani)
        elif condition=="健康" and aniList[ani].getHealth()==keyword:
            result.append(ani)
    return result


def deleteAni(aniList,num):              # 从列表中删除指定编号的一个元素,返回成功与否
    for ani in aniList:                  # 寻找待删除的元素
        if ani.getNum()==num:            # 如果找到相等元素
            aniList.remove(ani)          # 删除对应的元素
            print("已删除指定编号的动物信息")
            break
    else:                                # 如果找不到待删除的元素
        print("该动物不存在，删除失败！")    # 给出提示信息后返回
        return False
    return True
