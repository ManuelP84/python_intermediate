import random
import os

def read_data(words_route):
    with open(words_route, "r", encoding = "utf-8") as file:
        return [word.strip("\n") for word in file] #Create a list of the words by list comprehension
   
def select_word(words):
    return random.choice(words)

def visualization(user_word,tries):
    print("Bienvenido a HANG-MAN")
    print(f"Debes adivinar la palabra y/o las letras que la contienen...Tienes solo {tries} intentos!!!")
    for i in range(len(user_word)):
        print(user_word[i], end =" ") 
    print("\n")

def input_word():
    while True:
        try:
            input_word= input("Please enter the letter/word: ")
            if input_word.isalpha():
                return input_word.upper()
            else:
                raise Exception("Only alphabet characters allowed!!!")
            
        except Exception as m: 
            print(m)

# def  compare(random_word,option_word,user_word):
#     if len(random_word)==len(option_word):
#         cont=0
#         for i in range(len(random_word)):
#             if random_word[i]==option_word[i]:
#                 cont+=1
#         if cont==len(random_word):
#             for i in range(len(random_word)):
#                 user_word[i]=random_word[i]
#             return user_word
#     elif len(option_word)==1:
#         for i in range(len(random_word)):
#             if random_word[i]==option_word:
#                 user_word[i]=option_word
#         return user_word

    # else:
    #     return user_word
        
def win(random_word,user_word):
    cont=0
    for i in range(len(random_word)):
        if random_word[i]==user_word[i]:
            cont+=1
    if cont==len(random_word):
        return True
    else: return False

    
def run():
    tries=10 # Total lives
    state=False
    words_route="./files/data.txt" # Route of the file
    words =read_data(words_route)
    random_word=select_word(words).upper()

    user_word=["_" for i in range(len(random_word))]
    
    while tries>0 and not state:
        os.system("clear")
        visualization(user_word,tries)
        option_word=input_word()
        # user_word=compare(random_word,option_word,user_word)
        
        if len(random_word)==len(option_word):
            cont=0
            for i in range(len(random_word)):
                if random_word[i]==option_word[i]:
                    cont+=1
            if cont==len(random_word):
                for i in range(len(random_word)):
                    user_word[i]=random_word[i]
            else:
                tries-=1

        elif len(option_word)==1:
            cont=0
            for i in range(len(random_word)):
                if random_word[i]==option_word:
                    user_word[i]=option_word
                    cont+=1
            if cont==0:
                tries-=1

        else:
            tries-=1
        
        state = win(random_word,user_word)

    if tries==0:
        print("Has agotado todas tus vidas, la palabra es: ", random_word)      
    else:
        print("Ganaste!!!!!!")


if __name__ == "__main__":
    run()