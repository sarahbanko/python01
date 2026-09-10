#!/usr/bin/env python3

class Plant:

    class Stats:

        def __init__(self) -> None:
            self._count_show = 0
            self._count_grow = 0
            self._count_age = 0

        def count_show(self) -> None:
            self._count_show += 1

        def count_grow(self) -> None:
            self._count_grow += 1

        def count_age(self) -> None:
            self._count_age += 1

        def show(self) -> None:
            print(
                f"Stats: {self._count_grow} grow, "
                f"{self._count_age} age, "
                f"{self._count_show} show")

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
        self._stats = self.Stats()

    def show(self) -> None:
        print(
            f"{self._name}: {round(self._height, 1)}cm, "
            f"{self._age_days} days old")
        self._stats.count_show()

    def grow(self) -> None:
        self._height += self._growth_rate
        self._stats.count_grow()

    def age(self) -> None:
        self._age_days += 1
        self._stats.count_age()

    def show_stats(self) -> None:
        self._stats.show()

    @staticmethod
    def check_year(days: int) -> bool:
        return days > 365

    @classmethod
    def unknown_plant(cls) -> "Plant":
        return cls("Unkworn plant", 0.0, 0, 0)


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

    class Stats(Plant.Stats):

        def __init__(self) -> None:
            super().__init__()
            self._count_shade = 0

        def count_shade(self) -> None:
            self._count_shade += 1

        def show(self) -> None:
            super().show()
            print(f"{self._count_shade} shade")

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
        self._stats.count_shade()
        print(
            f"Tree {self._name} now produces a shaded of "
            f"{round(self._height, 1)}cm long and "
            f"{round(self._trunk_diam, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self._trunk_diam, 1)}cm")


class Seed(Flower):

    def __init__(
            self,
            name: str,
            height: float,
            age_days: int,
            growth_rate: float,
            color: str) -> None:
        super().__init__(name, height, age_days, growth_rate, color)
        self._seeds = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")

    def age(self) -> None:
        self._age_days += 20
        self._stats.count_age()

    def is_bloom(self) -> None:
        super().is_bloom()
        self._seeds += 42


def display_statistics(plant: Plant) -> None:
    plant.show_stats()


if __name__ == "__main__":

    rose = Flower("Rose", 15.0, 10, 8.0, "red")
    oak = Tree("Oak", 200.0, 365, 0.5, 5.0)
    sunflower = Seed("Sunflower", 80.0, 45, 30.0, "yellow")
    unknown = Plant.unknown_plant()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        f"Is 30 days more than a year? -> "
        f"{Plant.check_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> "
        f"{Plant.check_year(400)}"
    )
    print()

    print("=== Flower")
    rose.show()
    print("[statistics for Rose]")
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.is_bloom()
    rose.show()
    print("[statistics for Rose]")
    display_statistics(rose)
    print()

    print("=== Tree")
    oak.show()
    print("[statistics for Oak]")
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_statistics(oak)
    print()

    print("=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.age()
    sunflower.grow()
    sunflower.is_bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_statistics(sunflower)
    print()

    print("=== Anonymous")
    unknown.show()
    print("[statistics for Unknown plant]")
    display_statistics(unknown)
