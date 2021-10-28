def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 1:    # Error en la logica. Debe ser == 0. Esto para pobar debugging
            divisors.append(i)
    return divisors


def run():
    
    num = int(input('Ingresa un número: '))
    print(divisors(num))
    print("Terminó mi programa")

  

if __name__ == '__main__':
    run()