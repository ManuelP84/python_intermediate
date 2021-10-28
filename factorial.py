
def factorial(number):
    if number==1:
        return 1
    return number*factorial(number -1)

def run():
    number = int(input("Please enter the number you need to apply factorial function: "))
    print("The factorial from "+ str(number)+ " is " + str(factorial(number)))


if __name__=="__main__":
    run()