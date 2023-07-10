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
