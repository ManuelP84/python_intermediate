def run():
    dictionary={}
    limit = int(input("Please enter the limit: "))

    # for i in range(1,limit+1):               
    #     dictionary[i]=i**3
    # print(dictionary)

    # for i in range(1, limit +1):
    #     if i%3 ==0:
    #         continue
    #     else:
    #         dictionary[i]=i**3

    dictionary ={i:i**2 for i in range(1,limit+1) if i%3 !=0}

    print(dictionary)



if __name__=="__main__":
    run()