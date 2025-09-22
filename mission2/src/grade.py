from abc import ABC, abstractmethod
from mission2.src.user import User


class Grade(ABC):
    @abstractmethod
    def name(self) -> str:  # pragma: no cover
        pass

    @abstractmethod
    def threshold(self) -> int:  # pragma: no cover
        pass


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

    def is_candidate_for_removal(self, user: User):
        return user.count_wednesday() == 0 and user.count_weekend() == 0


class GradeFactory:
    @staticmethod
    def create(points: int) -> Grade:
        total = points
        if total >= GoldGrade().threshold:
            return GoldGrade()
        elif total >= SilverGrade().threshold:
            return SilverGrade()
        else:
            return NormalGrade()
