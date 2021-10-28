
def validar_string(func):
    """Función que valida ingreso de strings"""
    def wrapper(string: str):
        dato = func(string)
        while True:        
            try:            
                valor = float(dato)
            except ValueError:
                print("Por favor ingresar un dato válido.")
                dato = func(string)
            else:
                return valor
    return wrapper

def validar_monto(monto, impuesto, campos):
    """Función que valida que el monto e impuesto son valores mayores a cero"""
    while True:
        if monto <= 0:
            print(f"Por favor ingresar un {campos[0]} mayor a cero.")
            monto = solicitar_datos(campos[0])
        elif impuesto <= 0:
            print(f"Por favor ingresar un {campos[1]} mayor a cero.")
            impuesto = solicitar_datos(campos[1])                           
        else:
            pago_con_impuesto = calcular_total(monto, impuesto)
            print(f"Pago con impuesto: {pago_con_impuesto}")
            break
        
@validar_string
def solicitar_datos(string: str):
    """Solicita al cliente los montos (precio e impuesto) y los retorna en una lista
    """
    dato = (input("Por favor ingresar el " + string + ": "))
    return dato

def calcular_total(pago_sin_impuesto: float, impuesto: float):
    """Realiza el cálculo del precio con impuesto y lo retorna"""
    return pago_sin_impuesto + pago_sin_impuesto*(impuesto/100)

def run():
    """Función principal"""
    campos = ["monto", "impuesto"]
    monto = solicitar_datos(campos[0])
    impuesto = solicitar_datos(campos[1])
    validar_monto(monto, impuesto, campos)
    
if __name__ == "__main__":
    run()