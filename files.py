def read():
    family =[]

    with open("./files/familia.txt", "r", encoding = "utf-8") as file:
        for line in file:
            if line.strip("\n").isnumeric():
                family.append(int(line))
            else:
                family.append(line.strip("\n"))
        print(family)


def write():
    family_names ={"Manuel Pineda":36,"Angie Cruz":33,"Juan Manuel":4,"Juan Andres":1}
    with open("./files/names.txt","w", encoding="utf-8") as file:
        for name,edad in family_names.items():
            file.write(f"{name}:{edad}\n") # file.write("%s :  %s\n" %(name, int(edad))) ---> Another way to do the same thing
            

def run():
    # read()
    write()


if __name__ == "__main__":
    run()