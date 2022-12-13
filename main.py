def crear_tablero(n,char_i):
	# forma 1
	# tablero = []
	# for _ in range(n): # porque no necesito saber la variable
	# 	lista = []
	# 	for _ in range(n):
	# 		lista.append(char_i)
	# 	tablero.append(lista)
	# forma pro
	tablero = [[char_i for _ in range(n)] for _ in range(n)]
	return tablero

def imprimir_tablero(tablero, n):
	for fil in range(n):
		for col in range(n):
			print('[',tablero[fil][col],']',sep="", end="")
		print("")

def meter_una_jugada(tablero, num, fila, col):
	tablero[fila][col] = num
def meter_jugadas(tablero):
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
def encontrar_hueco(tablero,n, char_i):
	hueco_encontrado = False
	fila = 0
	col = 0
	fin_tablero = False
	while not hueco_encontrado and not fin_tablero:
		if tablero[fila][col] == char_i:
			hueco_encontrado = True
		else:
			#avanzar
			fila += 1
			if fila == n:
				col += 1
				fila = 0
		if col == n: # si la columna es 9
			fin_tablero = True
	return fila, col, hueco_encontrado
def buscarjugada(tablero,fila,col,n):
	mismo_num_fila = True
	mismo_num_col = True
	mismo_num_cuadrilla = True

	# como tengo que tener en cuenta TODOS los números de la fila hago For
	lista_num_fila = []
	for c in range(n):
		if type(tablero[fila][c]) == int:
			lista_num_fila.append(tablero[fila][c])

	lista_num_col = []
	for f in range(n):
		if type(tablero[f][col]) == int:
			lista_num_col.append(tablero[f][col])

	cuadrilla_fila = fila // 3
	cuadrilla_col = col // 3

	lista_num_cuadrilla = []
	for f in range(cuadrilla_fila*3, cuadrilla_fila*3 + 3):
		for c in range(cuadrilla_col*3, cuadrilla_col*3 + 3):
			if type(tablero[f][c]) == int:
				lista_num_cuadrilla.append(tablero[f][c])



	#print(lista_num_fila)
	#print(lista_num_col)
	#print(lista_num_cuadrilla)
	lista_total = lista_num_cuadrilla + lista_num_col + lista_num_fila
	print(lista_total)
	lista_num_posibles = []
	for x in range(1,10):
		if x not in lista_total:
			lista_num_posibles.append(x)
	print(lista_num_posibles)

def rellenar_tablero(tablero, n, char_i):
	fila, col, hueco_encontrado = encontrar_hueco(tablero, n, char_i)
	if hueco_encontrado:
		buscarjugada(tablero,fila,col,n)
		print("el hueco encontrado esta en la fila",fila, "y la columna", col)
		pass
	else:
		print("tablero lleno")
		tablero_lleno = True
if __name__ == '__main__':
	# variables control
	n = 9
	char_i = " "
	njugadas_aleat = 20
	# funciones 
	tablero = crear_tablero(n, char_i)
	meter_jugadas(tablero)
	imprimir_tablero(tablero, n)
	rellenar_tablero(tablero,n, char_i)