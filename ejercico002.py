def contar(palabra, l):
  p=palabra.lower()
  a=[]
  for i in range(len(l)):
     a.append(p.count(l[i].lower()))     
  return a

if __name__ == "__main__":
    t=input("ingrese un texto al programa ")
    l=[]
    c=[]
    for i in range(3):
        l.append(input("ingresa una letra "))
    c = contar(t,l)

    for i in range(3):
        print(f"la letra {l[i]}  esta {c[i]} veces")
