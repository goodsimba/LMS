from student import *


# 管理系统类
class Lms(object):

    # 储存学员数据需要的列表
    def __init__(self):
        self.student_list = []

    def bt(self):
        print('学号｜姓名｜性别｜年龄｜联系电话｜身份证号码')

    # 功能检查函数--------------------------------------------------------------
    def inspect(self):
        try:
            print(self.student_list)
        except:
            print('录入功能错误')
        else:
            print('读取学员数据功能测试成功')

    # 系统主页框架--------------------------------------------------------------
    def run(self):
        # 加载学员信息
        self.load_student()

        while True:
            # 显示菜单
            self.show_menu()
            # 输入选项
            menu_num = int(input('\n请输入功能序号：'))
            # 判断功能
            if menu_num == 1:  # 查询
                self.search_student()
            elif menu_num == 2:  # 新增
                self.add_student()
            elif menu_num == 3:  # 遍历
                self.show_student()
            elif menu_num == 0:  # 退出
                self.exit_student()
                break
            elif menu_num == 9:  # 系统检查
                self.inspect()  # 读取信息检测功能
                break

    # print系统菜单--------------------------------------------------------------
    def show_menu(self):  # 系统主页
        print('LMS v1.0'.center(54, '-'))
        print('1、查询学员信息'.center(50, ))
        print('2、新增学员信息'.center(50, ))
        print('3、遍历学员信息'.center(50, ))
        print('0、退出管理系统'.center(50, ))

    # 加载学员信息--------------------------------------------------------------
    def load_student(self):
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            str_data = f.read()
            dick_data = eval(str_data)
            self.student_list = [Student(i['name'], i['id_num'], i['tel'], i['stu_id']) for i in dick_data]
        f.close()

    # 增加功能--------------------------------------------------------------
    def add_student(self):
        global add_sut_id
        id_num = input('请输入身份证号码：')
        # 检查身份证号码位数
        if len(id_num) != 18:
            print('\n***您输入的身份证号码不正确，请重新输入!***\n\n')
            self.add_student()
        else:
            # 检查身份证号码是否已存在
            for i in self.student_list:
                if i.id_num == id_num:
                    print('\n***注意：身份证号存在冲突****\n冲突学员信息：')
                    self.bt()
                    print(i)
                    print('\n已为您返回主菜单\n\n')
                    self.run()
        name = input('请输入学员姓名：')
        tel = input('请输入手机号码：')

        # 调用 student.py模块，生成 学生信息对象，返回给 list
        student = Student(name, id_num, tel)
        self.student_list.append(student)

        # 确认录入信息是否有误：
        for i in self.student_list:
            if i.id_num == id_num:
                self.bt()
                print(i)
                add_sut_id = i.stu_id
                break
        a = input('请检查录入信息\n\n确认无误 Y\n修改录入 r\n返回主菜单 N\n请输入：')
        if a == 'Y' or a == 'y':
            self.save_data()
            print('***学员信息已保存***')
            self.run()
        elif a == 'R' or a == 'r':
            self.del_data(add_sut_id)
            print('请重新录入信息：\n')
            self.add_student()
        elif a == 'N' or a == 'n':
            self.run()

    # 保存数据模块，将学员数据列表，保存的 student.data 文件=---------------
    def save_data(self):
        f = open('student.data', 'w')
        list_data = [i.__dict__ for i in self.student_list]
        str_data = str(list_data)
        print(str_data)
        f.write(str_data)

    # 删除模块 ------------------------------------------
    def del_data(self, value1):
        for i in self.student_list:
            if i.stu_id == value1:
                del i
                break

# _______________________________________________________
#     # 查询功能
#     def search_student(self):  # 1查询功能页面
#         while True:
#             print('1、学号查询')
#             print('2、姓名查询')
#             print('0、退出查询')
#             mo = int(input('请输入查询方式：'))
#             if mo == 1:
#                 self.id_search()
#             elif mo == 2:
#                 self.name_search()
#             elif mo == 0:
#                 self.exit_search()
#                 break
#
#     def student_data(self):  # 启动系统读取全部学员数据文件，存到内存中，如果没有数据文件默认创建空文件，读取后关闭文件；
#         try:
#             f = open('student.data', 'r')
#         except:
#             f = open('student.data', 'w')
#         else:
#             data = f.read()
#             new_list = eval(data)
#             self.student_list = [Student(i['stu_id'], i['name'], i['gender'], i['tel'], i['id_num']) for i in new_list]
#
#     def aa(self):  # 测试学员储存信息函数
#         print(self.student_list)
#
#     # 框架程序入口
#     def run(self):  # 系统主页框架
#         # 欢迎页面
#         print('LMS v1.0'.center(54, '-'))
#         # 加载学员信息
#         # self.load_student()
#
#         while True:
#             # 显示菜单
#             self.show_menu()
#             # 输入选项
#             menu_num = int(input('\n请输入功能序号：'))
#             # 判断功能
#             if menu_num == 1:  # 查询
#                 self.search_student()
#             elif menu_num == 2:  # 新增
#                 self.add_student()
#             elif menu_num == 5:  # 遍历
#                 self.show_student()
#             elif menu_num == 0:  # 退出
#                 # self.exit_student()
#                 self.student_data()
#                 break
#
#     # 系统菜单
#     def show_menu(self):  # 系统主页
#         print('1、查询学员信息'.center(50, ))
#         print('2、新增学员信息'.center(50, ))
#         print('3、遍历学员信息'.center(50, ))
#         print('0、退出管理系统'.center(50, ))
#
#     # 查询功能
#     def search_student(self):  # 1查询功能页面
#         while True:
#             print('1、学号查询')
#             print('2、姓名查询')
#             print('0、退出查询')
#             mo = int(input('请输入查询方式：'))
#             if mo == 1:
#                 self.id_search()
#             elif mo == 2:
#                 self.name_search()
#             elif mo == 0:
#                 self.exit_search()
#                 break
#
#     def id_search(self):  # 1.1学号查询
#         id_student = int(input('请输入查询学员的学号：'))
#         print('学号｜姓名｜性别｜年龄｜联系电话｜身份证号码')
#         for i in self.student_list:
#             if i.id == id_student:
#                 print(i)
#                 break
#         else:
#             print('学号不正确！')
#             self.search_student()
#         num = int(input('1、重新查找\n2、修改学员信息\n3、删除学员信息\n0、返回主菜单'))
#         if num == 1:
#             self.id_search()
#         elif num == 2:
#             self.modify_student()
#         elif num == 3:
#             self.del_student()
#         elif num == 0:
#             self.run()
#
#     def name_search(self):  # 1.2姓名查询
#         name_student = input('请输入查询学员的姓名：')
#         print('学号｜姓名｜性别｜年龄｜联系电话｜身份证号码')
#         for i in self.student_list:
#             if i.name == name_student:
#                 print(i)
#         num = int(input('1、重新查找\n2、修改学员信息\n3、删除学员信息\n0、返回主菜单'))
#         if num == 1:
#             self.name_search()
#         elif num == 2:
#             self.modify_student()
#         elif num == 3:
#             self.del_student()
#         elif num == 0:
#             self.run()
#
#     def exit_modify(self):  # 1.3退出查询
#         self.run()
#
#     def modify_student(self):  # 1.1.1修改信息
#         modify_id = int(input('请输入修改学员学号：'))
#         for i in self.student_list:
#             if i.id == modify_id:
#                 break
#         print('学号｜姓名｜性别｜年龄｜联系电话｜身份证号码')
#         print(i)
#         print('请输入修改信息数字编号：')
#         print('1.姓名；2.性别；3.年龄；4.身份证号码；5.手机号码。')
#         modify_num = int(input('请输入编号：'))
#         new_modify = input('请输入修改内容：')
#         if modify_num == 1:
#             i.id = new_modify
#             print(i)
#         elif modify_num == 2:
#             pass
#         elif modify_num == 3:
#             pass
#         elif modify_num == 4:
#             pass
#         elif modify_num == 5:
#             pass
#
#     def del_student(self):  # 删除学员信息
#         del_id = input('请输入删除学员的学号：')
#         print('学号｜姓名｜性别｜年龄｜联系电话｜身份证号码')
#         for i in self.student_list:
#             if i.id == del_id:
#                 print(i)
#                 break
#         else:
#             print('您输入的学号有误！')
#
#         x = input('输入Y确认删除，输入N返回主菜单')
#         if x == 'Y' or 'y':
#             self.student_list.remove(i)
#             print('学员已删除！')
#         elif x == 'N' or 'n':
#             print('已取消！')
#
#
#
#     # 数据刷新模块
#     def save_data(self):
#         new_list = [i.__dict__ for i in self.student_list]
#         f = open('student.data', 'w')
#         f.write(str(new_list))
#         f.close()
#
#     # 修改功能
#     # 查询功能
#     # 退出功能
#
#
# if __name__ == '__main__':
#     ams = Lms()
#     ams.aa()
