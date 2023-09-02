from random import randint
import os 


#Programa principal en español
def Spanish(userPoints,computerPoints):
    userPoints
    isValid=False
    while isValid==False:  #We ask the choice to the user until he write a correct one
        userChoice=input("Usario:").lower()
        isValid=validarEntrada(userChoice)
    #asignamos a una lista los diferentes valores y mediante randint generamos uno de estos de manera aleatoria
    lista=["piedra","papel","tijera"]
    computerChoice=lista[randint(0,2)]
    print("Computer: "+ computerChoice)
    
    #Tal como indica el juego comparamos el valor del usuario con el de la maquina para determinar el ganador
    if userChoice==computerChoice:
        print("Empate")
    elif (userChoice=='paper' and computerChoice =='rock') or (userChoice=='scissors' and computerChoice=='paper') or (userChoice=='rock' and computerChoice=='scissors'):
        print("Gana el usuario")
        userPoints+=1
    else:
        print("Gana la computadora")
        computerPoints+=1
    print("Usuario ",userPoints," - ",computerPoints,"Computadora")
    
    return userPoints,computerPoints


def validarEntrada(userChoice):
    if userChoice=='piedra' or userChoice=='tijeras' or userChoice=='papel':
        return True
    else:
        return False
def validEntry(userChoice):
    if userChoice=='rock' or userChoice=='scissors' or userChoice=='paper':
        return True
    else:
        return False
        

def English(userPoints,computerPoints):
    isValid=False
    while isValid==False:
        userChoice=input("User:").lower()
        isValid=validEntry(userChoice)
    
    lista=["rock","paper","scissors"]
    computerChoice=lista[randint(0,2)]
    print("Computer: "+ computerChoice)
    
  
    if userChoice==computerChoice:
        print("Draw")
    elif (userChoice=='paper' and computerChoice =='rock') or (userChoice=='scissors' and computerChoice=='paper') or (userChoice=='rock' and computerChoice=='scissors'):
        print("User Wins")
        userPoints+=1
    else:
        print("Computer Wins")
        computerPoints+=1
    print("User ",userPoints," - ",computerPoints,"Computer")
    return userPoints,computerPoints

def MenuPrincipal():
    userPoints=0
    computerPoints=0
    language=-1
    while language != '0':
        language=input("1-English \n2-Español\n0-Salir\n")
        if language=='1':
            userPoints,computerPoints=English(userPoints,computerPoints)
        if language=='2':
            userPoints,computerPoints=Spanish(userPoints,computerPoints)
    os.system('clear')
   

print("ROCK PAPER SCISSORS")

MenuPrincipal()