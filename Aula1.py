# Primeiro passo em Python
#print('Hello World!')

# Declarando variáveis
x = 10
y = 10.5
nome = 'Arthur'
eh_verdade = True

# 1 = True
# 0 = False

# Vendo o tipo das variáveis
#print(type(x))
#print(type(y))
#print(type(nome))
#print(type(eh_verdade))

#print(nome)

# Lendo variáveis do teclado
#nome = input("Digite seu nome: ")
#print(nome)

# Métodos para printar frase com uma variável
# Método 1 (mais usado em Python)
# Este método só funcionará nas versões 3.6 pra cima das versões de Python
print(f"Olá {nome}")

a = 'teste'
# Método 2
print("Olá %s! Bem vindo %s!" % (nome, a)) # %s printar string
print("O valor de x eh: %d" % (x)) # %d printar int
print("O valor de y eh: %f" % (y)) # %f printar float
print("O valor de y eh: %d" % (y))

# Note a diferença das linhas 35 e 36

#Método 3
print("Olá {}" .format(nome))










