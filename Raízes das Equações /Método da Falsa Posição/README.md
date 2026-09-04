# Calculadora de Raízes: Método da Falsa Posição

Este repositório contém um script em Python para encontrar raízes de equações não lineares utilizando o **Método da Falsa Posição** (também conhecido como *Regula Falsi*). É uma implementação prática ideal para a resolução de problemas numéricos nas áreas de ciências exatas e engenharias.

## Funcionalidades
- **Entrada Dinâmica:** O usuário pode digitar a equação matemática no terminal em tempo de execução.
- **Suporte a Funções Matemáticas:** Avaliação segura da string com suporte nativo às funções da biblioteca `math` do Python (como `sin(x)`, `cos(x)`, `exp(x)`, `log(x)`, etc.).
- **Parâmetros Customizáveis:** Definição interativa do intervalo inicial `[a, b]` e da tolerância de erro (`tol`).

## Pré-requisitos
- **Python 3.6** ou superior instalado na máquina.
- O código utiliza apenas a biblioteca padrão do Python, dispensando a instalação de pacotes externos como `numpy` ou `scipy` para a versão básica.

## Como Executar
1. Salve o código fornecido em um arquivo, por exemplo, `falsa_posicao.py`.
2. Abra o seu terminal (ou prompt de comando).
3. Navegue até o diretório onde o arquivo foi salvo.
4. Rode o comando:
   ```bash
   python falsa_posicao.py
   ```
5. Siga os prompts exibidos na tela para inserir a equação e os parâmetros.

### Exemplo de Uso
Ao executar o programa, você verá uma interação semelhante a esta:

```text
=== Calculadora: Método da Falsa Posição ===
Digite a equação em função de 'x' (ex: x**3 - 9*x + 3 ou cos(x) - x): x**3 - 9*x + 3
Limite inferior do intervalo (a): 0
Limite superior do intervalo (b): 1
Tolerância desejada (ex: 1e-6): 1e-4

--- Resultados ---
Raiz aproximada: 0.33760896
Iterações realizadas: 4
Erro final f(raiz): -2.57e-05
```

## Dicas de Sintaxe para as Equações
- **Potenciação:** Utilize `**` em vez de `^`. Exemplo: `x**2 - 4`.
- **Multiplicação:** O operador `*` é obrigatório. Exemplo: `2*x` em vez de `2x`.
- **Trigonometria e Exponenciais:** Chame diretamente a função. Exemplo: `sin(x) - exp(-x)`.

## Notas de Segurança
A implementação utiliza a função `eval()` com um dicionário de ambiente restrito. As variáveis embutidas (`__builtins__`) são desativadas para mitigar riscos de execução de comandos arbitrários no sistema.
