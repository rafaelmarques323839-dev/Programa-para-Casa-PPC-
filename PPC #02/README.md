# PPC 02 - Determinação de Raízes de Polinômios (Método de Bairstow)

## 1. Resumo Operacional
Esta prática implementa computacionalmente o Método de Bairstow para a extração de raízes reais e complexas de polinômios de grau elevado. O algoritmo baseia-se na deflação polinomial sucessiva por um fator quadrático genérico $(x^2 - rx - s)$, cujos coeficientes $r$ e $s$ são otimizados iterativamente via método de Newton-Raphson. Do ponto de vista físico, o algoritmo soluciona a equação característica de um sistema dinâmico massa-mola-amortecedor com 2 graus de liberdade ($N=2$), permitindo analisar a estabilidade e as frequências naturais de oscilação do sistema através dos autovalores encontrados.

## 2. Dicionário de Variáveis
Abaixo estão mapeadas as principais variáveis de estado e parâmetros utilizados no script principal `ppc2_bairstow.py`:

| Variável no Script | Significado Físico / Matemático | Unidade | Tipo de Dado |
| :--- | :--- | :--- | :--- |
| `a` | Array contendo os coeficientes originais do polinômio na forma $a_0 + a_1\lambda + ... + a_n\lambda^n$. | Adimensional | `array (float)` |
| `r`, `s` | Parâmetros de iteração que compõem o fator quadrático divisor inicial. | Adimensional | `float` |
| `b`, `c` | Coeficientes obtidos na 1ª e 2ª deflações sintéticas, respectivamente. `c` fornece as derivadas parciais. | Adimensional | `array (float)` |
| `dr`, `ds` | Incrementos $\Delta r$ e $\Delta s$ calculados pelo sistema linear (Regra de Cramer). | Adimensional | `float` |
| `tol` | Tolerância percentual estabelecida como critério de convergência do método. | % (percentual) | `float` |
| `max_iter` | Critério de parada de segurança para o número máximo de iterações permitidas. | Adimensional | `int` |
| `resolucao` | Resolução da malha bidimensional $N \times N$ gerada para o plot do fractal. | Pixels | `int` |
| `fractal` | Matriz bidimensional que armazena a quantidade de iterações até a convergência para cada coordenada $(r_0, s_0)$. | Adimensional | `array (int)` |

## 3. Dependências e Bibliotecas
O código foi construído priorizando a lógica numérica "sob o capô". As bibliotecas utilizadas restringem-se a:
* **Python 3.x:** Ambiente de execução padrão.
* **NumPy:** Utilizada exclusivamente para inicialização e manipulação de vetores/matrizes de dados, sem invocar resolvedores nativos de raízes para o método.
* **Matplotlib (`pyplot`):** Utilizada estritamente para a geração gráfica e renderização do Mapa de Convergência (Fractal de Bairstow).

## 4. Especificação de I/O (Entradas e Saídas)
* **Inputs (Entradas):** 
  * Os coeficientes da equação característica da APC2 são alimentados diretamente no script através do vetor `a_apc2 = [100.0, 40.0, 34.0, 6.0, 1.0]`. 
  * Os limites do plano cartesiano para o fractal são passados como tuplas de argumentos `r_lim` e `s_lim`.
* **Outputs (Saídas):**
  * **Console (Terminal):** Impressão estruturada contendo o comparativo de raízes da validação, os autovalores obtidos para o problema da APC2 e uma análise automática sobre a estabilidade do sistema físico.
  * **Gráfico (Visualização):** Renderização de uma janela interativa contendo o mapa de calor iterativo (Fractal de Bairstow) plotado sobre o espaço de parâmetros $r_0 \times s_0$.

## 5. Procedimentos de Execução
Para executar o algoritmo, certifique-se de estar no diretório raiz desta PPC e de possuir as bibliotecas instaladas. No terminal do seu sistema operacional, execute o seguinte comando:

```bash
# Executa o script e imprime os resultados da validação e da APC no console, finalizando com a plotagem gráfica.
python ppc_2.py
