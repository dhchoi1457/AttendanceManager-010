from mission2.src.grade import GradeFactory, NormalGrade
from mission2.src.user import User

BONUS_POINTS = 10
BONUS_ATTEND_COUNT_THRESHOLD = 10

class AttendanceManager:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def get_or_create_user(self, name):
        if name not in self.users:
            self.users[name] = User(self.next_id, name)
            self.next_id += 1
        return self.users[name]

    def record_attendance(self, name, day):
        user = self.get_or_create_user(name)
        user.record_attendance(day)

    def add_bonus(self, user:User):
        bonus = 0
        if user.count_wednesday() >= BONUS_ATTEND_COUNT_THRESHOLD:
            bonus += BONUS_POINTS
        if user.count_weekend() >= BONUS_ATTEND_COUNT_THRESHOLD:
            bonus += BONUS_POINTS

        user.points += bonus

    def assign_grades(self):
        for user in self.users.values():
            self.add_bonus(user)
            user.grade = GradeFactory.create(user.points)

    def get_user(self, name):
        return self.users.get(name)

    def print_removed_results(self):
        for name in self.users:
            user = self.users.get(name)
            print(f"NAME : {user.name}, POINT : {user.points}, GRADE : {user.grade.name}")

        print("\nRemoved player\n==============")
        for name in self.users:
            user = self.users.get(name)
            if user.grade.name == "NORMAL":
                if NormalGrade().is_candidate_for_removal(user):
                    print(name)