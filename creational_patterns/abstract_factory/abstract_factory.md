<aside>

❓ **이 패턴에 대해 어떤 것인가?**

</aside>

Java 및 기타 언어에서 **추상 팩토리 패턴**은 실제 클래스를 지정할 필요 없이 **관련된/의존적인 객체**를 생성하기 위한 **인터페이스**를 제공한다.

이 패턴의 아이디어는 **비즈니스 로직, 플랫폼 선택 등**에 따라 **객체의 생성을 추상화**하는 것이다.

Python 에서 우리가 사용하는 인터페이스는 단순히 호출 가능한 ‘내장’ 인터페이스이며, 일반적인 상황에서는 Python 에서 클래스가 일급 객체이기 때문에 클래스 자체를 호출 가능한 객체로 사용할 수 있다.

<aside>

📝 **이 예제는 무엇을 하는 것인가?**

</aside>

애완동물의 생성을 **추상화**하며, 선택한 팩토리 (Dog 또는 Cat, 또는 random_animal) 에 따라 이를 수행한다.

이것이 가능한 이유는 Dog/Cat 과 random_animal 이 **공통 인터페이스** (생성을 위한 호출 가능하고 .speak()) 를 준수하기 때문이다.

<aside>

📖 **한 줄 요약**

</aside>

**개별 팩토리 그룹**을 **캡슐화** 하는 방법을 제공한다.


### 코드

---

```python
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
```


### 정리 이미지

---

![abstract_factory_rule](https://github.com/cwadven/design-patterns-with-python/blob/master/creational_patterns/abstract_factory/abstract_factory_rule.png)