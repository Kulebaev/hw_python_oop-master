class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, 
                 training_type,
                 duration,
                 distance,
                 speed,
                 calories):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories


    def get_message(self):
        return print(f'Тип тренировки: {self.training_type}; '
                     f'Длительность: {self.duration} ч.; '
                     f'Дистанция: {self.distance} км; '
                     f'Ср. скорость: {self.speed} км/ч; '
                     f'Потрачено ккал: {self.calories}.')


class Training:
    """Базовый класс тренировки."""

    LEN_STEP = None
    M_IN_KM = 1000


    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ):
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        pass

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        #преодолённая_дистанция_за_тренировку / время_тренировки
        pass

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage


class Running(Training):
    """Тренировка: бег."""
    #(18 * средняя_скорость + 1.79) * вес_спортсмена / M_IN_KM * время_тренировки_в_минутах 

    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79 
    pass


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    pass


class Swimming(Training):
    """Тренировка: плавание."""

    #длина_бассейна * count_pool / M_IN_KM / время_тренировки 
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

