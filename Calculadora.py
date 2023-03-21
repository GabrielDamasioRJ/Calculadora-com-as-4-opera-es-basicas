#Calculadora simples em python
       
print("************** Calculadora em python feita por Gabriel Damasio ************** \n \n \n")

print("Digite o número da operação desejada: \n \n 1. Soma \n 2. Subtração \n 3. Multiplicação \n 4. Divisão \n \n ")

#Loop while que somente será encerrado caso o usuário selecione uma operação numérica

while True:
      try:
         seletorDeOperacao = int(input("Digite o número da operação: "))
      except:
         print("Você não digitou um número!")
         continue
      else:
         break

if seletorDeOperacao == 1:

#Caso a soma seja selecionada, o usuário deve digitar apenas numeros, caso contrario o loop while não se encerrará

   while True:
      try:
         num1=float(input("Digite o primeiro numero: "))
         num2=float(input("Digite o segundo numero: "))
         print("O resultado da soma é: " , num1+num2)
         break
      except ValueError:
         print("Digite apenas numeros! Tente novamente.")

#Caso a subtração seja selecionada, o usuário deve digitar apenas numeros, caso contrario o loop while não se encerrará

elif seletorDeOperacao == 2:

   while True:
      try:
         num1 = float(input("Digite o primeiro numero: "))
         num2 = float(input("Digite o segundo numero: "))
         print("O resultado da subtração é: ", num1 - num2)
         break
      except ValueError:
         print("Digite apenas numeros! Tente novamente.")
   
elif seletorDeOperacao == 3:

# Caso a multiplicação seja selecionada, o usuário deve digitar apenas numeros, caso contrario o loop while não se encerrará

   while True:
      try:
         num1=float(input("Digite o primeiro numero: "))
         num2=float(input("Digite o segundo numero: "))
         print("O resultado da multiplicação é: " , num1*num2)
         break
      except ValueError:
         print("Digite apenas numeros! Tente novamente.")

elif seletorDeOperacao == 4:

#Caso a divisão seja selecionada, o usuário deve digitar apenas numeros, caso contrario o loop while não se encerrará.
# Se for digitado zero como divisor também sera requisitado um novo numero

   while True:
      try:
         num1=float(input("Digite o primeiro numero: "))
         num2=float(input("Digite o segundo numero: "))
         print("O resultado da soma é: " , num1/num2)
         break
      except ValueError:
         print("Digite apenas numeros! Tente novamente.")
      except ZeroDivisionError:
         print("Não é possível dividir por zero! Tente novamente.")
   
else: 
   print("Numero de seleção inválido! ")