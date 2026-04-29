# 父类：基础课程类
class Course:
    def __init__(self, course_type, subject, total_hours, lesson_length):
        self.course_type = course_type      # 一对一 / 班课
        self.subject = subject              # 科目：英语/数学/计算机
        self.total_hours = total_hours      # 总课时（小时）
        self.lesson_length = lesson_length  # 每节课长度

    # 通用功能：显示课程基本信息
    def show_info(self):
        print("\n==================== 课程信息 ====================\n")
        print(f"【课程类型】{self.course_type} | 科目：{self.subject}")
        print(f" 总课时：{self.total_hours}小时 | 每节长：{self.lesson_length}分钟")
        print("\n==================================================\n")

# 子类 1：一对一课程（继承父类）
class OneOnOneCourse(Course):
    def create_lesson(self, note, homework, summary):
        print("\n--- 一对一课堂完成 ---")
        print(f"讲义：{note}")
        print(f"作业：{homework}")
        print(f"课堂总结：{summary}")

# 子类 2：班课（继承父类）
class GroupCourse(Course):
    def class_announcement(self):
        print(f"\n📢 班课公告：本次{self.subject}班课准时开始，共{self.total_hours}小时！")

# 模拟课程运行
# TODO: 接下来的思路是从前端的角度出发，思考本程序（业务逻辑层）是如何
#       和前段交互的，牵扯到哪些具体操作和流程。

def run_course():
    # 创建课程对象
    english_course = OneOnOneCourse("一对一", "英语", 20, 60)
    computer_course = GroupCourse("班课", "计算机", 30, 90)

    # 英语课
    english_course.show_info()
    # english_course.create_lesson(
    #     note="过去式语法讲解",
    #     homework="完成练习册 P10-P12",
    #     summary="学生掌握了一般过去式的用法"
    # )

    # 计算机课
    computer_course.show_info()
    computer_course.class_announcement()

# 运行程序
if __name__ == "__main__":
    print()
    run_course()
    print()