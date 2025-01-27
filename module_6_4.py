import math
import random

class Figure:
    def __init__(self, color, *sides):
        self.__color = None
        self.filled = False
        self.sides_count = 0
        self.set_color(*color)  # Устанавливаем цвет через сеттер
        self.set_sides(*sides)  # Устанавливаем стороны через сеттер

    # Геттер для получения цвета
    def get_color(self):
        return self.__color

    # Сеттер для изменения цвета, проверяет корректность
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    # Проверка корректности цвета
    def __is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 for x in [r, g, b])

    # Геттер для получения сторон
    def get_sides(self):
        return self.__sides

    # Сеттер для изменения сторон
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    # Проверка корректности сторон
    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(x, int) and x > 0 for x in new_sides)

    # Метод для подсчета периметра фигуры
    def __len__(self):
        return sum(self.__sides)

    # Метод для вычисления площади, должен быть переопределен в дочерних классах
    def get_square(self):
        raise NotImplementedError("This method must be overridden in child classes")


class Circle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides_count = 1
        # Если передана длина окружности, то вычислим радиус
        if sides:
            self.__radius = sides[0] / (2 * math.pi)  # Радиус = длина окружности / (2 * pi)
            self.__sides = [sides[0]]  # Для круга только одна сторона - длина окружности
        else:
            self.__sides = [1]  # Если не передан параметр, то считаем, что длина окружности = 1

    # Переопределенный метод для получения площади круга
    def get_square(self):
        return math.pi * self.__radius**2


class Triangle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides_count = 3
        self.__sides = list(sides)

    # Переопределенный метод для получения площади треугольника
    def get_square(self):
        a, b, c = self.__sides
        s = (a + b + c) / 2  # Полупериметр
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides_count = 12
        # Если передан один параметр для куба, мы заполним все 12 рёбер одинаковыми значениями
        if sides:
            self._Figure__sides = [sides[0]] * 12
        else:
            self._Figure__sides = [1] * 12

    # Переопределенный метод для получения объема куба
    def get_volume(self):
        side = self._Figure__sides[0]
        return side ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())



