#SOMAR NUMEROS ATE ATINGIR UM LIMITE

limite = 100
soma = 0
numero = 1

# ENQUANTO A SOMA FOR MENOR QUE O LIMITE, CONTINUE SOMANDO
# while soma < limite:
# 	soma += numero
# 	numero += 1
# 	print(soma)
# 	print(numero)
 
# ENCONTRAR O PRIMEIRO NUMERO DIVISIVL POR 7 EM UM INTERVALO
# 1 -> 99
# for numero in range(1, 100):
#   if numero % 7 ==0:
#   	print(numero)	
#   	break

# VERIFICAR SE TODOS OS ITENS DE UMA LISTA SAO POSITIVOS
numeros = [1,2,3,4,8,9, -11]
todos_positivos = True

for numero in numeros:
  if numero < 0:
    todos_positivos = False
    break
  
if todos_positivos == True:
  print('Todos os numeros sao positivos')
else:
  print('Existem numeros negativos')