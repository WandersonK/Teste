# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

num = 10000

while num > 9999 or num < 0:
    num = int(input("Informe um número entre 0 e 9999: "))


print(f"unidade: {num % 10}")
print(f"dezena: {(num // 10) % 10}")
print(f"centena: {(num // 100) % 10}")
print(f"milhar: {(num // 1000) % 10}")
