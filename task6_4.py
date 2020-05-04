#4)	Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат
class Car:
    def __init__(self, speed, color, name, is_police=bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} старт'
    def stop(self):
        return f'{self.name} стоп'
    def turn_right(self):
        return f'{self.name} повернула направо'
    def turn_left(self):
        return f'{self.name} повернула налево'
    def show_speed(self):
        print(f'Городская машина {self.name} едет со скоросью {self.speed}')


class TownCar(Car):
       def show_speed(self):
        if self.speed > 60:
            return f'Городская машина {self.name} едет слишком быстро. Текущяя скорость {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Рабочая машина {self.name} едет слишком быстро. Текущяя скорость {self.speed}'

class PoliceCar(Car):
    pass


mazda = TownCar(70, 'black', 'Mazda СX-9', False)
porsche = SportCar(100, 'red', 'Porsche 911',  False)
zil = WorkCar (50, 'green', 'ZIL-130', False)
ford = PoliceCar(100, 'white', 'Ford Explorer', True)

print(f'{mazda.turn_right()},\n{porsche.turn_left()},\n{zil.turn_right()},\n{ford.turn_left()}.')
print(f'Когда {mazda.go()}, после {porsche.stop()}')
print(f'{mazda.show_speed()},\n{zil.show_speed()}')
print(zil.is_police)
print(ford.is_police)
print(mazda.name, mazda.speed, mazda.color, mazda.is_police)
print(porsche.name, porsche.speed, porsche.color, porsche.is_police)
print(zil.name, zil.speed, zil.color, zil.is_police)
print(ford.name, ford.speed, ford.color, ford.is_police)