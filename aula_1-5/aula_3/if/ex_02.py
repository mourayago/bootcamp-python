temp = float(input("Qual a temperatura atual?"))
tier = ""


if temp < 18:
    print("Temperatura baixa")
    tier = "baixa"
elif temp >= 18 and temp <= 26:
    print("temperatura normal")
    tier = "normal"
else:
    print("temperatura alta")
    tier = "alta"

print(f"A temperatura está em {temp}, o ambiente está em temperatura {tier}")