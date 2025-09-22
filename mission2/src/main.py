from mission2.src.manager import AttendanceManager


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
