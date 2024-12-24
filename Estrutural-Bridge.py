from abc import ABC, abstractmethod

# Implementação (Define como será feito, essa parte pode variar sem afetar a abstração)
class Renderer(ABC):
    @abstractmethod
    def render(self, shape):
        pass

class VectorRenderer(Renderer):
    def render(self, shape):
        return f"Desenhando {shape.name} com linhas vetoriais"

class RasterRenderer(Renderer):
    def render(self, shape):
        return f"Desenhando {shape.name} com pixels rasterizados"

# Abstração (A parte principal que utiliza a implementação)
class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @property
    @abstractmethod
    def name(self):
        pass

    def draw(self):
        return self.renderer.render(self)

class Circle(Shape):
    @property
    def name(self):
        return "Círculo"

class Square(Shape):
    @property
    def name(self):
        return "Quadrado"

# Testando o padrão Bridge
if __name__ == "__main__":
    # Usando renderização vetorial
    vector_renderer = VectorRenderer()
    circle = Circle(vector_renderer)
    print(circle.draw())  # Saída: Desenhando Círculo com linhas vetoriais

    # Usando renderização rasterizada
    raster_renderer = RasterRenderer()
    square = Square(raster_renderer)
    print(square.draw())  # Saída: Desenhando Quadrado com pixels rasterizados