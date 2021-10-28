
def run():
    my_list = ["Manuel" , "Pineda" , 36, "Ingeniero Electronico"]
    my_dict = {"Manuel Pineda":36 , "Angie Cruz": 33,"Juan Manuel": 3.5}

    super_list = [
                {"Name":"Manuel","Lastname":"Pineda","Age":36,"Heigt":1.72},
                {"Name":"Angie","Lastname":"Cruz","Age":33,"Heigt":1.72},
                {"Name":"Juan Manuel","Lastname":"Pineda","Age":3.5,"Heigt":0.92},
                {"Name":"Juan Andres","Lastname":"Pineda","Age":1,"Heigt":0.4},
    ]

    super_dict = {
                    "Numeros enteros":[1,2,3,4,5],
                    "Numeros reales":[0.1,4.3,8,10.2],
                    "Numeros imaginarios":["-3i","2i","-8i","40i","100.5i"]

    }

    for key, name in my_dict.items():
        print(key, " ", + name)

    for item in my_list:
        print(item)

    # print(my_dict)

if __name__=="__main__":
    run()