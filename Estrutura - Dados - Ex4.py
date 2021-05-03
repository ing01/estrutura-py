#Uma escola precisa montar o cadastro geral de seus alunos. Este cadastro deverá conter as seguintes informações por aluno: nome completo, data de nascimento, telefone, 
#endereço e série atual. Levando em conta que esta escola possui no máximo 500 alunos, como você faria para estruturar estas informações num sistema de gerenciamento 
#para a escola? Implemente utilizando estrutura. Também use a criação de funções para cada operação.

class Tipo_Aluno:
  nome = ''
  datan = ''
  telefone = ''
  endereco = ''
  serie = 0

def cadastrar():
  vet_aluno = []
  for i in range(3):
    aluno = Tipo_Aluno()
    aluno.nome = input('Cadastre o nome: ')
    aluno.datan = input('Cadastre a data de nascimento: ')
    aluno.telefone = input('Cadastre o telefone: ')
    aluno.endereco = input('Cadastre o endereço: ')
    aluno.serie = input('Cadastre a série atual: ')
    vet_aluno.append(aluno)
  return vet_aluno

def consultar(va):
  nome_a_consultar = input('Qual nome deseja pesquisar? ')
  achei = False
  for i in range(len(va)):
    if nome_a_consultar in va[i].nome:
      achei = True
  if achei:
      print('Aluno encontrado')
  else:
      print('Aluno não encontrado')

def visualizar(va):
  for i in range(len(va)):
     print('Nome:',va[i].nome,'\tData de nascimento:',va[i].datan,'\tTelefone:',va[i].telefone,'\tEndereço:',va[i].endereco,'\tSérie atual:',va[i].serie)  

def menu():
  print('\n * Menu de opções *')
  print('1. Cadastrar alunos')
  print('2. Consultar por nome')
  print('3. Visualizar todos os dados')
  print('4. Sair')
  op = int(input('Digite a opção desejada: '))
  return op

def main():
  opcao = menu()
  while opcao >= 1 and opcao <= 3:
    if opcao == 1:
      vet_a = cadastrar()
    elif opcao == 2:
      consultar(vet_a)
    elif opcao == 3:
      visualizar(vet_a)
    opcao = menu()

main()
