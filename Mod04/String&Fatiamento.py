# Conhecendo metodos úteis da classe string
# -> Manipular sequências de caracteres


palavra = "PythoN"
print(palavra.upper())
print(palavra.lstrip())
print(palavra.rstrip())
print(palavra.lower())
print(palavra.center(15, "-"))
print("_".join(palavra))



# Interpolação de variáveis 
# -> Temos 3 formas, % , Format, F strings. Pemeira forma não é atualmente recomendada e seu uso em python3 é raro

# Metdod % 
"""
Nome = "Nome"
Idade = 20
print("Nome: %s Idade: %d" % (Nome, Idade))

# Metodo Format
print("Nome: {} Idade: {}".format(Nome, Idade))

# Metodo f String
print(f"Nome: {Nome} Idade: {Idade}")
"""




#Fatiamento de String
# -> é uma tecnica utilizada para retornar substrings , informando inicio, fim, e passo
# -> Start, Stop e Step

nome = " Guilherme carvalho Souza "

print(nome[0])
print(nome[9])
print(nome[:9])
print(nome[5:])
nome[5:10]
nome[1:6:8]
nome[:]
nome[::-1]

# String Multiplas linhas
# -> 
