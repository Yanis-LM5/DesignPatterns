from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, a: int, b: int) -> None:
        pass
    #question self ^\^|

class ConcreteStrategyAdd(Strategy):
    # def __init__(self, a: int, b: int):
    #     self.a = a
    #     self.b = b

    def execute(self,  a: int, b: int ) -> int:
        return a + b

class ConcreteStrategySubstract(Strategy):

    # def __init__(self, a: int, b: int):
    #     self.a = a
    #     self.b = b

    def execute(self, a: int, b: int) -> int:
        return a - b

class ConcreteStrategyMultiply(Strategy):

    # def __init__(self, a: int, b: int):
    #     self.a = a
    #     self.b = b

    def execute(self, a: int, b: int) -> int:
        return a * b


class Context:

    def setStrategy(self, strat: Strategy) -> None:
        self.__strat: Strategy = strat

    def executeStrategy(self, a: int, b: int) -> int:
        return self.__strat.execute(a,b)

class App:


    def __init__(self, a: int, b: int, ope: str):
        self.ctxt = Context()

        self.a = a
        self.b = b
        self.ope = ope

    def main(self) -> int :

        if self.ope == "+":
            self.ctxt.setStrategy(ConcreteStrategyAdd())

        elif self.ope == "-":
            self.ctxt.setStrategy(ConcreteStrategySubstract())

        elif self.ope == "*":
            self.ctxt.setStrategy(ConcreteStrategyMultiply())

        return self.ctxt.executeStrategy(self.a, self.b)

if __name__ == "__main__":

    appli1 = App(1, 2, "+")
    appli2 = App(1, 2, "-")
    appli3 = App(1, 2, "*")

    print(appli1.main())
    print(appli2.main())
    print(appli3.main())