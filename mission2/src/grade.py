from abc import ABC, abstractmethod
from mission2.src.user import User

BONUS_POINTS = 10
BONUS_ATTEND_COUNT_THRESHOLD = 10

class Grade(ABC):
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def threshold(self) -> int:
        pass

    def is_candidate_for_removal(self, user:User) -> bool:
        return False


class GoldGrade(Grade):
    @property
    def name(self):
        return "GOLD"

    @property
    def threshold(self):
        return 50


class SilverGrade(Grade):
    @property
    def name(self):
        return "SILVER"

    @property
    def threshold(self):
        return 30


class NormalGrade(Grade):
    @property
    def name(self):
        return "NORMAL"

    @property
    def threshold(self):
        return 0

    def is_candidate_for_removal(self, user:User):
        return user.count_wednesday() == 0 and user.count_weekend() == 0


class GradeFactory:
    @staticmethod
    def create(points: int, wed_count: int, weekend_count: int) -> Grade:
        bonus = 0
        if wed_count >= BONUS_ATTEND_COUNT_THRESHOLD:
            bonus += BONUS_POINTS
        if weekend_count >= BONUS_ATTEND_COUNT_THRESHOLD:
            bonus += BONUS_POINTS

        total = points + bonus

        if total >= GoldGrade().threshold:
            return GoldGrade()
        elif total >= SilverGrade().threshold:
            return SilverGrade()
        else:
            return NormalGrade()

