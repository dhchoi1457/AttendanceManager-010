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


def register_user(name):
    global user_count
    if name not in user_ids:
        user_count += 1
        user_ids[name] = user_count
        names[user_count] = name
    return user_ids[name]


def record_attendance(name, day):
    user_id = register_user(name)
    attendance[user_id][day] += 1
    points[user_id] += DAY_POINTS.get(day, 0)
    if day == "wednesday":
        wednesday_count[user_id] += 1
    elif day in ("saturday", "sunday"):
        weekend_count[user_id] += 1


def print_removed_results():
    for user_id in range(1, user_count + 1):
        name = names[user_id]
        score = points[user_id]
        grade = grades[user_id]
        print(f"NAME : {name}, POINT : {score}, GRADE : {grade}")

    print("\nRemoved player\n==============")
    for user_id in range(1, user_count + 1):
        if grades[user_id] == "NORMAL" and wednesday_count[user_id] == 0 and weekend_count[user_id] == 0:
            print(names[user_id])


def apply_bonus_and_grade():
    for user_id in range(1, user_count + 1):
        if wednesday_count[user_id] >= BONUS_THRESHOLD:
            points[user_id] += BONUS_POINTS
        if weekend_count[user_id] >= BONUS_THRESHOLD:
            points[user_id] += BONUS_POINTS

        score = points[user_id]
        if score >= GRADE_THRESHOLDS["GOLD"]:
            grades[user_id] = "GOLD"
        elif score >= GRADE_THRESHOLDS["SILVER"]:
            grades[user_id] = "SILVER"
        else:
            grades[user_id] = "NORMAL"

def process_attendance_file(filename="../data/attendance_weekday_500.txt"):
    try:
        with open(filename, encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 2:
                    record_attendance(parts[0], parts[1])

        apply_bonus_and_grade()
        print_removed_results()

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


if __name__ == "__main__":
    process_attendance_file()