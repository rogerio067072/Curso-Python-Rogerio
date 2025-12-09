# imc_calculator.py
# Projeto Especial M2: Calculadora Simples

# 1. Entrada de Dados (Variáveis)
# Vamos definir as variáveis peso (em kg) e altura (em metros).

peso_kg = 75.5    # Exemplo de peso. É um objeto do tipo float.
altura_m = 1.89   # Exemplo de altura. É um objeto do tipo float.

# 2. Cálculo do IMC
# Fórmula do IMC: peso / (altura * altura)

# O uso de parênteses garante que a multiplicação (altura ** 2) seja feita primeiro
# antes da divisão, seguindo a ordem correta da fórmula.
imc = peso_kg / (altura_m ** 2)

# 3. Saída do Resultado (Função print())

# O print() aceita múltiplos argumentos separados por vírgula.
print("--- Calculadora IMC ---")
print("Peso utilizado (kg):", peso_kg)
print("Altura utilizada (m):", altura_m)
print("Seu Índice de Massa Corporal (IMC) é:", imc) 
# Note que o resultado é um float devido à divisão.

# Conhecimento Extra: Como formatar a saída para 2 casas decimais (Avançado!)
print(f"IMC formatado: {imc:.2f}")