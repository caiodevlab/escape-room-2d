# Escape Room Escolar 2D

Jogo 2D desenvolvido em **Godot** para um projeto escolar.

O jogador assume o papel de um aluno preso dentro da escola e precisa explorar o ambiente, encontrar pistas, resolver desafios relacionados a conteúdos escolares e desbloquear o caminho até a saída.

O objetivo principal é entregar um jogo **funcional, simples e apresentável**, priorizando gameplay e conclusão do projeto em vez de complexidade técnica ou gráficos avançados.
## Conceito final do jogo

O jogo será um Escape Room 2D ambientado dentro de uma escola, com visual simples e atmosfera de suspense leve. O jogador acorda trancado em uma sala e descobre que a escola foi fechada por um motivo misterioso. Para escapar, ele precisará explorar os corredores, salas e ambientes da instituição, coletar pistas, resolver enigmas baseados em matérias escolares e encontrar a forma de abrir a porta de saída.

O foco do jogo está em uma progressão clara, divertida e educativa: cada área apresenta um desafio diferente, e a solução de cada um desbloqueia o caminho para a próxima etapa. A mecânica principal é explorar, descobrir, interagir e usar as informações encontradas para avançar.

### Objetivo principal

Escapar da escola antes que o tempo acabe ou antes que a situação piore. Para isso, o jogador deve:

- explorar o mapa;
- encontrar pistas e itens;
- resolver desafios e perguntas escolares;
- desbloquear portas, salas e corredores;
- alcançar a saída final.

### Início

O jogo começa em uma sala de aula vazia, com a porta de saída aparentemente trancada e algumas pistas iniciais espalhadas pelo ambiente. O jogador aprende os controles básicos e recebe a primeira missão: investigar o local, procurar informações e entender como a escola está organizada.

Neste momento, a narrativa é discreta e a sensação de confinamento ajuda a criar o clima de escape room. O primeiro desafio introduz o jogador ao tipo de puzzle que será encontrado ao longo do jogo.

### Meio

No desenvolvimento do jogo, o jogador avança por diferentes ambientes da escola, como corredor, biblioteca, laboratório, sala de informática ou direção. Em cada local, ele encontra novas pistas e precisa solucionar enigmas que podem exigir:

- responder perguntas de matemática, português, ciências e história;
- localizar combinações ou códigos;
- encontrar chaves ou itens necessários;
- usar objetos do cenário corretamente;
- interpretar pistas visuais e textuais.

É nessa etapa que a progressão principal acontece. O jogador começa a entender a lógica do jogo e percebe que cada solução abre uma nova etapa, aproximando-o da saída.

### Final

Ao resolver os últimos desafios, o jogador reúne os itens e códigos necessários para abrir a porta principal da escola. A saída final é o momento de conclusão do jogo, em que o jogador confirma a fuga e encerra a experiência com uma sensação de vitória e resolução.

A conclusão pode ser reforçada por uma tela de vitória, mensagem final ou pequena animação de encerramento, mantendo a proposta simples e eficaz do projeto.
---

## 1. Visão geral

### Conceito

O jogador está preso dentro da escola.

Para escapar, ele precisa:

1. Explorar salas e corredores;
2. Encontrar objetos e pistas;
3. Interagir com elementos do cenário;
4. Resolver enigmas;
5. Responder perguntas relacionadas às matérias escolares;
6. Desbloquear novas áreas;
7. Chegar à saída final.

### Gênero

- Escape Room
- Puzzle
- Exploração
- Educacional

### Engine

**Godot 4.x**

### Dimensão

**2D**

### Plataforma principal

Computador para desenvolvimento e apresentação escolar.

A arquitetura deve evitar decisões que dificultem uma futura adaptação para outras plataformas, mas **não desenvolver suporte mobile nesta etapa**.

---

# 2. Objetivo do projeto

O objetivo NÃO é criar um jogo comercial enorme.

O objetivo é criar um **Escape Room escolar completo e jogável**.

A prioridade é:

1. Jogo funcionar do início ao fim;
2. Mecânicas principais funcionarem;
3. Puzzles funcionarem;
4. Progressão fazer sentido;
5. Visual ser consistente;
6. Apresentação ser boa.

Não devemos sacrificar a conclusão do projeto tentando adicionar funcionalidades desnecessárias.

---

# 3. Loop principal

O loop esperado é:

```text
Explorar
   ↓
Encontrar pista/objeto
   ↓
Interagir
   ↓
Resolver desafio
   ↓
Desbloquear área/objeto
   ↓
Continuar exploração
   ↓
Resolver novos desafios
   ↓
Encontrar saída
   ↓
Finalizar jogo
```

---

# 4. Fluxo do jogo

A progressão do jogo deve seguir uma sequência lógica, com cada sala introduzindo uma nova pista e um novo desafio. O objetivo é manter o jogador sempre avançando, sem travar em puzzles sem contexto.

## 4.1 Mapa e sequência de salas

```text
Sala de aula inicial
   ↓
Descobrir pista do armário
   ↓
Armário / corredor
   ↓
Encontrar chave do laboratório
   ↓
Laboratório
   ↓
Resolver enigma ou pergunta escolar
   ↓
Obter código da biblioteca
   ↓
Biblioteca
   ↓
Encontrar pista da sala da direção
   ↓
Sala da direção / informática
   ↓
Resolver último desafio
   ↓
Desbloquear porta da saída
   ↓
VITÓRIA
```

## 4.2 Sequência de pistas e desafios

### 1. Sala de aula inicial

- O jogador começa preso dentro da sala.
- A primeira pista está no quadro, em cadernos ou em um aviso do professor.
- Essa pista indica onde está o armário ou o primeiro item essencial.
- Desafio inicial: descobrir uma combinação simples ou identificar um objeto escondido.

### 2. Armário / corredor

- O jogador encontra uma chave, um bilhete ou um código.
- A informação leva ao laboratório.
- Esse trecho serve para introduzir a lógica do jogo: procurar, observar e interagir.

### 3. Laboratório

- O ambiente apresenta um enigma com pergunta escolar ou combinação.
- Exemplo: resolver uma conta, responder uma questão de ciências ou localizar um símbolo correto.
- A solução revela um código ou item que abre a próxima área.

### 4. Biblioteca

- O jogador precisa procurar um livro, diário ou sinalização que contenha a próxima pista.
- Essa área ajuda a reforçar o tema educacional do jogo.
- Pode incluir uma pergunta de português, história ou geografia.

### 5. Sala da direção / informática

- O jogador recebe a informação final necessária para abrir a saída.
- O desafio pode envolver a combinação correta de código, senha ou sequência de objetos.
- Essa etapa representa o ponto mais importante da progressão.

### 6. Saída

- Ao inserir o código ou usar o item correto, a porta abre.
- A tela final pode mostrar uma mensagem de vitória e encerrar a experiência.

## 4.3 Lógica da progressão

Cada área deve ter:

- uma pista clara;
- um objetivo específico;
- uma recompensa imediata;
- conexão direta com a próxima etapa.

A sequência precisa ser simples de seguir, para que o jogador entenda onde ir e o que precisa fazer sem ficar perdido. O importante é que cada desafio resolvido resulte em uma abertura, uma chave, uma senha ou uma nova direção.

## 4.4 Esboço do mapa da escola

O mapa pode ser uma escola pequena e organizada, com corredores e salas conectadas em um layout simples e jogável.

```text
+-----------------------------------------------------------+
|                       CORREDOR CENTRAL                    |
|  [Sala de aula] -- [Corredor] -- [Armário] -- [Laboratório] |
|       |                               |                  |
|       |                               |                  |
|  [Biblioteca] ---------------------- [Sala da direção]   |
|                               |                           |
|                         [Porta da saída]                  |
+-----------------------------------------------------------+
```

### Estrutura funcional

- Sala de aula inicial: ponto de partida, primeira pista e introdução ao jogo.
- Armário: contém objeto ou chave inicial.
- Corredor central: liga as áreas e guia o jogador para os próximos desafios.
- Laboratório: local do primeiro enigma mais técnico.
- Biblioteca: área de pesquisa e pistas textuais.
- Sala da direção / informática: última etapa antes da saída.
- Porta da saída: objetivo final do jogo.

### Observações de nível

- O mapa deve ser pequeno o suficiente para ser percorrido rapidamente.
- Os corredores devem funcionar como caminhos de conexão e não como área sem objetivo.
- Cada sala deve ter pelo menos um ponto visual de destaque, como mesa, quadro, armário, livro ou computador.
- A porta final precisa ser visível ou claramente indicada antes do último desafio.

---

# 5. Mecânicas principais

## 4.1 Movimento

O jogador deve conseguir:

- andar pelo mapa;
- colidir com paredes e obstáculos;
- entrar nas áreas permitidas.

O sistema deve ser simples e confiável.

Não adicionar sistemas avançados de movimento sem necessidade.

---

## 4.2 Interação

O jogador deve conseguir interagir com objetos importantes.

Exemplo:

```text
Jogador se aproxima do objeto
        ↓
Aparece indicação de interação
        ↓
Jogador pressiona E
        ↓
Objeto executa sua ação
```

A tecla de interação inicialmente será:

**E**

Se houver necessidade de alterar isso posteriormente, centralizar a configuração.

---

## 4.3 Objetos

Exemplos:

- portas;
- armários;
- mesas;
- quadros;
- computadores;
- livros;
- pistas;
- chaves;
- objetos necessários para puzzles.

Nem todo objeto precisa ser interativo.

---

## 4.4 Pistas

Pistas devem ajudar o jogador a resolver os desafios.

Exemplos:

- texto;
- número;
- símbolo;
- combinação;
- objeto;
- informação escondida no cenário.

As pistas devem fazer sentido dentro da lógica do puzzle.

---

## 4.5 Itens

Alguns desafios podem exigir que o jogador encontre e utilize itens.

Exemplo:

```text
Encontrar chave
      ↓
Guardar/identificar chave
      ↓
Encontrar porta correspondente
      ↓
Usar chave
      ↓
Porta desbloqueada
```

O sistema de itens deve ser simples.

Não criar um inventário complexo se não for necessário.

---

## 4.6 Puzzles

Os puzzles são uma das partes mais importantes do jogo.

Cada puzzle deve possuir:

- objetivo claro;
- pista ou informação necessária;
- solução;
- consequência ao resolver;
- integração com a progressão.

Exemplo:

```text
Pista encontrada
      ↓
Jogador descobre código
      ↓
Insere código
      ↓
Código correto
      ↓
Porta desbloqueada
```

---

## 4.7 Perguntas escolares

O jogo poderá utilizar perguntas relacionadas às matérias escolares.

Exemplos:

- Matemática;
- Português;
- História;
- Geografia;
- Ciências;
- Inglês;
- outras matérias definidas pelo grupo.

As perguntas devem estar integradas ao gameplay.

Não devem ser apenas uma lista de perguntas desconectadas do jogo.

---

# 5. Progressão

A progressão deve ser linear ou semi-linear.

Exemplo:

```text
Sala inicial
    ↓
Primeiro puzzle
    ↓
Corredor
    ↓
Segunda sala
    ↓
Segundo puzzle
    ↓
Nova área
    ↓
Desafio final
    ↓
Saída
```

O mapa não precisa ser enorme.

É melhor ter poucas salas bem feitas do que muitas salas incompletas.

---

# 6. Estrutura planejada

A estrutura pode evoluir conforme o projeto cresce, mas a organização recomendada é:

```text
escape-room-2d/
│
├── README.md
│
├── project.godot
│
├── scenes/
│   ├── main/
│   ├── player/
│   ├── rooms/
│   ├── objects/
│   ├── puzzles/
│   └── ui/
│
├── scripts/
│   ├── player/
│   ├── interaction/
│   ├── puzzles/
│   ├── objects/
│   └── systems/
│
├── assets/
│   ├── sprites/
│   ├── tilesets/
│   ├── ui/
│   ├── audio/
│   └── fonts/
│
└── docs/
    ├── game-design.md
    └── kanban.md
```

A estrutura não é obrigatória enquanto o projeto ainda estiver começando.

Não criar dezenas de pastas vazias apenas para seguir o README.

---

# 7. Organização do trabalho

O projeto possui 4 integrantes.

## Pessoa 1 — Programação e Integração

Responsável principalmente por:

- player;
- movimento;
- interação;
- portas;
- itens;
- puzzles;
- integração das mecânicas;
- correção de bugs;
- build final.

---

## Pessoa 2 — Level Design

Responsável principalmente por:

- mapa;
- salas;
- corredores;
- posicionamento dos objetos;
- colisões;
- fluxo de exploração;
- organização do nível.

---

## Pessoa 3 — Game Design e Conteúdo

Responsável principalmente por:

- história;
- objetivos;
- puzzles;
- pistas;
- perguntas escolares;
- soluções;
- dificuldade;
- testes de gameplay.

---

## Pessoa 4 — Arte, UI e Áudio

Responsável principalmente por:

- sprites;
- tiles;
- objetos visuais;
- interface;
- efeitos visuais simples;
- sons;
- música;
- identidade visual.

---

# 8. Regra de integração

Apesar da divisão de responsabilidades, o jogo pertence ao grupo inteiro.

Uma tarefa não deve ser considerada concluída apenas porque o arquivo foi criado.

Exemplo:

> "Player feito"

não significa necessariamente que a tarefa está pronta.

A tarefa só está concluída quando:

```text
Implementado
    +
Integrado
    +
Testado
    =
Concluído
```

---

# 9. Regras para desenvolvimento

## Regra 1 — Funcionalidade antes de polimento

Primeiro:

- movimento;
- interação;
- puzzles;
- progressão;
- final.

Depois:

- arte;
- sons;
- efeitos;
- polimento.

---

## Regra 2 — Não criar complexidade desnecessária

Evitar:

- sistemas complexos;
- arquitetura exagerada;
- frameworks externos desnecessários;
- plugins sem necessidade;
- sistemas que não contribuem para o gameplay.

O projeto é escolar.

A solução mais simples que funciona corretamente é preferível.

---

## Regra 3 — Não fazer "vibe coding" sem entender

O código pode ser criado com auxílio de IA, mas os integrantes precisam entender o que foi implementado.

A IA deve explicar:

- o que mudou;
- onde mudou;
- por que mudou;
- como testar.

Não simplesmente gerar centenas de linhas sem explicação.

---

# 10. Regras para IA — Hermes Agent / VS Code

Este projeto pode utilizar ferramentas de IA durante o desenvolvimento.

A IA deve seguir estas regras.

### Antes de modificar

Sempre:

1. Ler os arquivos relevantes;
2. Entender a estrutura existente;
3. Verificar dependências;
4. Identificar como a funcionalidade atual funciona;
5. Só então modificar.

---

### Não fazer

A IA NÃO deve:

- reescrever o projeto inteiro;
- trocar a engine;
- migrar para 3D;
- criar arquitetura complexa;
- adicionar funcionalidades não solicitadas;
- modificar várias partes sem necessidade;
- apagar código sem verificar dependências;
- instalar plugins sem necessidade;
- criar mocks para esconder funcionalidades incompletas.

---

### Para tarefas grandes

Dividir em etapas.

Exemplo:

```text
1. Analisar
2. Planejar
3. Implementar
4. Testar
5. Corrigir
6. Relatar
```

---

### Para tarefas pequenas

Fazer apenas a alteração solicitada.

Não aproveitar uma tarefa simples para "melhorar todo o projeto".

---

# 11. Git

O projeto utiliza Git/GitHub.

Antes de fazer alterações grandes:

```bash
git status
```

Verificar o estado atual do projeto.

Não sobrescrever trabalho de outros integrantes.

Não fazer commit automaticamente quando uma tarefa for executada por IA, a menos que isso seja solicitado.

---

# 12. Testes

Sempre que uma alteração for feita:

1. Executar o projeto;
2. Testar a funcionalidade;
3. Verificar se funcionalidades anteriores continuam funcionando.

Para sistemas importantes, testar também:

- condição normal;
- condição inválida;
- interação repetida;
- reinício do jogo, quando aplicável.

---

# 13. Critério de sucesso do jogo

O jogo estará funcional quando um jogador conseguir:

```text
Iniciar o jogo
      ↓
Controlar personagem
      ↓
Explorar a escola
      ↓
Interagir com objetos
      ↓
Encontrar pistas
      ↓
Resolver puzzles
      ↓
Desbloquear áreas
      ↓
Responder desafios
      ↓
Chegar à saída
      ↓
Ver a tela de conclusão
```

Esse é o principal "Definition of Done" do projeto.

---

# 14. O que NÃO é prioridade

Não são prioridade neste momento:

- multiplayer;
- sistema de save complexo;
- inventário avançado;
- inteligência artificial de inimigos;
- NPCs complexos;
- sistema de diálogos sofisticado;
- gráficos 3D;
- física avançada;
- loja;
- monetização;
- online;
- suporte mobile;
- sistemas desnecessários para o Escape Room.

Se uma dessas ideias surgir, avaliar somente depois que o jogo principal estiver funcionando.

---

# 15. Prioridade de desenvolvimento

A ordem recomendada é:

### Fase 1 — Fundação

- Projeto Godot;
- Git;
- cena principal;
- player;
- movimento.

### Fase 2 — Gameplay básico

- colisões;
- interação;
- objetos;
- portas;
- itens.

### Fase 3 — Escape Room

- mapa;
- pistas;
- puzzles;
- perguntas;
- desbloqueios.

### Fase 4 — Integração

- conectar salas;
- progressão;
- condição de vitória;
- tela final.

### Fase 5 — Polimento

- arte;
- UI;
- áudio;
- efeitos;
- ajustes.

### Fase 6 — Testes

- jogar do início ao fim;
- encontrar bugs;
- corrigir;
- testar novamente;
- preparar apresentação.

---

# 16. Filosofia do projeto

O projeto deve seguir uma regra simples:

> **Primeiro fazer o jogo funcionar. Depois fazer o jogo bonito.**

Não precisamos criar o Escape Room mais complexo.

Precisamos criar um Escape Room que:

- funciona;
- é divertido;
- possui desafios;
- possui começo, meio e fim;
- demonstra o que aprendemos;
- pode ser apresentado sem depender de improvisação.

---

# 17. Estado atual

O repositório está no início do desenvolvimento.

Antes de assumir que alguma mecânica, sistema ou cena existe, a IA deve verificar o código atual.

**Não presumir que funcionalidades descritas neste README já foram implementadas.**

Este README descreve o objetivo e a arquitetura desejada, não necessariamente o estado atual do código.

---

## Resumo para agentes

Ao trabalhar neste projeto, siga estas regras:

```text
ENGINE:
Godot 4.x

TIPO:
Escape Room 2D escolar

OBJETIVO:
Jogo funcional do início ao fim

PRIORIDADE:
Gameplay > Integração > Polimento

CONTROLES:
Interação inicialmente com E

IA:
Ler antes de modificar
Alterar somente o necessário
Não reescrever o projeto
Não inventar funcionalidades
Testar depois de modificar
Explicar o que foi feito

NÃO FAZER:
Migrar para 3D
Adicionar complexidade desnecessária
Criar sistemas fake
Reescrever tudo

DEFINITION OF DONE:
O jogador consegue iniciar,
explorar,
interagir,
resolver puzzles,
desbloquear áreas
e escapar da escola.
```