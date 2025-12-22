import Strategy

#---------------Factory_Method

class Factory:
    def __init__(self):
        self.strategy_dict = {
            "+": Strategy.ConcreteStrategyAdd(),
            "-": Strategy.ConcreteStrategySubstract(),
            "*": Strategy.ConcreteStrategyMultiply(),
        }

    def getStrategy(self, ope: str) -> Strategy.Strategy:
    #choix:

    # 1) return self.strategy_dict[ope] if ope in self.strategy_dict else Strategy.ConcreteStrategyAdd()
    # ou :
        return self.strategy_dict.get(ope, Strategy.ConcreteStrategyAdd())

#----------------Strategy

class App:
    def __init__(self, a: int, b: int, ope: str):
        self.ctxt = Strategy.Context()

        self.a = a
        self.b = b
        self.ope = ope

    def main(self) -> int :
        factory = Factory()
        concrete_strategy = factory.getStrategy(self.ope)
        self.ctxt.setStrategy(concrete_strategy)
        return self.ctxt.executeStrategy(self.a, self.b)





if __name__ == "__main__":

    appli1 = App(1, 2, "+")
    appli2 = App(1, 2, "-")
    appli3 = App(1, 2, "*")

    print(appli1.main())
    print(appli2.main())
    print(appli3.main())