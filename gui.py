from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import *
import os
from animal import Animal, printAni, deleteAni, find
from file import createFile, readFile, json_save, json_load


class BasicFrame(Frame):  # 继承Frame类
    def __init__(self, page_root=None):
        # 调用父类的构造方法，创建一个Frame实例，并把page_root作为其父容器
        Frame.__init__(self, page_root)
        self.root = page_root                 	# 页面

        # 定义4个StringVar变量
        self.id = StringVar()                 	    # 编号
        self.name = StringVar()                 	# 名称
        self.gender = StringVar()             	    # 性别
        self.age = StringVar()               	    # 年龄
        self.breeder = StringVar()                  # 饲养员
        self.aniType = StringVar()                  # 饲养员

        self.weight = StringVar()               	# 体重
        self.length = StringVar()                   # 体长
        self.diet = StringVar()             	    # 饮食
        self.state = StringVar()               	    # 健康状况

        self.pageInit()  # 初始化页面

        if not os.path.exists('animal.txt'):    # 判断数据文件存不存在
            # 提示数据文件不存在
            showinfo('提示', '数据文件animal.txt不存在！')
            exit()  # 然后退出

        self.aniList = readFile('animal.txt')  # 定义一个列表储存动物记录
        self.update_result()  # 更新Scrollbar，显示动物信息表格

    def pageInit(self):
        # 添加标签和输入框
        Label(self, text='名称：').grid(row=0, column=0, pady=10, sticky=E)
        Entry(self, textvariable=self.name).grid(row=0, column=1, pady=10)
        Label(self, text='性别：').grid(row=1, column=0, pady=10, sticky=E)
        Entry(self, textvariable=self.gender).grid(row=1, column=1, pady=10)
        Label(self, text='年龄：').grid(row=2, column=0, pady=10, sticky=E)
        Entry(self, textvariable=self.age).grid(row=2, column=1, pady=10)
        Label(self, text='饲养员：').grid(row=3, column=0, pady=10, sticky=E)
        Entry(self, textvariable=self.breeder).grid(row=3, column=1, pady=10)
        Label(self, text='编号：').grid(row=4, column=0, pady=10, sticky=E)
        Entry(self, textvariable=self.id).grid(row=4, column=1, pady=10)
        Label(self, text='体重：').grid(row=0, column=2, pady=10, sticky=E)
        Entry(self, textvariable=self.weight).grid(row=0, column=3, pady=10)
        Label(self, text='体长：').grid(row=1, column=2, pady=10, sticky=E)
        Entry(self, textvariable=self.length).grid(row=1, column=3, pady=10)
        Label(self, text='饮食：').grid(row=2, column=2, pady=10, sticky=E)
        Entry(self, textvariable=self.diet).grid(row=2, column=3, pady=10)
        Label(self, text='健康状况：').grid(row=3, column=2, pady=10, sticky=E)
        Entry(self, textvariable=self.state).grid(row=3, column=3, pady=10)
        Label(self, text='种类：').grid(row=4, column=2, pady=10, sticky=E)
        Entry(self, textvariable=self.aniType).grid(row=4, column=3, pady=10)

        # 添加 添加、修改、删除按钮
        addBtn = Button(self, text='添加', command=self.add_item)
        addBtn.grid(row=5, column=1, pady=10)
        modifyBtn = Button(self, text='修改', command=self.modify_item)
        modifyBtn.grid(row=5, column=2, pady=10)
        deleteBtn = Button(self, text='删除', command=self.delete_item)
        deleteBtn.grid(row=5, column=3, pady=10)

        # 添加ScrolledText用于显示结果
        self.result_text = ScrolledText(self, height=10)
        self.result_text.grid(row=6, column=1, columnspan=3, pady=10)

    # 添加基本信息的方法
    def add_item(self):
        if self.id.get() in [oneAni.getNum() for oneAni in self.aniList]:
            # 提示已存在
            showinfo('提示', '该编号已存在无法添加')
            return
        # 创建新添加的动物
        newAni = Animal(self.id.get(), self.name.get(), self.gender.get(), self.age.get(), self.breeder.get(),
                        self.weight.get(), self.length.get(), self.diet.get(), self.state.get(), self.aniType.get())
        self.aniList.append(newAni)
        createFile(self.aniList)  # 写入文件存盘
        # 提示添加成功
        showinfo('提示', '添加成功')
        self.update_result()

    # 修改基本信息的方法
    def modify_item(self):
        found = find(self.aniList, self.id.get(), "编号")
        if found != []:                # 如果该编号的记录存在
            self.update_result()
            newAni = Animal(self.id.get(), self.name.get(), self.gender.get(), self.age.get(), self.breeder.get(),
                            self.weight.get(), self.length.get(), self.diet.get(), self.state.get(), self.aniType.get())
            self.aniList[found[0]] = newAni   # 将刚读入的记录赋值给需要修改的动物记录
            self.update_result()
            createFile(self.aniList)  # 写入文件存盘
            # 提示修改成功
            showinfo('提示', '修改成功')
        else:
            showinfo('提示', "该动物不存在，无法修改其信息！")

    # 删除基本信息的方法
    def delete_item(self):
        if deleteAni(self.aniList, self.id.get()):
            # 提示删除成功
            showinfo('提示', '删除成功')
            createFile(self.aniList)  # 写入文件存盘
        else:
            showinfo('提示', '该动物编号=%s不存在，删除失败' % (self.id.get()))
        self.update_result()

    # 更新Scrollbar方法
    def update_result(self):
        self.result_text.delete('1.0', END)   # 清屏

        # 打印动物信息表头
        show = '-'*80 + '\n'    # 显示文本
        show += '编号\t名称\t性别\t年龄\t饲养员\t体重\t体长\t饮食\t健康状况\t种类\n'
        show += printAni(self.aniList)
        self.result_text.insert(END, show)    # 插入文本


class LiveFrame(Frame):  # 继承Frame类
    def __init__(self, page_root=None):
        # 调用父类的构造方法，创建一个Frame实例，并把page_root作为其父容器
        Frame.__init__(self, page_root)
        self.root = page_root                 	# 页面

        # 定义4个StringVar变量
        self.weight = StringVar()               	# 体重
        self.length = StringVar()                   # 体长
        self.diet = StringVar()             	    # 饮食
        self.state = StringVar()               	    # 健康状况

        self.pageInit()  # 初始化页面
        self.aniList = []                           # 定义一个列表储存动物记录
        self.read_aniList()

    def read_aniList(self):
        if not os.path.exists('animal.txt'):    # 判断数据文件存不存在
            # 提示数据文件不存在
            showinfo('提示', '数据文件animal.txt不存在！')
            exit()  # 然后退出

        self.aniList = readFile('animal.txt')  # 定义一个列表储存动物记录

    def pageInit(self):
        # 添加 添加、修改、删除按钮
        addBtn = Button(self, text='求所有动物个数', command=self.count_item)
        addBtn.grid(row=4, column=1, pady=10)

        # 添加ScrolledText用于显示结果
        self.result_text = ScrolledText(self, height=10)
        self.result_text.grid(row=5, column=0, columnspan=3, pady=10)

    # 统计动物的方法
    def count_item(self):
        self.read_aniList()                   # 更新列表
        self.result_text.delete('1.0', END)   # 清屏

        # 打印动物信息表头和动物信息
        show = '-'*80 + '\n'    # 显示文本
        show += '所有动物的个数为：%d\n' % len(self.aniList)  # 统计Animal
        self.result_text.insert(END, show)    # 插入文本


class SearchFrame(Frame):  # 继承Frame类
    def __init__(self, page_root=None):
        # 调用父类的构造方法，创建一个Frame实例，并把page_root作为其父容器
        Frame.__init__(self, page_root)
        self.root = page_root  # 定义内部变量root
        self.search_key = StringVar()               	# 查询关键字
        self.search_value = StringVar()               	# 查询值

        self.pageInit()  # 初始化页面
        self.aniList = []                           # 定义一个列表储存动物记录
        self.read_aniList()

    def read_aniList(self):
        if not os.path.exists('animal.txt'):    # 判断数据文件存不存在
            # 提示数据文件不存在
            showinfo('提示', '数据文件animal.txt不存在！')
            exit()  # 然后退出

        self.aniList = readFile('animal.txt')  # 定义一个列表储存动物记录

    def pageInit(self):
        # 创建一个Frame，将三个按钮放在其中
        self.button_frame = Frame(self)
        self.button_frame.pack(side=TOP, expand=True, fill=BOTH)

        self.search_button = Button(self.button_frame, text='基本信息查询', command=self.searchBasic)
        self.search_button.pack(side=LEFT, expand=True, fill=BOTH)

        self.life_button = Button(self.button_frame, text='生活信息查询', command=self.searchLife)
        self.life_button.pack(side=LEFT, expand=True, fill=BOTH)

        self.count_button = Button(self.button_frame, text='存活个数统计', command=self.countSurvived)
        self.count_button.pack(side=LEFT, expand=True, fill=BOTH)

        # 再创建一个Frame，放查询选项信息
        self.info_frame = Frame(self)
        self.info_frame.pack(side=TOP, expand=True, fill=BOTH)

        # 查询选项
        self.serach_opt = ttk.Combobox(self.info_frame)
        self.serach_opt.pack(side=LEFT, expand=True, fill=BOTH)
        self.serach_opt['value'] = ('编号', '名称', '饲养员')
        self.serach_opt.current(0)  # 默认选项
        # 查询值
        Entry(self.info_frame, textvariable=self.search_value).pack(side=LEFT, expand=True, fill=BOTH)

        # 将ScrolledText放在一个单独的Frame中，和按钮Frame垂直堆叠
        self.result_frame = Frame(self)
        self.result_frame.pack(side=TOP, expand=True, fill=BOTH)

        self.result_text = ScrolledText(self.result_frame)
        self.result_text.pack(side=TOP, expand=True, fill=BOTH)

    # 查询基本信息的代码
    def searchBasic(self):
        self.read_aniList()                   # 更新列表
        show = '查询结果: \n'                 # 显示文本
        search_results = []                   # 查询结果

        # 根据查询选项获取查询结果
        if self.serach_opt.get() == '编号':
            search_results = [oneAni for oneAni in self.aniList if oneAni.getNum() == self.search_value.get()]
        elif self.serach_opt.get() == '名称':
            search_results = [oneAni for oneAni in self.aniList if oneAni.getName() == self.search_value.get()]
        elif self.serach_opt.get() == '饲养员':
            search_results = [oneAni for oneAni in self.aniList if oneAni.getBreeder() == self.search_value.get()]

        # 根据查询结果构造显示文本
        if len(search_results) > 0:
            show += '-'*70 + '\n'                 # 字符串拼接
            show += '编号\t名称\t性别\t饲养员\t种类\n'  # 基本信息表头
            for ani in search_results:
                show += ani.getNum() + '\t'
                show += ani.getName() + '\t'
                show += ani.getGender() + '\t'
                show += ani.getBreeder() + '\t'
                show += ani.getType() + '\n'
            # 将结果插入到ScrolledText中
            self.insert_result(show)
        else:
            # 将结果插入到ScrolledText中
            self.insert_result("未找到结果 %s=%s" % (self.serach_opt.get(), self.search_value.get()))

    # 查询生活信息的代码
    def searchLife(self):
        self.read_aniList()                   # 更新列表
        show = '查询结果: \n'                 # 显示文本
        search_results = []                   # 查询结果

        # 根据查询选项获取查询结果
        if self.serach_opt.get() == '编号':
            search_results = [oneAni for oneAni in self.aniList if oneAni.getNum() == self.search_value.get()]
        elif self.serach_opt.get() == '名称':
            search_results = [oneAni for oneAni in self.aniList if oneAni.getName() == self.search_value.get()]
        elif self.serach_opt.get() == '饲养员':
            search_results = [oneAni for oneAni in self.aniList if oneAni.getBreeder() == self.search_value.get()]

        # 根据查询结果构造显示文本
        if len(search_results) > 0:
            show += '-'*70 + '\n'                 # 字符串拼接
            show += '编号\t年龄\t体重\t体长\t饮食\t健康状况\n'  # 生活信息表头
            for ani in search_results:
                show += ani.getNum() + '\t'       # 除生活信息外，在结果中显示编号
                show += ani.getAge() + '\t'
                show += ani.getWeight() + '\t'
                show += ani.getLength() + '\t'
                show += ani.getDiet() + '\t'
                show += ani.getHealth()
            # 将结果插入到ScrolledText中
            self.insert_result(show)
        else:
            # 将结果插入到ScrolledText中
            self.insert_result("未找到结果 %s=%s" % (self.serach_opt.get(), self.search_value.get()))

    # 统计存活个数的代码
    def countSurvived(self):
        self.read_aniList()                   # 更新列表
        show = '存活个数: \n'                 # 显示文本
        animal_type_set = set([oneAni.getType() for oneAni in self.aniList])                   # 查询动物种类
        for animal_type in animal_type_set:
            live_num = len([oneAni for oneAni in self.aniList if oneAni.getType() == animal_type])  # 查询个数
            show += "%s\t: %d\n" % (animal_type, live_num)                   # 字符串拼接
        # 将结果插入到ScrolledText中
        self.insert_result(show)

    def insert_result(self, text):
        self.result_text.delete('1.0', END)   # 清屏
        self.result_text.insert(END, text)    # 插入文本


class AccountFrame(Frame):  # 继承Frame类
    def __init__(self, user, page_root=None):
        # 调用父类的构造方法，创建一个Frame实例，并把page_root作为其父容器
        Frame.__init__(self, page_root)
        self.root = page_root  # 定义内部变量root
        self.user = user       # 用户名

        # 定义3个StringVar变量
        self.old_p = StringVar()
        self.new_p = StringVar()
        self.new_p2 = StringVar()

        self.pageInit()  # 初始化页面

    def pageInit(self):
        # 创建标签和输入框
        Label(self).grid(row=0, stick=W, pady=10)  # 空标签
        self.lbl_old_password = Label(self, text='请输入原密码: ')
        self.lbl_old_password.grid(row=1, stick=W, pady=10)  # 输入框标签
        self.entry_old_password = Entry(self, textvariable=self.old_p)
        self.entry_old_password.grid(row=1, column=1, stick=E)  # 输入框

        self.lbl_new_password = Label(self, text='请输入新密码: ')
        self.lbl_new_password.grid(row=2, stick=W, pady=10)  # 输入框标签
        self.entry_new_password = Entry(self, textvariable=self.new_p)
        self.entry_new_password.grid(row=2, column=1, stick=E)  # 输入框

        self.lbl_new_password2 = Label(self, text='请再输入一次')
        self.lbl_new_password2.grid(row=3, stick=W, pady=10)  # 输入框标签
        self.entry_new_password2 = Entry(self, textvariable=self.new_p2)
        self.entry_new_password2.grid(row=3, column=1, stick=E)  # 输入框

        # 创建按钮
        self.btn_save = Button(self, text='保存', command=self.save_password)
        self.btn_save.grid(row=4, stick=W, pady=10)

    def save_password(self):
        # 获取输入框中的内容
        old_password = self.entry_old_password.get()
        new_password = self.entry_new_password.get()
        new_password2 = self.entry_new_password2.get()

        # 验证输入的内容是否符合要求
        if not old_password:
            showerror('错误', '请输入原密码')
            return
        if not new_password:
            showerror('错误', '请输入新密码')
            return
        if not new_password2:
            showerror('错误', '请再次输入新密码')
            return
        if new_password != new_password2:
            showerror('错误', '两次输入的密码不一致')
            return

        user_dict = json_load("account.json")  # 读取用户数据文件
        if old_password == user_dict[self.user]:  # 验证原密码是否正确
            user_dict[self.user] = new_password
            json_save(user_dict, "account.json", indent=4)  # 写入新用户数据文件
            # 提示用户密码已成功更改
            showinfo('提示', '密码已成功更改！')
        else:
            showinfo('错误', '原密码不正确！')  # 提示密码错误信息


class MainPage(object):
    def __init__(self, user, page_root=None):
        self.root = page_root  # 定义内部变量root
        self.root.geometry('%dx%d' % (700, 450))  # 设置窗口大小
        self.user = user

        self.pageInit()  # 初始化页面

    def pageInit(self):
        self.basicPage = BasicFrame(self.root)  # 创建不同Frame
        self.livePage = LiveFrame(self.root)
        self.searchPage = SearchFrame(self.root)
        self.accountPage = AccountFrame(self.user, self.root)
        self.basicPage.pack()  # 默认显示数据录入界面

        # 创建菜单栏
        menubar = Menu(self.root)
        # 添加菜单项
        menubar.add_command(label='基本/生活信息维护', command=self.basicData)
        menubar.add_command(label='生活信息统计', command=self.liveData)
        menubar.add_command(label='信息查询/统计', command=self.searchData)
        menubar.add_command(label='账户设置', command=self.accountData)
        self.root['menu'] = menubar  # 设置菜单栏

    def basicData(self):
        # 显示基本信息界面，隐藏其他界面
        self.basicPage.pack()
        self.livePage.pack_forget()
        self.searchPage.pack_forget()
        self.accountPage.pack_forget()

    def liveData(self):
        # 显示生活信息界面，隐藏其他界面
        self.basicPage.pack_forget()
        self.livePage.pack()
        self.searchPage.pack_forget()
        self.accountPage.pack_forget()

    def searchData(self):
        # 显示信息查询/统计界面，隐藏其他界面
        self.basicPage.pack_forget()
        self.livePage.pack_forget()
        self.searchPage.pack()
        self.accountPage.pack_forget()

    def accountData(self):
        # 显示账户设置界面，隐藏其他界面
        self.basicPage.pack_forget()
        self.livePage.pack_forget()
        self.searchPage.pack_forget()
        self.accountPage.pack()


class LoginPage(object):
    def __init__(self, page_root=None):
        self.root = page_root  # 定义内部变量root
        self.root.geometry('%dx%d' % (300, 180))  # 设置窗口大小
        self.username = StringVar()  # 创建StringVar对象，保存用户名
        self.password = StringVar()  # 创建StringVar对象，保存密码
        self.pageInit()  # 初始化页面

    def pageInit(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()  # 显示Frame
        Label(self.page).grid(row=0, stick=W)  # 空白行
        Label(self.page, text='账户: ').grid(row=1, stick=W, pady=10)  # 用户名标签
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)  # 用户名输入框
        Label(self.page, text='密码: ').grid(row=2, stick=W, pady=10)  # 密码标签
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)  # 密码输入框
        Button(self.page, text='登录', command=self.loginCheck).grid(row=3, stick=W, pady=10)  # 登录按钮
        Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=E)  # 退出按钮

    def loginCheck(self):
        if not os.path.exists("account.json"):  # 如果不存在用户数据文件
            showinfo(title='错误', message='找不到用户数据文件[account.json]！')  # 提示错误信息
        user_dict = json_load("account.json")  # 读取用户数据文件

        name = self.username.get()  # 获取输入的用户名
        secret = self.password.get()  # 获取输入的密码
        if name not in user_dict:  # 如果用户名不存在
            showinfo(title='错误', message='用户不存在！')  # 提示错误信息
            return

        if user_dict[name] == secret:  # 如果用户名和密码正确
            self.page.destroy()  # 销毁登陆页面
            MainPage(name, self.root)  # 进入主界面
        else:  # 如果密码错误
            showinfo(title='错误', message='密码错误！')  # 提示错误信息


if __name__ == "__main__":
    root = Tk()  # 创建一个顶级窗口对象，命名为root，用于容纳整个GUI应用程序
    root.title('动物园动物信息管理系统')  # 设置窗口的标题
    LoginPage(root)  # 显示登录界面
    root.mainloop()  # 开启主事件循环
