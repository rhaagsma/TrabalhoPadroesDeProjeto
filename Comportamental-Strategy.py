from abc import ABC, abstractmethod

# Interface da estratégia
class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a: int, b: int) -> int:
        pass

# Estratégia de Adição
class AdditionStrategy(OperationStrategy):
    def execute(self, a: int, b: int) -> int:
        return a + b

# Estratégia de Subtração
class SubtractionStrategy(OperationStrategy):
    def execute(self, a: int, b: int) -> int:
        return a - b

# Contexto que utiliza a estratégia
class Calculator:
    def __init__(self, strategy: OperationStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: OperationStrategy):
        self.strategy = strategy

    def calculate(self, a: int, b: int) -> int:
        return self.strategy.execute(a, b)

# Testando o padrão Strategy
if __name__ == "__main__":
    # Inicialmente usando adição
    calculator = Calculator(AdditionStrategy())
    print(f"Adição: {calculator.calculate(10, 5)}")  # Saída: 15

    # Mudando para subtração
    calculator.set_strategy(SubtractionStrategy())
    print(f"Subtração: {calculator.calculate(10, 5)}")  # Saída: 5
