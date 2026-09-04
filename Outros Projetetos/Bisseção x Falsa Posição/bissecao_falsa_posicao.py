
# Parâmetros físicos do problema
B = 20.0
Q = 5.0

def f(H):
    # Função principal f(H) = 0 derivada da equação de Manning
    return 0.471405*((20*H)**(5/3))/((20+2*H)**(2/3))-5.0

def calcular_velocidade(H):
    # U = Q/(B*H)
    return Q/(B*H)

def bissecao(Hl, Hu, tol=1e-6, max_iter=100):
    print("--- Método da Bisseção ---")
    if f(Hl) * f(Hu) >= 0:
        print("Erro: O intervalo inicial não contém mudança de sinal")
        return None

    for k in range(1, max_iter+1):
        Hr = (Hl+Hu)/2.0
        f_Hr = f(Hr)

        print(f"Iteração {k}: Hl = {Hl:.6f}, Hu = {Hu:.6f}, Hr = {Hr:.6f}, f(Hr) = {f_Hr:.6e}")

        if abs(f_Hr) < tol:
            print(f"-> Convergiu em {k} iterações. Profundidade H: {Hr:.6f} m\n")
            return Hr

        if f(Hl)*f_Hr < 0:
            Hu = Hr
        else:
            Hl = Hr

    print("O método atingiu o número máximo de iterações.\n")
    return Hr

def falsa_posicao(Hl, Hu, tol=1e-6, max_iter=100):
    print("--- Método da Falsa Posição ---")
    if f(Hl)*f(Hu)>=0:
        print("Erro: O intervalo inicial não contém mudança de sinal.")
        return None

    for k in range(1, max_iter+1):
        f_Hl = f(Hl)
        f_Hu = f(Hu)

        Hr = (Hl*f_Hu-Hu*f_Hl)/(f_Hu-f_Hl)
        f_Hr = f(Hr)

        print(f"Iteração {k}: Hl = {Hl:.6f}, Hu = {Hu:.6f}, Hr = {Hr:.6f}, f(Hr) = {f_Hr:.6e}")

        if abs(f_Hr) < tol:
            print(f"-> Convergiu em {k} iterações. Profundidade H = {Hr:.6f} m\n")
            return Hr

        if f_Hl*f_Hr < 0:
            Hu = Hr
        else:
            Hl = Hr

    print("O método atingiu o número máximo de iterações.\n")
    return Hr

# Execução conforme as estimativas fornecidas
H_l_inicial = 0.5
H_u_inicial = 1.0

H_bissecao = bissecao(H_l_inicial, H_u_inicial)
if H_bissecao:
    U_bissecao = calcular_velocidade(H_bissecao)
    print(f"Velocidade média (Bisseção): {U_bissecao:.6f} m/s\n")

H_falsa_pos = falsa_posicao(H_l_inicial, H_u_inicial)
if H_falsa_pos:
    U_falsa_pos = calcular_velocidade(H_falsa_pos)
    print(f"Velocidade média (Falsa Posição): {U_falsa_pos:.6f} m/s\n")
