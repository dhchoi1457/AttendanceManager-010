import pytest
from mission2.attendance import User

def test_user_attendance_and_points():
    # Arrange
    user = User(1, "choi")

    # Act
    user.record_attendance("wednesday")
    user.record_attendance("saturday")
    user.record_attendance("monday")

    # Assert
    assert user.attendance["wednesday"] == 1
    assert user.attendance["saturday"] == 1
    assert user.attendance["monday"] == 1
    assert user.points == 6  # 3 + 2 + 1

def test_user_weekend_count():
    # Arrange
    user = User(2, "dohyun")

    # Act
    for _ in range(3):
        user.record_attendance("saturday")
    for _ in range(2):
        user.record_attendance("sunday")

    # Assert
    assert user.count_weekend() == 5

