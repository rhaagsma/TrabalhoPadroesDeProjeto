# TrabalhoPadroesDeProjeto
Trabalho da Disciplina de Engenharia de Software - Implementando Padrões de Projeto

## 1 - Padrão Criacional: Singleton
Qual Problema ele resolve?

Primeiramente, o padrão Singleton viola o princípio de responsabilidade única, um conceito de desenvolvimento de software orientado à objetos que define que uma classe deve ter apenas uma responsabilidade, deve ser responsável por uma parte única do software.

No caso do Singleton, ele resolve 2 problemas:

1. Ele garante que uma classe tenha só uma instância. Toda vez que tentarmos instanciar uma classe, iremos ser direcionados à única instância dessa classe, feita pelo construtor único definido nela. O que nos leva ao segundo problema que o padrão resolve:

2. Ele fornece um ponto de acesso global para aquela instância. Com essa classe com a instância singleton, você pode acessar um objeto dela em qualquer lugar do programa.

Qual a Solução?

- O construtor da classe é privado, dessa forma, outros objetos não podem usar o operador new com a classe singleton
- Criar um método estático que age como um construtor. Esse método vai chamar o construtor privado, e assim todas as chamadas seguintes para esse método chamarão o objeto já criado previamente.

Código de Exemplo explicado:
```python
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
```
## 2 - Padrão Estrutural: Bridge
Qual Problema ele resolve?

Esse padrão resolve o problema de quando temos uma única classe com várias combinações de subclasses que relacionam os objetos de forma hierárquica, fazendo com que essas conexões se tornem dependências, ou seja, as alterações numa classe alteram as demais classes relacionadas

Qual a Solução?

Utiliza-se subclasses com a estrutura de composição ao invés de hierárquica. Dessa forma podemos estruturar partes menores das subclasses, ou seja, invés de rlacionarmos as classes diretamente entre si, as relacionamos atrave´s de classes auxiliares prórpias para conexão, deste modo, cada classe é independente de si, visto que a conexão não é mais feita dentro da implementação 

## 3 - Padrão Comportamental: Strategy
Qual Problema ele resolve?

Esse padrão soluciona o problema de quando temos formas diferentes de executar uma mesma tarefa. Caso usássemos uma única função que pode executar todas as formas de executar a tarefa, seria muito difícil alterar somente uma das formas sem afetar todo o resto do código.

Qual a Solução?

O padrão utiliza uma classe principal contexto, que tem a capacidade de 
