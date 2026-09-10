#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self._name = name
        self._height = height
        self._age_days = age_days

    def show(self) -> None:
            print(f"{self._name}: {round(self._height, 1)}cm, "
                f"{self._age_days} days old")

    def set_height(self, value: float) -> None:
        if (value >= 0):
            self._height = value
            print(f"Height updated: {self._height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, value: int) -> None:
        if (value >= 0):
            self._age_days = value
            print(f"Age updated: {self._age_days} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

if __name__ == "__main__":
   rose = Plant("Rose", 15.0, 10)
   print("=== Garden Security System ===")
   print("Plant created:", end=" ")
   rose.show()
   print()

   rose.set_height(25.0)
   rose.set_age(30)
   print()

   rose.set_height(-5.0)
   rose.set_age(-2)
   print()

   print("Current state:", end=" ")
   rose.show()

        