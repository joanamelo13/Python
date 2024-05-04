# encoding: utf-8
from decimal import Decimal, ROUND_HALF_UP

print("Olá! Seja bem vindo ao programa responsável por calcular seu IMC! \n \n Para isso iremos precisar do seu peso e sua altura \n")

weight = float(input("Informe seu peso: \n"))
height = float(input("Informe sua altura: \n"))
imc = float(weight / pow(height, 2))

if round(imc,2) < 18.50: 
    print(f"Você encontra-se abaixo do peso. O seu IMC é: {imc:.2f}")
elif round(round(imc,2) >= 18.50,2) & round(round(imc,2) <= 24.99):
    print(f"Você encontra-se no peso normal. O seu IMC é: {imc:.2f}")
elif round(round(imc,2)>= 25.00,2) & round(round(imc,2) <= 29.99,2):
    print(f"Você encontra-se acima do peso. O seu IMC é: {imc:.2f}")
else:
    print(f"Você encontra-se obeso. O seu IMC é: {imc:.2f}")
