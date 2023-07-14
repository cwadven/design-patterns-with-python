https://github.com/faif/python-patterns/blob/master/patterns/creational/factory.py

<aside>

❓ **이 패턴에 대해 어떤 것인가?**

</aside>

팩토리는 객체를 생성하는 다른 객체입니다.

<aside>

📝 **이 예제는 무엇을 하는 것인가?**

</aside>

이 코드는 영어와 그리스어 두 가지 언어로 단어를 지역화하는 방법을 보여줍니다. 

`get_localizer`는 선택된 언어에 따라 로컬라이저를 구성하는 팩토리 함수입니다.

로컬라이저 객체는 지역화된 언어에 따라 다른 클래스의 인스턴스가 될 것입니다. 

그러나, 메인 코드는 `localize` 메소드가 언어에 관계없이 동일한 방식으로 호출될 것이므로, 어떤 로컬라이저가 인스턴스화될지 걱정할 필요가 없습니다.

<aside>

✏️ **어디서 자주 쓰이는가?**

</aside>

팩토리 메소드는 인기 있는 웹 프레임워크인 Django에서 볼 수 있습니다

예를 들어, 다양한 유형의 폼들이 formset_factory를 사용하여 생성됩니다.

<aside>

📖 **한 줄 요약**

</aside>

### 코드

---

```python
from typing import Dict
from typing_extensions import Protocol
from typing import Type

class Localizer(Protocol):
    def localize(self, message: str) -> str:
        pass

class GreekLocalizer(Localizer):
    """
    A simple localizer a la gettext
    """
    def __init__(self) -> None:
        self.translations = {"dog": "σκύλος", "cat": "γάτα"}

    def localize(self, msg: str) -> str:
        """
        We'll punt if we don't have a translation
        """
        return self.translations.get(msg, msg)

class EnglishLocalizer(Localizer):
    """
    Simply echoes the message
    """
    def localize(self, msg: str) -> str:
        return msg

def get_localizer(language: str = "English") -> Localizer:
    """
    Factory
    """
    localizers: Dict[str, Type[Localizer]] = {
        "English": EnglishLocalizer,
        "Greek": GreekLocalizer,
    }
    return localizers[language]()

def main():
    # Create our localizers
    e, g = get_localizer(language="English"), get_localizer(language="Greek")

    # Localize some text
    for msg in "dog parrot cat bear".split():
        print(e.localize(msg), g.localize(msg))

if __name__ == "__main__":
    main()

"""
dog σκύλος
parrot parrot
cat γάτα
bear bear
"""
```


### 정리 이미지

---

![abstract_factory_rule](https://github.com/cwadven/design-patterns-with-python/blob/master/creational_patterns/factory/factory.png)