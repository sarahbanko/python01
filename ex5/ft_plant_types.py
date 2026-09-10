#!/usr/bin/env python3


class Plant:

    def __init__(
            self,
            name: str,
            height: float,
            age_days: int,
            growth_rate: float) -> None:
        self._name = name
        self._height = height
        self._age_days = age_days
        self._growth_rate = growth_rate

    def show(self) -> None:
        print(
            f"{self._name}: {round(self._height, 1)}cm, "
            f"{self._age_days} days old")

    def grow(self) -> None:
        self._height += self._growth_rate

    def age(self) -> None:
        self._age_days += 1


class Flower(Plant):

    def __init__(
            self,
            name: str,
            height: float,
            age_days: int,
            growth_rate: float,
            color: str) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self._color = color
        self._is_bloom = False

    def is_bloom(self) -> None:
        self._is_bloom = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._is_bloom:
            print("Rose is blooming beautifully!")
        else:
            print("Rose has not bloomed yet")


class Tree(Plant):

    def __init__(
                self,
                name: str,
                height: float,
                age_days: int,
                growth_rate: float,
                trunk_diam: float) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self._trunk_diam = trunk_diam

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shaded of "
            f"{round(self._height, 1)}cm long and "
            f"{round(self._trunk_diam, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self._trunk_diam, 1)}cm")


class Vegetable(Plant):

    def __init__(
            self,
            name: str,
            height: float,
            age_days: int,
            growth_rate: float,
            havest_season: str) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self._havest_season = havest_season
        self._nutritional_value = 0

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._havest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    rose = Flower("Rose", 15.0, 10, 0.8, "red")
    oak = Tree("Oak", 200.0, 365, 0.5, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, 2.1, "Abril")

    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.is_bloom()
    rose.show()
    print()

    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
