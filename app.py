# Pedindo as notas ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calculando a média
media = (nota1 + nota2) / 2

# Exibindo o resultado
print(f"Sua média final foi: {media}")

# Estrutura de decisão 
if media >= 6:
    print("Parabéns! Você foi aprovado.")
else:
    print("Continue estudando, você ficou de recuperação.")
