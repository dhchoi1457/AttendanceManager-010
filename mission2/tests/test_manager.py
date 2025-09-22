import pytest
from mission2.src.manager import AttendanceManager


def test_user_registration_and_attendance():
    # Arrange
    manager = AttendanceManager()

    # Act
    manager.record_attendance("choi", "wednesday")
    manager.record_attendance("choi", "saturday")
    manager.record_attendance("choi", "monday")

    user = manager.get_user("choi")

    # Assert
    assert user.name == "choi"
    assert user.attendance["wednesday"] == 1
    assert user.attendance["saturday"] == 1
    assert user.attendance["monday"] == 1
    assert user.points == 6  # 3 + 2 + 1

def test_grade_assignment():
    # Arrange
    manager = AttendanceManager()
    for _ in range(10):
        manager.record_attendance("dohyun", "wednesday")
        manager.record_attendance("dohyun", "saturday")
    manager.record_attendance("dohyun", "monday")

    # Act
    manager.assign_grades()
    user = manager.get_user("dohyun")

    # Assert
    assert user.grade.name == "GOLD"
