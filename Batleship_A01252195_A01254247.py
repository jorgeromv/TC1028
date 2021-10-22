# %%
#--------------------------------TABLERO---------------------------
from random import randint

tablero =[]
for x in range(5):
    tablero.append(["O"] * 5)
#-------------- Numero de O en las filas  ----------

def imprimir_tablero(tablero): 
    for fila in tablero:
        print( " ".join(fila))

#------------- Hace las filas hacia abajo y quita las comillas -------

print ("Jugaremos muevete luz verde, aaaaaaa broma, batalla naval, !")
imprimir_tablero(tablero)
print("Escribe un numero de el 0 al 4")

def random_linea(tablero):
    return randint(0, len(tablero) - 1)

def random_col(tablero):
    return randint(0, len(tablero[0]) - 1)

nave_linea = random_linea(tablero) 
nave_col = random_col(tablero) 

#------------ da un valor random a la nave ---------


#------------ aqui empieza el loop -----------------
for turn in range(4):
    print ("Turno", turn + 1)
    adivina_linea = int(input("Linea?:")) 
    adivina_col = int(input("Columna?:"))

#----------- Todo lo escrito y 4 turnos -----------------------

    if adivina_linea == nave_linea and nave_col == nave_col:
        print ("¡Felicidades hundiste mi nave!") 
        break 
    else: 
        if (adivina_linea < 0 or adivina_linea > 4) or (adivina_col <0 or adivina_col > 4):
            print ("¡ni siquiera hay mar aqui!.") 
        elif(tablero[adivina_linea][adivina_col] == "X"):
            print ("Esta ya la adivinaste.") 
        else:
            print ("Fallaste ;)!") 
            tablero[adivina_linea][adivina_col] = "X"
            if turn == 3:
                print("suerte para la proxima, PERDISTE")          
        imprimir_tablero (tablero)
# %%
