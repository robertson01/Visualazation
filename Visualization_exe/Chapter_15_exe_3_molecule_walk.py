# Измените программу rw_visual.py и замените plt.scatter()
# вызовом plt.plot(). Чтобы смоделировать путь пыльцевого зерна на поверхности водя-ной капли,
# передайте значения rw.x_values и rw.y_values и включите аргумент linewidth.
# Используйте 5000 точек вместо 50 000.

from random import choice
import matplotlib.pyplot as plt

class RandomWalk:
    """Класс для генерирования случайных блужданий"""
    def __init__(self, num_points=5000):
        """Инициализирует атрибуты блуждания"""
        self.num_points = num_points

        # Все блуждания начинаются с точки (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Вычисляет все точки блуждания"""
        # Шаги генерируются до достижения нужной длинны
        while len(self.x_values) < self.num_points:
            # Определение направления и длины перемещения
            x_step = self.get_step()
            y_step = self.get_step()

            # Отклонение нулевых перемещений
            if x_step == 0 and y_step == 0:
                continue

            # Вычисление следующих значений x и y
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        """Определяет расстояние и направление"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance

        return step

while True:
    # Построение случайного блуждания
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Нанесение точек на диаграмму
    plt.style.use('classic')
    fix, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)

    # Выделение первой и последней точек.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
               edgecolors='none', s=100)

    # Удаление осей.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk? (y\\n): ')
    if keep_running == 'n':
        break