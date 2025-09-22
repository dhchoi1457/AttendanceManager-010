from mission2.src.grade import GoldGrade, SilverGrade, NormalGrade


def test_grade_thresholds():
    # Arrange
    gold = GoldGrade()
    silver = SilverGrade()
    normal = NormalGrade()

    # Act
    gold_threshold = gold.threshold
    silver_threshold = silver.threshold
    normal_threshold = normal.threshold

    # Assert
    assert gold_threshold == 50
    assert silver_threshold == 30
    assert normal_threshold == 0