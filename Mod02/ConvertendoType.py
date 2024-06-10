# Convertendo Tipos -> Em alguns momentos é necessário converter o tipo de uma variável
# para manipular de forma diferente. Por exemplo: 
# Variáveis do tipo String, que armazenam números e precisamos fazer algum matemática com esse valor.

price = 20
print(price)
print(int(1.0))
print(str(10.10))
print(type(10.10))

# ------------------------------
# Função Input
# Função Builtin Input é utilizada quando queremos ler dados da entrada padrão( teclado ). Ela recebe um argumento fo tipo string, que é exibido para o usuario na saída padrão (tela).
nome = input("Qual seu nome")
data_Nasceu = input("Sua data de nascimento")

# print(nome, data_Nasceu, end="...\n")
# print(nome, data_Nasceu, sep="#")
print(5 // 2)