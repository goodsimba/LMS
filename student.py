import datetime


# 学生信息模块
class Student(object):
    def __init__(self,  name, id_num, tel, stu_id=0, gender=0, age=0):
        self.stu_id = stu_id
        self.name = name
        self.id_num = id_num
        self.tel = tel
        self.gender = gender
        self.age = age

    # 通过身份证识别性别
    def genders(self):
        if int(self.id_num[16:17]) <= 1:
            i = int(self.id_num[16:17])
        else:
            i = int(self.id_num[16:17]) % 2

        if i == 0:
            self.gender = '女'
        elif i == 1:
            self.gender = '男'

    # 通过身份证识别年龄
    def ages(self):
        new_today = datetime.date.today()
        id_today = datetime.datetime.strptime(self.id_num[6:14], '%Y%m%d').date()
        self.age = new_today.year - id_today.year
        if new_today.month <= id_today.month:
            self.age -= 1
        elif new_today.month == id_today.month and new_today.day < id_today.day:
            self.age -= 1

    # 通过遍历学员信息，生成学号
    def stu_ids(self):
        pass

    def __str__(self):
        self.genders()
        self.ages()
        return f'{self.stu_id},{self.name},{self.gender},{self.age},{self.tel},{self.id_num}'
        # return (f'学员信息\n'
        #         f'姓名：{self.name}\t性别：{self.gender}\t 年龄：{self.age}\n'
        #         f'手机号码：{self.tel}\n'
        #         f'身份证号码：{self.id_num}')


if __name__ == '__main__':
    stu = Student('wang', '230402199305220011', '18310933771')
    print(stu)

