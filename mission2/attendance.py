from collections import defaultdict

DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_POINTS = {
    "monday": 1, "tuesday": 1,
    "wednesday": 3,
    "thursday": 1, "friday": 1,
    "saturday": 2, "sunday": 2
}
BONUS_THRESHOLD = 10
BONUS_POINTS = 10
GRADE_THRESHOLDS = {"GOLD": 50, "SILVER": 30}

user_ids = {}
user_count = 0
names = {}
attendance = defaultdict(lambda: defaultdict(int))
points = defaultdict(int)
grades = {}
wednesday_count = defaultdict(int)
weekend_count = defaultdict(int)

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