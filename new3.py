class Student:
    def __init__(self, korean, english, math):
        self.korean = korean
        self.english = english
        self.math = math
    def calculate_average(self):
        return (self.korean + self.english + self.math) / 3
def main():
    num_students = int(input("학생 수를 입력 (N): "))

    for i in range(num_students):
        korean = int(input(f"{i + 1}번째 학생의 국어 성적을 입력: "))
        english = int(input(f"{i + 1}번째 학생의 영어 성적을 입력: "))
        math = int(input(f"{i + 1}번째 학생의 수학 성적을 입력: "))

        student = Student(korean, english, math)
        average = student.calculate_average()
        print(f"{i + 1}번째 학생의 평균 점수: {average}")
if __name__ == "__main__":
    main()