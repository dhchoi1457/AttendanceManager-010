from collections import defaultdict

from mission2.src.manager import AttendanceManager

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


def process_attendance_file(filename="../data/attendance_weekday_500.txt"):
    try:

        manager = AttendanceManager()

        with open(filename, encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 2:
                    manager.record_attendance(parts[0], parts[1])

        manager.assign_grades()
        manager.print_removed_results()

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


if __name__ == "__main__":
    process_attendance_file()