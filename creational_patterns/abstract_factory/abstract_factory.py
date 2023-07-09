import random
from typing import Type


class Pet:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class Dog(Pet):
    def speak(self) -> None:
        print("Woof!")

    def __str__(self) -> str:
        return f"Dog<{self.name}>"


class Cat(Pet):
    def speak(self) -> None:
        print("Meow!")

    def __str__(self) -> str:
        return f"Cat<{self.name}>"


class PetShop:
    """
    A pet shop
    """
    def __init__(self, animal_factory: Type[Pet]) -> None:
        """
        pet_factory 는 우리의 추상 팩토리 입니다.
        """
        self.pet_factory = animal_factory

    def buy_pet(self, name: str) -> Pet:
        """
        추상 팩토리를 사용하여 애완동물을 생성하고 보여줍니다.
        """
        pet = self.pet_factory(name)
        print(f"Here is your lovely {pet}!")
        return pet


def random_animal(name: str) -> Pet:
    """
    랜덤한 애완동물을 생성합니다.
    """
    return random.choice([Dog, Cat])(name)


def main() -> None:
    cat_shop = PetShop(Cat)
    pet = cat_shop.buy_pet("Lucy")
    pet.speak()

    shop = PetShop(random_animal)
    for name in ["Max", "Jack", "Buddy"]:
        pet = shop.buy_pet(name)
        pet.speak()
        print("=" * 20)


if __name__ == "__main__":
    random.seed(1234)
    main()


"""
Here is your lovely Cat<Lucy>!
Meow!
Here is your lovely Cat<Max>!
Meow!
====================
Here is your lovely Dog<Jack>!
Woof!
====================
Here is your lovely Dog<Buddy>!
Woof!
====================

Process finished with exit code 0
"""