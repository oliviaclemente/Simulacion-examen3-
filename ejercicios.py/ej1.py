def creartablero(n):
  caracter_inicial= " "
  lista= []
  tablero= []
  for _ in range(n): # _ no ncesito saber la variable
    lista=[]
    for _ in range(n):
      lista.append(1)
    tablero.append(lista)
  return tablero
def imprimirtablero(tablero,n):
  for fila in range(n):
    for columna in range(n):
      print("[",tablero[fila][columna],"]", sep=" " ,end="")
    print("")
def rellenar_tablero(tabero, num, fila, columna):
  tablero[fila][columna]= num
def meter_jugada(tablero):
	meter_una_jugada(tablero,5,0,0)
	meter_una_jugada(tablero,2,1,1)
	meter_una_jugada(tablero,9,2,2)
	meter_una_jugada(tablero,6,3,2)
	meter_una_jugada(tablero,9,4,1)
	meter_una_jugada(tablero,3,5,0)
	meter_una_jugada(tablero,9,6,0)
	meter_una_jugada(tablero,1,7,1)
	meter_una_jugada(tablero,4,7,2)
	meter_una_jugada(tablero,5,8,2)
	meter_una_jugada(tablero,4,0,4)
	meter_una_jugada(tablero,1,1,4)
	meter_una_jugada(tablero,7,2,4)
	meter_una_jugada(tablero,8,2,3)
	meter_una_jugada(tablero,7,3,3)
	meter_una_jugada(tablero,3,4,3)
	meter_una_jugada(tablero,5,4,4)
	meter_una_jugada(tablero,4,4,5)
	meter_una_jugada(tablero,6,6,4)
	meter_una_jugada(tablero,3,7,4)
	meter_una_jugada(tablero,8,8,4)
	meter_una_jugada(tablero,7,8,5)
	meter_una_jugada(tablero,7, 7, 8)
	meter_una_jugada(tablero,2, 6, 8)
	meter_una_jugada(tablero,1, 5, 8)
	meter_una_jugada(tablero,5, 7, 7)
	meter_una_jugada(tablero,6, 4, 7)
	meter_una_jugada(tablero,2, 3, 6)
	meter_una_jugada(tablero,1, 2, 6)
	meter_una_jugada(tablero,6, 1, 6)
	meter_una_jugada(tablero,8, 1, 7)
	meter_una_jugada(tablero,9, 0, 8)


def encontrar_hueco(tablero,n , caracter_inicial):
  hueco_encontardo= False
  fila= 0
  columna=0
  fin_tablero= False
  while not hueco_encontrado and not fin_tablero:
    if tablero[fila][col] == caracter_inicial: 
      hueco_encontardo= True
    else: 
      #avanzar
      fila += 1 
      if fila == n:
        columna +=1
        fila= 0
    if columna == n: 
      fin_tablero= True
    
  return fila, columna, encontrado
  
def rellenar_tablero(tablero):
  fila, columna, encontrado= encontrar_hueco(tablero)
  if hueco_encontrado:
    #buscarjugada()
    print("El hueco encontrado esta en la fila", fila, "y la columna", columna)
    pass
  else:
    print("tablero lleno")
    tablero_lleno=True



if __name__ == '__main__':
  #variables control
  n=9
  #funciones
  tablero= creartablero(n)
 
  tablero= crear_tablero(n, caracter_inicial)
  meter_jugada(tablero)
  imprimirtablero(tablero,n)
  rellenar_tablero(tablero, n , caracter_inicial)
  