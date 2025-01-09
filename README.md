# TrabalhoPadroesDeProjeto
Trabalho da Disciplina de Engenharia de Software - Implementando Padrões de Projeto

O presente trabalho utiliza como fonte de referência o conteúdo disponibilizado no site Refactoring Guru, acessível em: https://refactoring.guru.
## 1 - Padrão Criacional: Singleton
Qual Problema ele resolve?

Primeiramente, o padrão Singleton viola o princípio de responsabilidade única, um conceito de desenvolvimento de software orientado à objetos que define que uma classe deve ter apenas uma responsabilidade, deve ser responsável por uma parte única do software.

No caso do Singleton, ele resolve 2 problemas:

1. Ele garante que uma classe tenha só uma instância. Toda vez que tentarmos instanciar uma classe, iremos ser direcionados à única instância dessa classe, feita pelo construtor único definido nela. O que nos leva ao segundo problema que o padrão resolve:

2. Ele fornece um ponto de acesso global para aquela instância. Com essa classe com a instância singleton, você pode acessar um objeto dela em qualquer lugar do programa.

Qual a Solução?

- O construtor da classe é privado, dessa forma, outros objetos não podem usar o operador new com a classe singleton
- Criar um método estático que age como um construtor. Esse método vai chamar o construtor privado, e assim todas as chamadas seguintes para esse método chamarão o objeto já criado previamente.

Diagrama UML do funcionamento do Singleton:

![Singleton](https://github.com/user-attachments/assets/82355459-dc1d-4e21-a0c6-3dc43fc12801)


## Explicando o código Criacional-Singleton.py
O método __new__ controla a criação de novas instâncias. Ele só cria uma instância caso ela ainda não existe, garantindo que só existirá uma única instância da classe.

O método __init__ verifica se o objeto não possui um valor de configuração ou estado atribuído à instância, e atribui esse valor à instância somente se ele ainda não existir, garantindo que haverá somente uma instância com este valor.

Teste: Ao criar duas instâncias (singleton1 e singleton2), elas apontam para o mesmo objeto na memória.

## 2 - Padrão Estrutural: Bridge
Qual Problema ele resolve?

Esse padrão resolve o problema de quando temos uma única classe com várias combinações de subclasses que relacionam os objetos de forma hierárquica, fazendo com que essas conexões se tornem dependências, ou seja, as alterações numa classe alteram as demais classes relacionadas.

Qual a Solução?

Utiliza-se subclasses com a estrutura de composição ao invés de hierárquica. Dessa forma podemos estruturar partes menores das subclasses, ou seja, invés de rlacionarmos as classes diretamente entre si, as relacionamos atrave´s de classes auxiliares prórpias para conexão, deste modo, cada classe é independente de si, visto que a conexão não é mais feita dentro da implementação.

Diagrama UML do funcionamento do Bridge:

![Bridge](https://github.com/user-attachments/assets/9eaf120f-90d7-4ba1-b2a8-7b6fc5f67a58)


## Explicando o código Estrutural-Bridge.py
Na parte do código de Implementação, há uma classe "Renderer" que possui um método abstrato "render", servindo como uma interface para que as subclasses concretas utilizem esse método. Estas subclasses definem como a implementação será feita.

Depois, na parte de Abstração, é definido uma classe "Shape". Ela é uma abstração base, representando o conceito de uma forma geométrica, definindo um nome e um comportamento(draw). O método draw chama o método render da classe Renderer, delegando a responsabilidade da implementação a ela. A classe Shape não sabe e não precisa saber como a forma será desenhada, pois é a partir desse desacoplamento que se dá o padrão Bridge. Dessa forma, podemos alterar e estender a abstração e a implementação de forma independente, sem que uma interfira na outra.

## 3 - Padrão Comportamental: Strategy
Qual Problema ele resolve?

Esse padrão soluciona o problema de quando temos formas diferentes de executar uma mesma tarefa. Caso usássemos uma única função que pode executar todas as formas de executar a tarefa, seria muito difícil alterar somente uma das formas sem afetar todo o resto do código.

Qual a Solução?

Primeiramente, temos classes separadas chamadas estratégias, onde são implementadas as diferentes formas de executar a mesma tarefa. Temos a classe principal chamada contexto, que tem um campo referenciando uma das estratégias, que será executada. Porém, essa classe principal não sabe muito sobre as estratégias, a escolha da estratégia ocorre por meio de uma classe genérica interface, onde será selecionado qual estratégia será acionada.

Diagrama UML do funcionamento do Strategy:

![Strategy](https://github.com/user-attachments/assets/63c6fb75-38c4-4de4-a0f5-a3df3a140417)


## Explicando o código Comportamental-Strategy.py

A Interface da estratégia é representada pela classe OperationStrategy, que define o método abstrato execute. Todas as estratégias concretas devem implementar esse método, cada uma fornecendo uma forma diferente de processar as mesmas entradas

O Contexto que utiliza a estratégia é a classe Calculator. Ela delega a execução da operação ao método execute da estratégia selecionada, sem precisar saber como essa operação é implementada. Essa abstração permite que o comportamento da classe Calculator seja alterado facilmente, simplesmente trocando a estratégia em tempo de execução. Assim, o padrão Strategy promove flexibilidade e desacoplamento entre o contexto e as lógicas específicas de operação.
