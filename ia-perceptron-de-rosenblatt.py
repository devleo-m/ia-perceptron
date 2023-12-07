import random #Pesos e bias com valores aleatórios

def step_function(x):
    return 1 if x >= 0 else -1

taxa_aprendizado = 0.01 # Taxa de aprendizado

pesos = [random.uniform(0, 1) for _ in range(7)]
bias = random.uniform(0, 1)

ru = [3, 2, 3, 5, 6, 0, 9] # Meu RU
dados_treinamento = [ # Dados de treinamento expandidos
    (ru, 1),
    ([1, 3, 1, 4, 5, 6, 7], -1),
    ([0, 0, 0, 0, 0, 2, 0], -1),
    ([1, 1, 1, 1, 1, 3, 1], -1),
    ([2, 4, 2, 6, 2, 4, 8], -1),
    ([4, 3, 2, 4, 5, 5, 6], -1),
    ([5, 1, 4, 3, 3, 6, 0], -1),
    ([0, 0, 0, 0, 0, 7, 5], -1),
    ([6, 1, 2, 2, 4, 8, 3], -1),
    ([7, 4, 5, 7, 7, 9, 8], -1),
    ([8, 3, 6, 8, 8, 2, 7], -1),
    ([9, 3, 7, 9, 9, 1, 4], -1),
    ([1, 1, 2, 4, 5, 6, 8], -1),
    ([1, 3, 2, 4, 5, 6, 0], -1),
    ([2, 3, 4, 4, 5, 7, 8], -1),
    ([0, 0, 0, 0, 0, 2, 1], -1),
    ([4, 4, 4, 4, 5, 1, 0], -1),
    ([1, 1, 1, 1, 1, 1, 1], -1),
    ([0, 0, 0, 0, 0, 1, 0], -1),
    ([2, 1, 2, 2, 2, 2, 2], -1),
    ([4, 4, 4, 4, 4, 4, 4], -1),
    ([5, 5, 5, 4, 5, 5, 5], -1),
    ([6, 6, 6, 6, 7, 6, 6], -1),
    ([7, 7, 7, 7, 7, 7, 7], -1),
    ([8, 8, 8, 8, 8, 8, 8], -1),
    ([9, 9, 9, 9, 9, 9, 8], -1),
    ([1, 1, 3, 4, 5, 6, 8], -1),
    ([2, 3, 4, 4, 7, 7, 8], -1),
    ([5, 4, 4, 2, 1, 1, 0], -1),
    ([0, 1, 0, 1, 0, 1, 0], -1),
    ([0, 4, 2, 4, 3, 4, 3], -1),
    ([6, 7, 8, 9, 0, 1, 2], -1),
    ([1, 0, 0, 0, 0, 1, 0], -1),
    ([5, 3, 5, 2, 5, 2, 5], -1),
    ([5, 5, 2, 2, 5, 5, 2], -1),
    ([4, 4, 2, 2, 4, 4, 2], -1),
    ([6, 6, 2, 3, 7, 6, 3], -1),
    ([8, 8, 4, 4, 8, 8, 4], -1),
    ([2, 3, 2, 2, 3, 3, 2], -1),
    ([7, 7, 2, 3, 7, 7, 3], -1),
    ([9, 9, 4, 4, 9, 9, 4], -1),
    ([7, 7, 2, 2, 7, 7, 2], -1),
    ([1, 3, 2, 4, 4, 6, 6], -1),
    ([4, 4, 2, 3, 3, 4, 4], -1),
    ([5, 5, 4, 4, 4, 4, 5], -1),
    ([6, 6, 5, 4, 5, 5, 6], -1),
    ([7, 7, 6, 6, 7, 6, 7], -1),
    ([8, 8, 7, 7, 7, 7, 8], -1),
    ([9, 9, 8, 8, 8, 8, 8], -1),
    ([4, 3, 1, 1, 1, 1, 2], -1),
    ([2, 3, 1, 2, 3, 1, 2], -1),
    ([4, 4, 2, 3, 4, 2, 3], -1),
    ([1, 1, 2, 2, 1, 3, 2], -1),
    ([5, 5, 5, 1, 5, 5, 1], -1),
    ([6, 6, 6, 6, 6, 6, 2], -1),
    ([7, 7, 7, 7, 7, 7, 3], -1),
    ([8, 8, 8, 8, 8, 8, 4], -1),
    ([9, 9, 9, 9, 9, 9, 5], -1),
    ([1, 1, 2, 1, 1, 2, 2], -1),
    ([2, 1, 2, 3, 3, 3, 4], -1),
    ([4, 3, 2, 1, 0, 1, 0], -1),
    ([4, 3, 4, 3, 3, 3, 0], -1),
    ([0, 0, 1, 1, 2, 2, 3], -1),
    ([0, 1, 4, 6, 8, 2, 2], -1),
    ([0, 1, 2, 3, 4, 5, 6], -1),
    ([6, 5, 4, 3, 2, 1, 0], -1),
    ([1, 4, 7, 4, 1, 4, 7], -1),
    ([1, 1, 1, 1, 1, 1, 0], -1),
    ([2, 3, 1, 1, 2, 2, 0], -1),
    ([2, 3, 4, 3, 0, 1, 0], -1),
    ([7, 0, 7, 0, 7, 1, 7], -1),
    ([0, 0, 1, 0, 1, 1, 1], -1),
    ([1, 0, 0, 0, 1, 1, 0], -1),
    ([2, 0, 0, 0, 2, 1, 0], -1),
    ([1, 0, 1, 0, 1, 1, 1], -1),
    ([1, 1, 1, 2, 1, 2, 1], -1),
    ([2, 1, 2, 1, 3, 1, 3], -1),
    ([2, 3, 2, 1, 1, 1, 0], -1),
    ([2, 0, 2, 0, 3, 2, 3], -1),
    ([2, 0, 0, 3, 0, 1, 3], -1),
    ([3, 2, 3, 5, 6, 0, 9], 1),
]

# Treinamento
epocas = 10000

for _ in range(epocas):
    erro_total = 0  #Variável para controlar o erro total durante o treinamento
    for entrada, desejado in dados_treinamento:
        soma_ponderada = sum(w * x for w, x in zip(pesos, entrada)) + bias # Calcula a soma ponderada
        previsto = step_function(soma_ponderada) # Aplica a função de ativação degrau
        erro = desejado - previsto # Calcula o erro
        erro_total += erro  # Acumula o erro total durante o treinamento
        for i in range(len(pesos)):
            pesos[i] += taxa_aprendizado * erro * entrada[i] # Atualiza os pesos
        bias += taxa_aprendizado * erro # Atualiza o bias
    if erro_total == 0:
        break  # Finaliza o treinamento se não houver erro

# Teste
################|||||||||||||||||||||##############################################################################
entrada_teste = [3, 2, 3, 5, 6, 0, 9]  # Entrada dos valores para o teste [OBS: É aqui que alteramos os numeros] :P
################|||||||||||||||||||||##############################################################################

soma_ponderada = sum(w * x for w, x in zip(pesos, entrada_teste)) + bias # Calcula a soma ponderada para o teste
resultado = step_function(soma_ponderada) # Aplica a função de ativação degrau

if resultado == 1: # Se o resultado for igual a 1 vai ser printado o valor 1
    print("1")
else: # Senão for igual a 1 vai ser printado -1
    print("0")
