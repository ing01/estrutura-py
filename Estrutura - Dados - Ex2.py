#Elabore uma estrutura para representar um produto (código, nome, preço). Cadastre 5 produtos, use vetor/lista. Aplique 10% de aumento no preço do produto e apresente todos os dados do #preço.

class DadosProduto:
  codigo = 0
  nome = ''
  preco = 0

def main():
  vet_produto = []
  for i in range(3):
    produto = DadosProduto()
    produto.codigo = int(input('Insira o código do produto: '))
    produto.nome = input('Insira o nome do produto: ')
    produto.preco = float(input('Insira o preço do produto: '))
    produto.preco = produto.preco + (produto.preco * 0.1)
    vet_produto.append(produto)
  for i in range(len(vet_produto)):
    print('Código:',vet_produto[i].codigo,'\n','Nome:',vet_produto[i].nome,'\n','Preço: R$',vet_produto[i].preco)

main()
