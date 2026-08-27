# Método da Bissecção em Python

Este repositório contém um script interativo em Python para encontrar raízes reais de equações não lineares utilizando o **Método da Bissecção**. 

O método numérico é ideal para resolver equações implícitas onde a variável de interesse não pode ser isolada analiticamente — uma situação comum na resolução de problemas práticos de engenharia, como o cálculo do fator de atrito em mecânica dos fluidos ou em análises de transferência de calor e termodinâmica.

## 🚀 Funcionalidades
- **Interatividade:** O usuário insere a equação, o intervalo inicial e a tolerância de erro diretamente no terminal.
- **Validação Matemática:** O script verifica automaticamente o Teorema de Bolzano, garantindo que o intervalo fornecido possui sinais opostos ($f(a) \times f(b) < 0$).
- **Suporte a Funções Nativas:** Integração com a biblioteca `math`, permitindo o uso de funções trigonométricas (`math.sin`, `math.cos`), exponenciais (`math.exp`), entre outras.

## 📋 Pré-requisitos
- Python 3.x instalado na máquina.
- Nenhuma biblioteca externa adicional é necessária para o funcionamento básico.

## 🔧 Como utilizar

1. Salve o arquivo principal em sua máquina (ex: `bisseccao.py`).
2. Abra o terminal e navegue até a pasta onde o arquivo está salvo.
3. Execute o script com o comando:
   ```bash
   python bisseccao.py
   ```
4. Siga as instruções na tela:
   - **Equação:** Escreva usando a sintaxe do Python (ex: `x**3 - 9*x + 3` ou `math.cos(x) - x`).
   - **Intervalo [a, b]:** Escolha valores de `a` e `b` onde a função cruza o eixo X.
   - **Tolerância:** Defina a precisão desejada para a convergência (ex: `1e-6` ou `0.0001`).

## 💡 Exemplo de Uso
Se quisermos encontrar a raiz da função $f(x) = x^3 - x - 2$ no intervalo $[1, 2]$ com tolerância de $0.001$:

```text
Digite a equação (em função de 'x'): x**3 - x - 2
Digite o início do intervalo (a): 1
Digite o fim do intervalo (b): 2
Digite a tolerância desejada (ex: 0.0001 ou 1e-4): 0.001

--- Resultados ---
Raiz aproximada: 1.52050781
Iterações realizadas: 10
```

## ⚙️ Estrutura do Código
A função principal `bisseccao(f, a, b, tol)` recebe uma função `lambda`, os limites numéricos e a tolerância de parada. O laço `while` divide o subintervalo ao meio a cada iteração até que o erro de aproximação satisfaça a precisão exigida, convergindo para a solução de forma bastante estável.
