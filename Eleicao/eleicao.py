candidatos = 10
azul = 0
vermelho = 0
amarelo = 0
nulo = 0

while candidatos > 3:
    candidatos = int(input("Quantos candidatos concorrerão? (Máximo 3): "))
    if candidatos > 3:
        print("O número de candidatos deve ser no máximo 3!")

qtd_chapas = candidatos
chapas = ['Azul', 'Vermelho', 'Amarelo']
candidatos_n = ['Nenhum', 'Nenhum', 'Nenhum']

for n in range(0, candidatos):
    candidatos_n[n] = input("Nome do candidato: ")

for x in range(0, 35):
    if candidatos_n[2] != 'nenhum':
        print('Candidatos: ', '\n1. Azul: ',     candidatos_n[0],
                              '\n2. Vermelho: ', candidatos_n[1],
                              '\n3. Amarelo: ',  candidatos_n[2])
    elif candidatos_n[1] != 'nenhum':
        print('Candidatos: ',   '\n1. Azul: ',     candidatos_n[0],
                                '\n2. Vermelho: ', candidatos_n[1])
    elif candidatos_n[0] != 'nenhum':
        print('Candidatos: ', '\n1. Azul: ', candidatos_n[0])
    else:
        print('Não há nenhum candidato!')

    voto = int(input('Qual é o seu voto (1, 2 ou 3; 0 para nulo): '))

    if voto == 1 :
        azul += 1
    elif voto == 2:
        vermelho += 1
    elif voto == 3:
        amarelo += 1
    elif voto == 0:
        nulo +=1
    else:
        'Voto inválido!'

print('Apuração de votos: ')
print('Azul: ', azul)
print('Vermelho: ', vermelho)
print('Amarelo: ', amarelo)
print('Nulos: ', nulo)

if azul > vermelho and azul > amarelo:
    print('O SÍNDICO ELEITO É', candidatos_n[0])
elif vermelho > azul and vermelho > amarelo:
    print('O SÍNDICO ELEITO É', candidatos_n[1])
elif amarelo > azul and amarelo > vermelho:
    print('O SÍNDICO ELEITO É', candidatos_n[2])






