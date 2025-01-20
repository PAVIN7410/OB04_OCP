from abc import ABC, abstractmethod

#Импортируем ABC и abstractmethod из модуля abc, чтобы создать абстрактные классы и методы.

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

    def str(self):
        return "меч"


class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

    def str(self):
        return "лук"


class Fighter:
    def init(self, name):  # Исправлено на init
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon}.")

    def attack_monster(self, monster):
        if self.weapon:
            print(self.weapon.attack())
            print(f"{monster.name} побежден!")
        else:
            print(f"{self.name} не имеет оружия!")

class Monster:
    def init(self, name):  # Исправлено на init
        self.name = name

#Шаг 4: Реализация боя
fighter = Fighter("Боец")
monster = Monster("Монстр")

#Боец с мечом
sword = Sword()
fighter.change_weapon(sword)
fighter.attack_monster(monster)

#Боец с луком
bow = Bow()
fighter.change_weapon(bow)
fighter.attack_monster(monster)

