edad = int(input("Por favor, ingresa tu edad: "))

if edad < 12:
    print("Eres un niño.")
elif 12 <= edad < 65:
    print("Eres un adulto.")
else:
    print("Eres una persona de la tercera edad.")