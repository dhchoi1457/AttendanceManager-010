from mission2.src.grade import GradeFactory
from mission2.src.user import User

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

    def assign_grades(self):
        for user in self.users.values():
            user.grade = GradeFactory.create(
                user.points,
                user.count_wednesday(),
                user.count_weekend()
            )

    def get_user(self, name):
        return self.users.get(name)
