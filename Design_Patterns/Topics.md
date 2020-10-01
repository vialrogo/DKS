# Design Patterns

## Introdução

+ Originalmente o conceito de DP (ou Padrões de Projeto em português) foi criado por Christopher Alexander in _A Pattern Language: Towns, Buildings_ (1977). A pesar que teve algumas outras coisas no meio, a publicação que deixou o nome realmente conhecido na computação foi o livro _Design Patterns: Elements of Reusable Object-Oriented Software_ no 1994, e rapidamente virou a principal referência no tópico na área. Depois disso teve e continua tendo atualizações e reinterpretações.

+ Mas que são esses _Design Patterns_ ralmente? O curioso é que não tem um consenso. Alguns dizem que são templates e soluções prontas, outro técnicas e outros conselhos. Eu gosto pensar que é experiência condensada. Os DP são _para mim_ a versão escrita desse colega de trabalho velho que te diz: "Faz deste outro jeito que fica melhor, vai por mim". 

+ Como os padrões são basicamente exemplos de situações que acontecem comumente na engenharia de computação, existe um número infinito deles. Podem ser criados mais e mais dependendo do que se entenda por comum. O livro de _Design Patterns_ do '94 traz 23, mas muito outros tem sido criados. Alguns como derivações e outros como modificações.

+ É importante ter muito claro que os DP dependem do contexto. O livro do 94 foi apoiado nas soluções que usavam o paradigma orientado ao objetos, mas esse não é o único jeito de pensar e solucionar problemas na computação, e pode ser que em outros contextos um padrão determinado não aplique. Também dependem muito dos objetivos da programação, já que não é o mesmo programar com fins comerciais que acadêmicos ou de pesquisa. É sempre necessário ter critério antes de aceitar qualquer padrão.

+ Os DP também variam com o tempo e a moda. A programação orientada a objetos por exemplo, tem sido o padro da industria os últimos 30 anos, mas a forma como esse paradigma é usado tem mudado. Coisas como alocações explicitas de memoria, _structs_ e _sockets_ cada vez são menos usados, enquanto sistemas multi linguagens, interfaces e sistemas sem memória são cada vez mais comuns. Isto faz que um padrão que parecia uma ótima ideia faz décadas, hoje seja menos relevante.

+ Originalmente os DP foram divididos em categorias (isso foi proposto no livro do 94). Padrões de criação, de estrutura e de comportamento. Também na literatura as vezes é utilizado o conceito de padrões de arquitectura. Vou tentar seguir esta classificação.


## Bora lá, os DPs
