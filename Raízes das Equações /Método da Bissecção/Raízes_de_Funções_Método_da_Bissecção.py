{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNxBMw5OiaLUT56kXwEZSYl",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rafaelmarques323839-dev/Programa-para-Casa-PPC-/blob/main/Ra%C3%ADzes%20das%20Equa%C3%A7%C3%B5es%20/M%C3%A9todo%20da%20Bissec%C3%A7%C3%A3o/Ra%C3%ADzes_de_Fun%C3%A7%C3%B5es_M%C3%A9todo_da_Bissec%C3%A7%C3%A3o.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FC24FHZ0h5Yi",
        "outputId": "5f3b6702-4987-40e9-bcd6-ee9830cc46ed"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--- Encontrar Raízes pelo Método da Bissecção\n",
            "Dica: Use a sintaxe do Python. Ex: para x³, digite x**3. Para cosseno, digite math.cos(x).\n",
            "Digite a equação (em função de 'x'): math.sin(x) - x/2\n",
            "Digite o início do intervalo (a): 1\n",
            "Digite o fim do intervalo (b): 2\n",
            "Digite a tolerância desejada (ex: 0.0001 ou 1e-4): 0.0000000001\n",
            "\n",
            "--- Resultados ---\n",
            "Raiz aproximada: 1.89549427\n",
            "Iterações realizadas: 33\n"
          ]
        }
      ],
      "source": [
        "import math\n",
        "\n",
        "def bisseccao(f, a, b, tol, max_iter=1000):\n",
        "  \"\"\"\n",
        "    Encontra a raiz de uma função f no intervalo [a, b] usando o método da bissecção.\n",
        "    \"\"\"\n",
        "  # Verifica se os sinais de f(a) e f(b) são opostos (Teorema de Bolzano)\n",
        "  if f(a)*f(b)>=0:\n",
        "    raise ValueError (\"O intervalo é inválido. A função deve ter sinais opostos em 'a' e 'b'.\")\n",
        "\n",
        "  iteracao = 0\n",
        "  # O laço continua enquanto a estimativa do erro for maior que a tolerância\n",
        "  while (b-a)/2.0>tol and iteracao<max_iter:\n",
        "    c = (a+b)/2.0 # Ponto médio\n",
        "\n",
        "    # Se encontrou a raiz exata\n",
        "    if f(c)==0:\n",
        "      break\n",
        "\n",
        "    # Define o novo subintervalo\n",
        "    if f(a)*f(c)<0:\n",
        "      b=c\n",
        "    else:\n",
        "      a=c\n",
        "\n",
        "    iteracao += 1\n",
        "\n",
        "  # Retorna o ponto médio do intervalo final e o número de iterações\n",
        "  return (a+b)/2.0, iteracao\n",
        "\n",
        "if __name__==\"__main__\":\n",
        "  print(\"--- Encontrar Raízes pelo Método da Bissecção\")\n",
        "  print(\"Dica: Use a sintaxe do Python. Ex: para x³, digite x**3. Para cosseno, digite math.cos(x).\")\n",
        "\n",
        "  # Recebe a equação como string\n",
        "  equacao_str = input(\"Digite a equação (em função de 'x'): \")\n",
        "\n",
        "  # Cria uma função avaliável usando lambda e eval\n",
        "  f = lambda x: eval(equacao_str)\n",
        "\n",
        "  try:\n",
        "    # Recebe os parâmetros do usuário\n",
        "    a = float(input(\"Digite o início do intervalo (a): \"))\n",
        "    b = float(input(\"Digite o fim do intervalo (b): \"))\n",
        "    tol = float(input(\"Digite a tolerância desejada (ex: 0.0001 ou 1e-4): \"))\n",
        "\n",
        "    # Executa o cálculo\n",
        "    raiz, iteracoes = bisseccao(f, a, b, tol)\n",
        "\n",
        "    print(\"\\n--- Resultados ---\")\n",
        "    print(f\"Raiz aproximada: {raiz:.8f}\")\n",
        "    print(f\"Iterações realizadas: {iteracoes}\")\n",
        "\n",
        "  except ValueError as ve:\n",
        "    print(f\"\\nErro de Valor: {ve}\")\n",
        "  except Exception as e:\n",
        "    print(f\"\\nOcorreu um erro ao processar a função: Verifique se a sintaxe da equação está correta. (Erro original: {e})\")"
      ]
    }
  ]
}