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