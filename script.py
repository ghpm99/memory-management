import random

memory = [None] * 100
user_choice = 0
data_length = 0
data = ' '

for i in range(100):
    if random.randint(0, 11) >= 5:
        memory[i] = 'x'
    else:
        memory[i] = ' '


def sortMemoryMap(data):
    return data['total_empty']


def create_memory_map(memory):
    print('Criando mapa de memoria')
    index_can_be_allocated = []

    temp_empty_index = 0
    temp_total_empty = 0

    for i in range(memory.__len__()):
        if memory[i] == ' ':
            if temp_empty_index == 0:
                temp_empty_index = i
            temp_total_empty += 1
        if memory[i] == 'x':
            if temp_total_empty > 0:
                index_can_be_allocated.append({
                    'index': temp_empty_index,
                    'total_empty': temp_total_empty
                })
                temp_empty_index = 0
                temp_total_empty = 0
    print(index_can_be_allocated)
    return index_can_be_allocated


def allocate_memory(memory, index, data_length, data):
    for length in range(data_length):
        memory[index + length] = data
    print("Memoria depois da alocacao")
    print(memory)


def first_fit(memory, data_length, data):
    memory_map = create_memory_map(memory)
    print("Buscando melhor endereço")
    allocated = False
    for memory_data in memory_map:
        if memory_data['total_empty'] >= data_length:
            print("Espaço encontrado! alocando...")
            allocate_memory(memory, memory_data['index'], data_length, data)
            allocated = True
            break

    if allocated is not True:
        print("Nao foi possivel alocar, sem endereço")


def best_fit(memory, data_length, data):
    memory_map = create_memory_map(memory)
    print("Buscando melhor endereço")
    allocated = False
    for memory_data in memory_map:
        if memory_data['total_empty'] == data_length:
            print("Espaço encontrado! alocando...")
            allocate_memory(memory, memory_data['index'], data_length, data)
            allocated = True
            break
    if allocated is not True:
        print("Nao foi encontrado espaço ideal, alocando em espaço maior...")
        memory_map.sort(key=sortMemoryMap)
        for memory_data in memory_map:
            if memory_data['total_empty'] >= data_length:
                print("Espaço encontrado! alocando...")
                allocate_memory(memory, memory_data['index'], data_length, data)
                allocated = True
                break

    if allocated is not True:
        print("Nao foi possivel alocar, sem endereço")


def worst_fit(memory, data_length, data):
    memory_map = create_memory_map(memory)
    print("Buscando melhor endereço")
    allocated = False

    memory_map.sort(key=sortMemoryMap, reverse=True)
    for memory_data in memory_map:
        if memory_data['total_empty'] >= data_length:
            print("Espaço encontrado! alocando...")
            allocate_memory(memory, memory_data['index'], data_length, data)
            allocated = True
            break

    if allocated is not True:
        print("Nao foi possivel alocar, sem endereço")


while user_choice != 4:
    print("1 - Primeira Escolha")
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print("Escolha o algoritmo pelo numero")
    user_choice = int(input())
    if user_choice == 4:
        break
    print("Digite o tamanho da informacao")
    data_length = int(input())
    print("Digite a letra a ser utiliada")
    data = input()

    print("Memoria antes da alocacao")
    print(memory)
    if user_choice == 1:
        first_fit(memory, data_length, data)
    elif user_choice == 2:
        best_fit(memory, data_length, data)
    elif user_choice == 3:
        worst_fit(memory, data_length, data)
    else:
        print("Opcao invalida")
