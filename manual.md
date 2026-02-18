# Manual Técnico - Simulador de Caça-Níquel

## Estrutura do Código
- `validador_de_vitorias`: verifica linhas vencedoras.
- `giros_do_caca_niquel`: gera símbolos aleatórios.
- `print_caca_niquel`: exibe resultado em formato 3x3.
- `deposito`: coleta depósitos do jogador.
- `coleta_do_numero_de_linhas`: define número de linhas apostadas.
- `valor_da_aposta`: define valor da aposta por linha.
- `selecionar_opcao`: permite depositar ou refazer aposta.
- `giros`: mantém o loop das rodadas, validando saldo e apostas até que uma jogada seja realizada.
- `main`: executa e finaliza o software (loop principal do jogo).

## Fluxo
1. Depósito inicial
2. Escolha de linhas e aposta
3. Validação de saldo
4. Giro da máquina
5. Exibição de resultado
6. Atualização de saldo e loop das rodadas
7. Repetição ou saída
