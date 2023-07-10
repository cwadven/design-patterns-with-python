<aside>

❓ **이 패턴에 대해 어떤 것인가?**

</aside>

Borg 패턴 또는 Monostate 패턴으로 알려진 이 패턴은 싱글톤 동작을 구현하는 방법이다.

하지만 한 클래스의 오직 하나의 인스턴스를 가지는 것이 아닌, 동일한 상태를 공유하는 여러 인스턴스를 가진다.

즉, 인스턴스 식별성을 공유하는 대신 상태를 공유하는 데 초점을 둔다.

<aside>

📝 **이 예제는 무엇을 하는 것인가?**

</aside>

이 패턴이 Python에서 어떻게 구현되는지 이해하려면, Python에서 인스턴스 속성이 `__dict__` 라는 속성 딕셔너리에 저장된다는 것을 알아야 한다.

보통, 각 인스턴스는 자기만의 딕셔너리를 가지지만, **Borg 패턴**은 이를 수정하여 모든 인스턴스가 동일한 딕셔너리를 가지도록 한다.

이 예제에서, `__shared_state` 속성은 모든 인스턴스 간에 공유될 딕셔너리가 될 것이며, 이는 새로운 인스턴스를 초기화할 때 (`init` 메서드에서) `__shared_state` 를 `dict` 변수에 할당함으로써 보장된다.

다른 속성들은 보통 인스턴스의 속성 딕셔너리에 추가되지만, 속성 딕셔너리 자체가 공유되는 것이기 때문에, 다른 모든 속성들도 공유되게 됩니다.

<aside>

✏️ **어디서 자주 쓰이는가?**

</aside>

**데이터베이스 connection** 에서 자주 쓰입니다.

<aside>

📖 **한 줄 요약**

</aside>

### 코드

---

```python
from typing import Dict


class Borg:
    _shared_state: Dict[str, str] = {}

    def __init__(self) -> None:
        self.__dict__ = self._shared_state


class YourBorg(Borg):
    def __init__(self, state: str = None) -> None:
        super().__init__()
        if state:
            self.state = state
        else:
            # initiate the first instance with default state
            if not hasattr(self, "state"):
                self.state = "Init"

    def __str__(self) -> str:
        return self.state


def main():
    rm1 = YourBorg()
    rm2 = YourBorg()

    rm1.state = "Idle"
    rm2.state = "Running"

    print("rm1: {0}".format(rm1))
    # rm1: Running
    print("rm2: {0}".format(rm2))
    # rm2: Running

    # rm2 에서 state 를 변경하면 rm1 의 state 도 변경됩니다.
    rm2.state = "Zombie"

    print("rm1: {0}".format(rm1))
    # rm1: Zombie
    print("rm2: {0}".format(rm2))
    # rm2: Zombie

    # rm1 과 rm2 는 같이 attribute 를 공유하지만 다른 객체입니다.
    print(rm1 is rm2)
    # False

    # 새로운 객체 또한 같은 attribute 를 공유합니다.
    rm3 = YourBorg()

    print("rm1: {0}".format(rm1))
    # rm1: Zombie
    print("rm2: {0}".format(rm2))
    # rm2: Zombie
    print("rm3: {0}".format(rm3))
    # rm3: Zombie

    # 새로운 객체를 생성할 때 state 를 변경하면 모든 객체의 state 가 변경됩니다.
    rm4 = YourBorg("Running")

    print("rm4: {0}".format(rm4))
    # rm4: Running

    # 존재하고 있던 객체도 state 가 변경됩니다.
    print("rm1: {0}".format(rm1))
    # rm1: Running


if __name__ == '__main__':
    main()
```