from collections import defaultdict

DAY_POINTS = {
    "monday": 1, "tuesday": 1,
    "wednesday": 3,
    "thursday": 1, "friday": 1,
    "saturday": 2, "sunday": 2
}

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.attendance = defaultdict(int)
        self.points = 0
        self.grade = None

    def record_attendance(self, day):
        self.attendance[day] += 1
        self.points += DAY_POINTS.get(day, 0)

    def count_wednesday(self):
        return self.attendance["wednesday"]

    def count_weekend(self):
        return self.attendance["saturday"] + self.attendance["sunday"]