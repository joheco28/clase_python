def devolver_distintos(num):
    sum=0
    print(num)
    for i in range(3):
        sum=sum + num[i]
    if sum<10:
        print(num[0])
    if (sum>=10 and sum<=15):
        print(num[1])
    if sum>15:
        print(num[2])


if __name__ == "__main__":
    num =[]
    for i in range(3):
        n1 = int(input(f"Ingresar el valor {i} "))
        num.append(n1)
        num.sort()
    devolver_distintos(num)
    

