# Estrutura para representar um produto (código, nome, preço). Crie uma função para cadastrar 5 produtos. 
# Crie outra função para aplicar 10% de aumento no preço do produto e apresente, por meio de outra função, todos os dados do produtos cadastrados, após o aumento

class Tipo_Produto:
  nome = ''
  preco = 0.0
  codigo = 0
  aumento  = 0.0

def Cadastro():
  cadastros = []
  for i in range(5):
    a = Tipo_Produto()
    a.nome = input('Insira o nome do produto: ')
    a.preco = float(input('Insira o valor do produto: '))
    a.codigo = int(input('Insira o código do produto: '))
    cadastros.append(a)
  return cadastros

def Novo_preco(cadastros):
  for i in range(len(cadastros)):
    cadastros[i].aumento = cadastros[i].preco + (cadastros[i].preco * 0.1)
  return cadastros

def apresentar(cadastros):
  for i in range(len(cadastros)):
    print('Nome do produto: \t Preço do produto: \t Código do produto: \t Preço pós aumento: ')
    print(cadastros[i].nome,'\t \t',cadastros[i].preco,'\t \t',cadastros[i].codigo,'\t \t',cadastros[i].aumento)
    print()

def main():
    vetp = Cadastro()
    apresentar(vetp)
    vet_novo = Novo_preco(vetp)
    apresentar(vet_novo)

main()
