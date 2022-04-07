nome = input('Informe o seu nome: ')
idade = input('Informe a sua idade: ')
altura = input('Informe a sua altura (ex.: 1.72): ')
peso = input('Informe seu peso conforme à balança (ex.: 52.4): ')
dia = input('Informe o dia em que nasceu: ')
mes = input('Informe seu mês de nascimento (extenso): ')
ano = input('Informe o ano em que nasceu: ')
imc = float(peso)/float(altura)**2
print('')
print(f'O(A) {nome} tem {idade} anos de idade, tem {altura} metros de altura e tem a massa de {peso}kg;')
print(f'O(A) {nome} nasceu dia {dia} de {mes} de {ano}')
if int(idade) >= 18:
    print(f'O(A) {nome} possui maioridade? \n Sim')
else:
    print(f'O(A) {nome} possui maioridade? \n Não')
print(f'O IMC (Índice de Massa Corporal) do(a) {nome} é de {imc:.4f};')
if imc >= 24.9:
    print(f'O(A) {nome} está com o IMC ideal? \n Não')
elif imc <= 18.4:
    print(f'O(A) {nome} está com o IMC ideal? \n Não')
else:
    print(f'O(A) {nome} está com o IMC ideal? \n Sim '
          f'\n Resgitro concluído com sucesso!')
print('__________________________________________________')
input('')
