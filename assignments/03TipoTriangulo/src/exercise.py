def main():
    #escribe tu código abajo de esta línea
    l1 = int(input("Ingresa la medida del lado 1: "))
    l2 = int(input("Ingresa la medida del lado 2: "))
    l3 = int(input("Ingresa la medida del lado 3: "))
    if l1==l2 and l1==l3:
        print("ES UN TRIANGULO EQUILATERO")
    elif l1!=l2 and l1!=l3:
            print("ES UN TRIANGULO ESCALENO") 
    else:
                print("ES UN TRIANGULO ISOSCELES")
    if l3 > l1 + l2:
        print("NO ES UN TRINAGULO")
    
   
    
if __name__=='__main__':
    main()
