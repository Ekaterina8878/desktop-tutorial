import random


class Animal:
    def __init__(self, speed):
        self.live = True
        self.sound = None
        self._DEGREE_OF_DANGER = 0
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if self._cords[2] + dz < 0:
            print("It's too deep, i can't dive :(")
            return
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed

    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        if self.sound:
            print(self.sound)


class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True

    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} eggs for you")


class AquaticAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        self._cords[2] -= dz
        # Если Z опускается ниже 0, устанавливаем её в 0
        if self._cords[2] < 0:
            self._cords[2] = 0 #она все равно выводит 24
        self.speed /= 2


class PoisonousAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = "Click-click-click"

    def attack(self):
        if self._DEGREE_OF_DANGER > 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")


# Пример работы программы:
db = Duckbill(10)

# Проверяем атрибуты
print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()  # X: 10 Y: 20 Z: 30

db.dive_in(6)
db.get_cords()  # X: 10 Y: 20 Z: 0

# Откладываем яйца
db.lay_eggs()
