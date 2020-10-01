Scrum desfiado
==============

Scrum é um framework, ou seja, *não* é nem um processo, *nem* um método, é um marco de trabalho que permite definir processos

No Scrum temos:
+ Equipe + Roles
    - Product Owner
    - Dev Team
    - Scrum Master
+ Eventos
    - Sprint
        * Planejamento do Sprint
        * Scrum diário
        * Sprint Review
        * Sprint Retrospective
+ Artefatos
    - Product Backlog
    - Sprint Backlog
+ Regras

As equipes em Scrum têm que ser pequenas

As equipes têm roles

As regras juntam tudo: Equipes com Roles, tem Eventos e fazem Artefatos, seguindo as regras

O processo no Scrum é empírico e precisa então de:
+ Transparência nas informações
+ Constante inspeção e autocrítica
+ Constante adaptação

As inspeções e revisões não devem ser tão frequentes que atrapalhem o trabalho

Os ajuste tem que ser feitos o mais rápido possível

Valores da Equipe:
+ Comprometimento
+ Coragem
+ Foco
+ Mente aberta
+ Respeito

Valores do Processo:
+ Transparência
+ Inspeção
+ Adaptação


# Equipe

A equipe se compõe de 3 partes:
+ Product Owner
+ Dev team
+ Scrum Master

A equipe tem que ser:
+ Auto organizado
+ Multifuncional
+ Auto contido / Auto suficiente


## Product Owner
+ Seu objetivo é maximizar o valor do produto
+ Ele tem que garantir que todos entendam o que o produto tem e o que vai ser feito a seguir
+ É uma pessoa. Pode ter um time para ajudar, mas é uma pessoa.


## Dev team
+ São que incrementam a lista de *Done* (e são os únicos!)
+ É auto organizado
+ Ninguém diz ao Dev Team como fazer seu trabalho
+ É multifuncional
+ Não tem títulos internos nem sub equipes
+ A responsabilidade é de todos da equipe
+ Um bom tamanho é de 3 a 9 pessoas (two pizza team)


## Scrum Master
+ Ajuda a executar Scrum
+ Líder
+ Interatua com as pessoas externas (é um intermediário)

Scrum Master => Dev Team
+ Coach
+ Explicar o valor do produto
+ Fazer o Meio-campo

Scrum Master => Product Owner
+ Conferir/Corrigir objetivos e escopo
+ Intermediar caso necessário

Scrum Master => Organização
+ Coordenar o Scrum
+ Explicar para os empregados e outros atores como usar o processo
+ Implementar mudanças


# Eventos
+ Todos os eventos são de "tempo fechado"
+ Sprints são eventos
+ Reuniões também são eventos

## Sprint
+ Duração fixa, máximo 1 mês (recomendado entre 2 semanas e 1 mês)
+ O resultado é um **produto**
+ Todos os Sprints ao longo do projeto são do mesmo tamanho
+ Cada Sprint começa imediatamente quando o anterior termina

Durante o Sprint:
+ Não é modificado o objetivo
+ Não é diminuída a qualidade esperada
+ Pode-se esclarecer o escopo
+ O Sprint pode ser cancelado (se percebe-se que o objetivo do Sprint parou de fazer sentido)

Partes do Sprint:
+ Planejamento
+ Scrum diário
+ Desenvolvimento
+ Revisão
+ Retrospectiva

### Planejamento do Sprint
+ Feito pela equipe toda
+ Duração fixa
+ Máximo 8 horas por cada mês de Sprint


O planejamento responde:
+ Que pode ser entregue/desenvolvido no Sprint
+ Como é o trabalho para fazer a entrega

```plain
+---------+          Capacidade do time        +------+
| Product |  <-------------------------------  | Dev  |
|  Owner  |  ------------------------------->  | Team |
+---------+    Seleciona um item do Backlog    +------+
     ^                                             ^
     |                  ~~~~~~~~~~~                |
     |                 {  Objttivo }               |
     |                 { do Sprint }               |
     |                  ~~~~~~~~~~~                |
     |                                             |
     |                   +--------+                |
     +------------------ | Scrum  | <--------------+
        O que pode       | Master |    Como vai ser
       ser entregue      +--------+     o trabalho
```

Entradas do planejamento:
+ Product Backlog
+ O que foi feito no último Sprint
+ Capacidade do time

Saídas do planejamento:
+ O objetivo do Sprint
+ O trabalho que vai ser feito nesse sprint (Sprint Backlog)
+ Como o trabalho vai ser feito


### Scrum diário
+ Tem duração fixa de 15 minutos
+ É diário. Nele se planejam as próximas 24 horas de trabalho
+ Para evitar atrasos e esforço extra, ele se faz no mesmo local e horário sempre
+ O Scrum Master garante que a reunião aconteça
+ A reunião é dirigida pela equipe de desenvolvimento


### Sprint Review
+ Revisa qual foi o incremento e atualiza o Product Backlog
+ Tem que durar, no máximo, 4 horas por mês de Sprint


### Sprint Retrospective
+ Reunião para analisar como foi o Sprint e mudar como se faz o trabalho.
+ Se faz depois do review e antes do próximo planejamento.
+ Máximo 3 horas por cada mês de Sprint


# Artefatos
+ O objetivo principal dos artefatos é prover transparência a todos os membros da equipe


## Product Backlog
+ É uma lista ordenada
+ Contem tudo o que é necessário no produto
+ É uma lista única
+ Jamais está completa, se estivesse, o projeto acabaria
+ O Product Owner é o responsável por esta lista
+ Inclui informações do produto e do ambiente
+ Muda constantemente
+ Esta lista inclui de tudo, características, funções, requerimentos, melhoras e concertos


A lista do Product Backlog tem:
+ Número do item
+ Descrição do item
+ Ordem: define a prioridade do item
+ Estimativa: tempo para realizar estimado pela equipe de desenvolvimento
+ Test: Que provas mostram que o item está operacional
+ Estado: 
    - New: Acabou de chegar na lista
    - Ready: Já foi pensado e dividido em um tamanho suficientemente pequeno para ser feito em um sprint. Ou seja, já pode ser seleccionado para um sprint
    - Done: foi concluído
+ A lista do Product Backlog sempre está em completo refinamento, mas este processo não deve levar mais de 10% do tempo da equipe de desenvolvimento
+ Done é uma convenção. A equipe de desenvolvimento define o que vai se entender como Done


## Sprint Backlog
+ É um subconjunto do Product Backlog que vai ser feito no sprint
+ Inclui o plano para integrar os incrementos no produto
+ Fazendo o Sprint Backlog se atinge o Sprint Goal
+ Inclui melhorias vinda da reunião de retrospectiva
+ Só a equipe de desenvolvimento pode mudar a lista do Sprint Backlog durante o Sprint
