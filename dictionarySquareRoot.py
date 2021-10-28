
def run():
    
    limit=int(input("Please insert the maximun value: "))

    # dictionary = {i:i**0.5 for i in range(1,limit+1)}
    # print(dictionary)

    list= [i for i in range(1, limit+1) if i%2 !=0]

    print(list)

if __name__=="__main__":
    run()