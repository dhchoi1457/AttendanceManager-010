import pytest
import io
from contextlib import redirect_stdout
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

def test_grade_assignment_gold():
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

def test_grade_assignment_silver():
    # Arrange
    manager = AttendanceManager()
    for _ in range(10):
        manager.record_attendance("dohyun", "wednesday")

    # Act
    manager.assign_grades()
    user = manager.get_user("dohyun")

    # Assert
    assert user.grade.name == "SILVER"

def test_grade_assignment_normal():
    # Arrange
    manager = AttendanceManager()
    for _ in range(2):
        manager.record_attendance("dohyun", "wednesday")

    # Act
    manager.assign_grades()
    user = manager.get_user("dohyun")

    # Assert
    assert user.grade.name == "NORMAL"
    assert user.grade.is_candidate_for_removal(user) == False


def test_print_removed_results_output():
    # Arrange
    manager = AttendanceManager()

    # 사용자 1: GOLD 등급
    user1 = manager.get_or_create_user("kim")
    for _ in range(10):
        user1.record_attendance("wednesday")
        user1.record_attendance("saturday")

    # 사용자 2: NORMAL 등급, 탈락 후보
    user2 = manager.get_or_create_user("choi")
    user2.record_attendance("monday")

    # 사용자 3: NORMAL 등급, 탈락 아님
    user3 = manager.get_or_create_user("lee")
    user3.record_attendance("saturday")

    # Act
    manager.assign_grades()
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        manager.print_removed_results()
    output = buffer.getvalue()

    # Assert
    assert "NAME : kim, POINT :" in output
    assert "NAME : choi, POINT :" in output
    assert "NAME : lee, POINT :" in output

    assert "Removed player" in output