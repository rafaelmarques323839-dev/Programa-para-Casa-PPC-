# PPC 02 - Resolução de Equações Não Lineares: Métodos da Bisseção e da Falsa Posição
**Universidade de Brasília**
**Cálculo Numérico Aplicado**

## Resumo Operacional
O algoritmo implementa os métodos numéricos intervalares da Bisseção e da Falsa Posição para encontrar a raiz de uma função não linear que modela o escoamento uniforme de água em um canal aberto retangular. O problema físico consiste em determinar a profundidade $H$ da lâmina d'água para uma vazão volumétrica prescrita $Q$, utilizando a equação empírica de Manning acoplada à geometria transversal do canal. A partir da profundidade calculada em estado de equilíbrio, o algoritmo computa a velocidade média $U$ do escoamento.

## Dicionário de Variáveis
* `B`: Largura da base do canal retangular | Unidade: $m$ | Tipo: `float`
* `Q`: Vazão volumétrica de projeto no escoamento | Unidade: $m^3/s$ | Tipo: `float`
* `Hl`: Limite inferior do intervalo de busca que contém a raiz | Unidade: $m$ | Tipo: `float`
* `Hu`: Limite superior do intervalo de busca que contém a raiz | Unidade: $m$ | Tipo: `float`
* `Hr`: Aproximação atual iterativa para a profundidade da lâmina d'água | Unidade: $m$ | Tipo: `float`
* `f(H)`: Função residual não linear derivada da equação de Manning | Unidade: $m^3/s$ | Tipo: `function`
* `tol`: Tolerância de erro utilizada como critério de parada ($10^{-6}$) | Unidade: Adimensional | Tipo: `float`
* `max_iter`: Número máximo de iterações permitidas para evitar laços infinitos | Unidade: Adimensional | Tipo: `int`[cite: 3]
* `U`: Velocidade média do fluido na seção transversal | Unidade: $m/s$ | Tipo: `float`[cite: 3]

## Dependências e Bibliotecas
A implementação foi desenvolvida inteiramente com Python puro (padrão embutido), dispensando o uso de bibliotecas de terceiros como `numpy` ou `scipy`. Isso atende às restrições da matéria, reforçando a construção manual da lógica de cálculo numérico utilizando controle de fluxo básico e operações algébricas fundamentais.

## Especificação de I/O (Entradas e Saídas)
* **Inputs:** A alimentação do modelo é feita via variáveis declaradas diretamente no código-fonte (*hardcoded*). Os parâmetros do canal ($B=20$, $Q=5$, $S=0,0002$, $n=0,03$) estão incorporados na inicialização da função objetivo de vazão residual e na fórmula de velocidade[cite: 3]. 
* **Outputs:** O programa retorna informações textuais diretamente no terminal (console). Durante a execução, ele imprime o passo a passo iterativo de cada método numérico (número da iteração $k$, limites atuais $H_l$ e $H_u$, raiz aproximada $H_r$ e o valor da função $f(H_r)$). Ao atingir a tolerância estipulada, ele retorna os valores finais em ponto flutuante da profundidade $H$ e da velocidade média $U$ correspondente[cite: 3].

## Procedimentos de Execução
Para executar a aplicação, certifique-se de ter o Python instalado na máquina.
1. Abra um interpretador de linha de comando ou terminal.
2. Navegue até o diretório onde o script está armazenado.
3. Digite o seguinte comando e pressione ENTER:
   ```bash
   python nome_do_arquivo.py
