# 🎰 Simulador de Caça-Níquel em Python

Este projeto é um simulador de caça-níquel (slot machine) interativo via terminal, desenvolvido em Python. O jogador pode depositar créditos, escolher quantas linhas deseja apostar, definir o valor da aposta por linha e girar a máquina para tentar obter combinações vencedoras.

## 🚀 Funcionalidades
- Depósito inicial e adicional de créditos
- Escolha de número de linhas para apostar (até 3)
- Definição do valor da aposta por linha (com limites mínimo e máximo)
- Geração aleatória de símbolos em uma matriz 3x3
- Validação de vitórias por linha (símbolos iguais)
- Cálculo de ganhos com base nos valores dos símbolos
- Atualização automática do saldo após cada rodada
- Loop contínuo até o jogador decidir sair

## 🎮 Regras do Jogo
- O caça-níquel possui 3 linhas e 3 colunas.
- Os símbolos disponíveis são: `$`, `@`, `#`, `%`, com diferentes probabilidades e valores.
- O jogador aposta em até 3 linhas simultaneamente.
- Se todos os símbolos de uma linha forem iguais, o jogador ganha o valor do símbolo multiplicado pela aposta.

## 🧑‍💻 Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/KauaLasco/Slot-Machine-Simulator.git

2. Entrar na pasta do projeto:
   ```bash
   cd Slot-Machine-Simulator

3. Execute o programa em Python
   ```bash
   python src/main.py
  - Esse comando roda o arquivo principal do jogo que está dentro da pasta src/.
  - Se você estiver usando Linux/Mac e tiver o Python 3 instalado, pode ser necessário usar:
   ```bash
   python3 src/main.py
   ```

---

# 🎰 Slot Machine Simulator in Python

This project is an interactive slot machine simulator via terminal, developed in Python. The player can deposit credits, choose how many lines to bet on, set the bet value per line, and spin the machine to try to get winning combinations.

## 🚀 Features
- Initial and additional credit deposit
- Choice of number of lines to bet on (up to 3)
- Setting the bet value per line (with minimum and maximum limits)
- Random generation of symbols in a 3x3 matrix
- Validation of wins per line (matching symbols)
- Calculation of winnings based on symbol values
- Automatic balance update after each round
- Continuous loop until the player decides to quit

## 🎮 Game Rules
- The slot machine has 3 rows and 3 reels.
- The available symbols are: `$`, `@`, `#`, `%`, with different probabilities and values.
- The player bets on up to 3 lines simultaneously.
- If all the symbols on a line are the same, the player wins the value of the symbol multiplied by the bet.

## 🧑‍💻 How to Run
1. Clone the repository:
```bash
git clone https://github.com/KauaLasco/Slot-Machine-Simulator.git
```

2. Enter the project folder:
```bash
cd Slot-Machine-Simulator
```

3. Run the Python program:
```bash
python src/main.py
```
- This command runs the main game file located in the src/ folder.
- If you are using Linux/Mac and have Python 3 installed, you may need to use:
```bash
python3 src/main.py
```
