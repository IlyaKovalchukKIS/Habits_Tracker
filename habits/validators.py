from rest_framework.serializers import ValidationError


class RelatedHabitsValidator:
    def __init__(self, related_habit, award: str, pleasant_habit: str):
        self.related_habit = related_habit
        self.award = award
        self.pleasant_habit = pleasant_habit

    def __call__(self, value: dict):
        related_habit = dict(value).get(self.related_habit)  # связанная привычка
        pleasant_habit = dict(value).get(self.pleasant_habit)  # признак приятной привычки
        award = dict(value).get(self.award)  # вознаграждение

        if related_habit and award:
            raise ValidationError('Нельзя выбрать одновременно вознаграждение и связаную приятную привычку')

        if related_habit:
            if not related_habit.pleasant_habit:
                raise ValidationError('вы выбрали не приятную привычу')

        if pleasant_habit and award:
            raise ValidationError('У приятной привычки не может быть вознагражденния')


class NotNullValidator:
    def __init__(self, related_habit, award, pleasant_habit):
        self.related_habit = related_habit
        self.award = award
        self.pleasant_habit = pleasant_habit

    def __call__(self, value: dict):

        if not self.pleasant_habit:
            if not self.related_habit and not self.award:
                raise ValidationError('укажите вознаграждение либо связанную приятную привычку')


class MaxTimeToCompleteValidator:
    def __init__(self, time_to_complete):
        self.time_to_complete = time_to_complete

    def __call__(self, value: dict):
        time_to_complete = dict(value).get(self.time_to_complete, 0)
        if time_to_complete >= 120:
            raise ValidationError('время выполнения привычки не должно превышать 120 секунд')