def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0: 
            divisors.append(i)
    return divisors


def run():
    
    try:
        num = int(input('Ingresa un número: '))
        if num<0:
            raise Exception("El número ingresado es negativo. Por favor ingrese un número positivo.")

    except ValueError:
        print("Por favor digita un número. No se aceptan símbolos ni caracteres.")

    except Exception as m:
        print(m)

    else:
        print("El programa corrió perfectamente. El resultado es: " + str(divisors(num)))
     
    finally:
         print("Terminó mi programa")

 

if __name__ == '__main__':
    run()