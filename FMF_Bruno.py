a = 5
b = 3
c = 10
soma = a + b + c

print("A primeira soma é: ",soma)
print("\n")

quadrado = soma**2

print(quadrado)
print("\n")

#declaração de variaveis, soma dois numeros, eleva ao quadrado e imprime texto da soma e seu quadrado
#todos os códigos anteriores

print("A soma é: ",soma)
print("O quadrado da soma é: ",quadrado)
print("\n")

#verificar se a soma é verdadeira ou falsa

print(soma==7)
print(soma==18)
print("\n")

#estrutura de controle para tomada de decisão

if soma == 10:
    print ("A soma é 10.")
else:
    print("A soma não é 10!")
print("\n")

#soma 2 numeros e imprime esses dois numeros

n1 = 5
n2 = 10

soma2 = n1 + n2
print("A soma é: ",soma2)
print("Os dois numeros são: ",n1,"|",n2)
print("\n")

#loop com for
for n in range(3):
    print(n)
print("\n")

#imprimir nome em sequencia de 5
for name in range(5):
    print("Igor")
print("\n")

#ler valor através do comando input, passando para variavel nome

nome = input ("Qual é seu nome?")
print ("Seu nome é: ", nome)
print("\n")

#condicionais
horario = input ("Qual a parte do dia?")

if horario == "tarde":
    print ("Boa tarde!")
elif horario == ("manhã"):
    print("Bom dia!")
else:
    print("Boa noite!")
print("\n")