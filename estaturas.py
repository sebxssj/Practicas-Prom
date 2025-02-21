
suma_estaturas=0
contador_personas=0
while True:
    estatura=float( input("Ingresa la estatura (O presiona Enter para terminar)"))
    if estatura == "":
        break
    suma_estaturas += estatura
    contador_personas += 1
    if estatura > 0:
        promedio= suma_estaturas / contador_personas
    else:
        print ("No se registaron estaturas")
        break
print(f"La estatura promedio es: {promedio} metros.")