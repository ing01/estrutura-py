# Estrutura para representar um produto (código, nome, preço). Aplique 10% de aumento no preço do produto e apresente.

class produto:
  codigo = 0
  nome = ''
  preco = 0

def main():
  prod = produto()
  prod.codigo = int(input('Insira o código do produto: '))
  prod.nome = input('Inira o nome do produto: ')
  prod.preco = float(input('Insira o preço do produto: '))
  prod.preco = prod.preco + (prod.preco * 10 / 100)
  print(F'Código: {prod.codigo}\nNome: {prod.nome}\nPreço: R${prod.preco:.2f}')

main()
