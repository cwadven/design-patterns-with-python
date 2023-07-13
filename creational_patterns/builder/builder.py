class Building:
    def __init__(self) -> None:
        self.build_floor()
        self.build_size()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

    def __repr__(self) -> str:
        return "Floor: {0.floor} | Size: {0.size}".format(self)


class House(Building):
    def build_floor(self) -> None:
        self.floor = "One"

    def build_size(self) -> None:
        self.size = "Big"


class Flat(Building):
    def build_floor(self) -> None:
        self.floor = "More than One"

    def build_size(self) -> None:
        self.size = "Small"


class ComplexBuilding:
    def __repr__(self) -> str:
        return "Floor: {0.floor} | Size: {0.size}".format(self)


class ComplexHouse(ComplexBuilding):
    def build_floor(self) -> None:
        self.floor = "One"

    def build_size(self) -> None:
        self.size = "Big and fancy"


def construct_building(cls) -> Building:
    building = cls()
    building.build_floor()
    building.build_size()
    return building


def main():
    house = House()
    print(house)
    # Floor: One | Size: Big

    flat = Flat()
    print(flat)
    # Floor: More than One | Size: Small

    complex_house = construct_building(ComplexHouse)
    print(complex_house)
    # Floor: One | Size: Big and fancy


if __name__ == "__main__":
    main()


"""
Floor: One | Size: Big
Floor: More than One | Size: Small
Floor: One | Size: Big and fancy
"""