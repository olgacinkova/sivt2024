class Ucet:

    def __init__(self, zustatek: int =0):
        self.zustatek = zustatek

    def pridej(self, kolik: int) -> None:
        self.zustatek += kolik
        return None

    def uber(self, kolik:int) -> None:
        self.zustatek -= kolik
        return None


if __name__ == "__main__":
    ucet = Ucet(101)
    ucet.pridej(100)
    ucet.uber(200)
    print("jupiii")
    print("uaaaaa")
    print(ucet.zustatek)
