
import numpy as np
import matplotlib.pyplot as plt

def bairstow_step(a, r, s, tol=1e-5, max_iter=100):
    """
    Executa iterações do Método de Bairstow para encontrar um fator quadrático (x^2 - rx - s).
    a: Lista ou array de coeficientes ordenados do menor para o maior grau [a_0, a_1, ..., a_n]
    """
    n = len(a) - 1 # O grau do polinômio é o tamanho do vetor de coeficientes menos 1
    
    # Criamos os vetores b e c com o mesmo tamanho dos coeficientes originais
    b = np.zeros(n + 1)
    c = np.zeros(n + 1)
    
    for iter_count in range(max_iter):
        # 1. Primeira deflação (Relação de recorrência para os b_i)
        b[n] = a[n]
        b[n-1] = a[n-1] + r * b[n]
        for i in range(n-2, -1, -1):
            b[i] = a[i] + r * b[i+1] + s * b[i+2]
            
        # 2. Segunda deflação para Derivadas Parciais (c_i)
        c[n] = b[n]
        c[n-1] = b[n-1] + r * c[n]
        for i in range(n-2, 0, -1): # c0 não é necessário para o cálculo, então paramos em 1
            c[i] = b[i] + r * c[i+1] + s * c[i+2]
            
        # 3. Montagem e resolução do sistema linear 2x2 via Regra de Cramer
        # Equações: c1*dr + c2*ds = -b0
        #           c2*dr + c3*ds = -b1
        det = c[1] * c[3] - c[2] ** 2
        
        if det == 0:
            # Matriz singular (falha na iteração), aborta a tentativa
            return r, s, b, max_iter 
            
        dr = (-b[0] * c[3] - (-b[1]) * c[2]) / det
        ds = (c[1] * (-b[1]) - c[2] * (-b[0])) / det
        
        # Atualização de r e s
        r += dr
        s += ds
        
        # 4. Critério de parada (Erro Relativo em %)
        tol_r = abs(dr / r) if r != 0 else abs(dr)
        tol_s = abs(ds / s) if s != 0 else abs(ds)
        
        if tol_r < tol and tol_s < tol:
            return r, s, b, iter_count + 1
            
    return r, s, b, max_iter

def get_roots_from_quadratic(r, s):
    """Calcula as duas raízes a partir do fator (x^2 - rx - s = 0)"""
    delta = r**2 + 4*s
    if delta > 0:
        x1 = (r + np.sqrt(delta)) / 2
        x2 = (r - np.sqrt(delta)) / 2
        return [x1, x2]
    elif delta == 0:
        return [r / 2, r / 2]
    else:
        real_part = r / 2
        imag_part = np.sqrt(-delta) / 2
        return [complex(real_part, imag_part), complex(real_part, -imag_part)]

def bairstow_full(a, r0=1.0, s0=1.0, tol=1e-5):
    """Aplica deflações sucessivas para encontrar todas as raízes do polinômio"""
    roots = []
    a_curr = np.array(a, dtype=float)
    
    # Enquanto o polinômio resultante for de grau >= 3 (tamanho >= 4)
    while len(a_curr) > 3:
        r, s, b, iters = bairstow_step(a_curr, r0, s0, tol)
        roots.extend(get_roots_from_quadratic(r, s))
        # O novo polinômio assume os coeficientes de b_2 até b_n.
        # Como o array no Python é indexado de 0, b[2:] fará exatamente esse fatiamento
        a_curr = b[2:] 
        
    # Se sobrou um polinômio de grau 2 (tamanho == 3)
    if len(a_curr) == 3:
        # P(x) = a_2*x^2 + a_1*x + a_0 = 0 -> Dividindo por a_2: x^2 + (a_1/a_2)x + (a_0/a_2) = 0
        r_final = -a_curr[1] / a_curr[2]
        s_final = -a_curr[0] / a_curr[2]
        roots.extend(get_roots_from_quadratic(r_final, s_final))
    
    # Se sobrou um polinômio de grau 1 (tamanho == 2)
    elif len(a_curr) == 2:
        # P(x) = a_1*x + a_0 = 0 -> x = -a_0/a_1
        roots.append(-a_curr[0] / a_curr[1])
        
    return roots

def gerar_fractal_bairstow(a, resolucao=300, r_lim=(-3, 3), s_lim=(-3, 3)):
    """Varre o plano r0, s0 e gera o fractal baseado no número de iterações"""
    print("\n--- Gerando Fractal de Bairstow (Pode levar alguns segundos...) ---")
    r_vals = np.linspace(r_lim[0], r_lim[1], resolucao)
    s_vals = np.linspace(s_lim[0], s_lim[1], resolucao)
    
    fractal = np.zeros((resolucao, resolucao))
    max_iteracoes_permitidas = 50
    
    for i, s0 in enumerate(s_vals):
        for j, r0 in enumerate(r_vals):
            _, _, _, iters = bairstow_step(a, r0, s0, max_iter=max_iteracoes_permitidas)
            # Se atingiu max_iter, consideramos divergência e marcamos como 0 
            fractal[i, j] = iters if iters < max_iteracoes_permitidas else 0

    plt.figure(figsize=(8, 6))
    plt.imshow(fractal, extent=[r_lim[0], r_lim[1], s_lim[0], s_lim[1]], 
               origin='lower', cmap='nipy_spectral')
    plt.colorbar(label='Iterações para Convergência')
    plt.title('Fractal de Bairstow - Polinômio APC2')
    plt.xlabel('$r_0$ inicial')
    plt.ylabel('$s_0$ inicial')
    plt.show()

# ====================================================================
# EXECUÇÃO E TESTES SOLICITADOS NO PPC2
# ====================================================================
if __name__ == "__main__":
    
    # 1. VALIDAÇÃO: Polinômio de 7ª Ordem
    print("--- Validação: Polinômio de 7ª Ordem ---")
    # Construindo um polinômio a partir de raízes conhecidas
    raizes_conhecidas = [1, -1, 2, -2, 3, complex(-1, 1), complex(-1, -1)]
    poly_7_numpy = np.poly(raizes_conhecidas)
    # Importante: np.poly retorna do maior grau para o menor [a7, a6, ..., a0].
    # Nós precisamos reverter para [a0, a1, ..., a7]
    a_validacao = poly_7_numpy[::-1].real
    
    # Teste de raízes com aproximação inicial
    raizes_encontradas = bairstow_full(a_validacao, r0=0.5, s0=0.5)
    
    print("Raízes Conhecidas Originais:")
    for raiz in raizes_conhecidas: print(f"  {np.round(raiz, 4)}")
    print("\nRaízes Encontradas pelo Método de Bairstow:")
    # Ordenamos a impressão pelo valor real para facilitar a visualização de que as raízes batem
    for raiz in sorted(raizes_encontradas, key=lambda x: x.real): print(f"  {np.round(raiz, 4)}")


    # 2. SOLUÇÃO APC2: Sistema de Múltiplos Graus de Liberdade
    print("\n--- Solução do Polinômio da APC2 ---")
    # P(λ) = 100 + 40λ + 34λ^2 + 6λ^3 + 1λ^4 = 0
    a_apc2 = [100.0, 40.0, 34.0, 6.0, 1.0]
    
    autovalores = bairstow_full(a_apc2, r0=1.0, s0=-1.0)
    
    print("Autovalores do Sistema (Raízes):")
    for lam in autovalores:
        print(f"  λ = {np.round(lam, 5)}")

    # 3. INTERPRETAÇÃO FÍSICA
    print("\n--- Interpretação Física ---")
    estavel = all(lam.real < 0 for lam in autovalores)
    oscilatorio = any(abs(lam.imag) > 1e-5 for lam in autovalores)
    
    print(f"Estabilidade: O sistema é {'ESTÁVEL' if estavel else 'INSTÁVEL'} " 
          f"pois a parte real das raízes é {'negativa (as vibrações decaem)' if estavel else 'positiva em pelo menos um polo'}.")
    if oscilatorio:
        print("Comportamento: O sistema apresenta resposta OSCILATÓRIA (subamortecida), "
              "evidenciada pela presença de parte imaginária não nula nos autovalores (frequências naturais do sistema).")

    # 4. GERAÇÃO DO FRACTAL
    gerar_fractal_bairstow(a_apc2, resolucao=300)
