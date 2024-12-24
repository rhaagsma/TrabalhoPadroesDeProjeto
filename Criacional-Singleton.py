class Singleton:
    _instance = None  # Atributo de classe para armazenar a instância única

    def __new__(cls, *args, **kwargs): #cls é uma convenção de como chamar o parâmetro de classe 
        if not cls._instance:  # Se ainda não há instância criada
            cls._instance = super().__new__(cls)  # Cria a instância
        return cls._instance  # Retorna a instância única

    def __init__(self, value=None):
        if not hasattr(self, "value"):  # função hasattr: verifica se um objeto possui um atributo específico 
            self.value = value #Garante que o valor seja inicializado apenas uma vez


# Testando o Singleton
singleton1 = Singleton("Primeira instância")
print(f"singleton1.value: {singleton1.value}")

singleton2 = Singleton("Segunda instância")
print(f"singleton2.value: {singleton2.value}")

# Verificando se é a mesma instância
print(f"singleton1 é singleton2? {singleton1 is singleton2}")
