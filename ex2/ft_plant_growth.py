#!/usr/bin/env python3

class Plant:
    name: str
    height: float
    age_days: int

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self.age_days = self.age_days + 1

    def plant_growth(self) -> None:
        print("=== Garden Plant Growth ===")
        self.show()
        for day in range(1, 8):
            self.grow()
            self.age()
            print(f"=== Day {day} ===")
            self.show()


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.age_days = 30

    initial_height = rose.height
    rose.plant_growth()
    print(f"Growth this week: {round(rose.height - initial_height, 1)}cm")
