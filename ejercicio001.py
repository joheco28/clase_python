def calcular(total):
    r=total * 0.13
    return round(r,2)

if __name__ == "__main__":
    n = input("escribe tu nombre ")
    t = float(input("escrbe tus ventas del mes "))
    c = calcular(t)
    print(f"vendedor (a) {n} su comisión es {c}") 
