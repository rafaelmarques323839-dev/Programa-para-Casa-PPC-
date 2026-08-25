# PPC 01 - Integração Numérica do Movimento de Sedimentação (RK4)

## Resumo Operacional
Este algoritmo computacional realiza a simulação unidimensional da dinâmica de uma partícula esférica sedimentando sob a ação da gravidade em um fluido viscoso, um problema clássico no estudo de fenômenos de transporte. O script utiliza o método numérico de Runge-Kutta de quarta ordem (RK4) para resolver a equação diferencial ordinária (EDO) que governa o movimento em dois regimes físicos distintos:
1. **Regime Laminar (Stokes):** Onde o escoamento ao redor da esfera dita um arrasto puramente linear e dependente da viscosidade.
2. **Regime Inercial (Oseen):** Onde correções inerciais são inseridas no balanço de forças, resultando em um arrasto não-linear quadrático.

## Dicionário de Variáveis
Abaixo estão as principais variáveis e parâmetros de estado utilizados no código-fonte:

| Variável / Parâmetro | Significado Físico / Matemático | Unidade | Tipo de Dado |
| :--- | :--- | :--- | :--- |
| `St` | Número de Stokes (razão de tempos de relaxação e convecção) | Adimensional | `float` |
| `Re_s` | Número de Reynolds da partícula | Adimensional | `float` |
| `t` | Tempo instantâneo da simulação | Adimensional | `float` |
| `v` | Velocidade vertical (z) da esfera | Adimensional | `float` |
| `h` | Passo temporal de integração ($h = \Delta t$) | Adimensional | `float` |
| `T_MAX` | Tempo máximo para interrupção do laço de simulação | Adimensional | `float` |
| `k1`, `k2`, `k3`, `k4`| Coeficientes iterativos de inclinação do RK4 | Adimensional | `float` |
| `tempos` | Vetor de armazenamento do histórico da variável de estado temporal | Adimensional | `list` |
| `velocidades` | Vetor de armazenamento do histórico da variável de estado da velocidade | Adimensional | `list` |

## Dependências e Bibliotecas
Respeitando as restrições da disciplina de Cálculo Numérico Aplicado para evitar funções "caixa-preta", o código baseia-se estritamente na linguagem nativa e em bibliotecas auxiliares essenciais:
* `math` (Nativa do Python): Utilizada para o cálculo de exponenciais e raízes quadradas das soluções analíticas.
* `matplotlib.pyplot` (Externa): Empregada estritamente para a geração e visualização comparativa dos gráficos de saída.

## Especificação de I/O (Entradas e Saídas)
* **Inputs:** O modelo numérico é alimentado através de parâmetros \textit{hardcoded} definidos no bloco de execução global do script (linha 53 em diante). Os parâmetros configuráveis incluem `T_MAX`, `H_PADRAO`, `St` e `Re_s`.
* **Outputs:** O script processa a EDO e gera, em tempo de execução, quatro gráficos (janelas independentes) que plotam os vetores resultantes da integração em comparação com as soluções de referência exatas.

## Procedimentos de Execução
Para executar a simulação e gerar as análises gráficas, abra o terminal no diretório onde o script está localizado e digite:

```bash
python main.py
