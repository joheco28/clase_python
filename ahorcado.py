from random import randint

palbras = ["Matematicas","fisica","computadora","lenguaje"]
vidas=[1,2,3,4,5,6]

auxiliar=[]

def selecPalabra():
    i = randint(0,4)
    p=palbras[i]
    return p

def espacios(p):
    a=len(p)
    for i in range(a):
        auxiliar.append("_")
    escribirLetras(auxiliar)


def encontrarLetra(p,l):
    op=0
    for i in range(len(p)):
        if p[i]==l:
            auxiliar[i]=l
            op=op+1
    if op==0:
        vidas.pop()
    print("tus vidas son ", end=" ")
    print(vidas)
    escribirLetras(auxiliar)



def escribirLetras(p):
    for i in range(len(p)):
        print(p[i], end=" ")


def ingresaLetra(p):
    op=1
    while op==1:
        l=input("escribe una letra ")
        if l=="@":
            op=0
        else:
            encontrarLetra(p,l)
            if "_" not in auxiliar:
                print("/n")
                print("congratulaciones has GANADO")
                op=0
            
            if vidas == []:
                print("/n")
                print("has PERDIDO para la proxima")
                op=0

if __name__ == "__main__":
    p =selecPalabra()
    print(p)
    print("tus vidas son ", end=" ")
    print(vidas)
    espacios(p)
    ingresaLetra(p)