def menu():
    print('---Lista de Tarefas---')
    print('1 - Adicionar tarefa')
    print('2 - Exibir tarefas')
    print('3 - Remover tarefa')
    print('4 - Sair')


def adicionar_tarefa(lista):
    tarefa = str(input('Digite a tarefa: ')).strip()
    if tarefa:
        lista.append(tarefa)
        print(f'Tarefa "{tarefa}" adicionada com sucesso!')
    else:
        print('A tarefa não pode ficar sem nome!')


def exibir_tarefas(lista):
    if not lista:
        print('Nenhuma tarefa cadastrada.')
    else:
        print('\n---Lista de Tarefas---')
        for i, tarefa in enumerate(lista, start=1):
            print(f'{i} - {tarefa}')


def remover_tarefa(lista):
    exibir_tarefas(lista)
    if lista:
        try:
            numero = int(input('Digite o número da tarefa que deseja remover: '))
            if 1 <= numero <= len(lista):
                removida = lista.pop(numero - 1)
                print(f'Tarefa "{removida}" removida com sucesso!')
            else:
                print('Número inválido. Tente novamente.')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número válido.')


def sistema():
    tarefas = list()
    while True:
        menu()
        try:
            opcao = input('\nEscolha uma opção: ')
        except EOFError:
            print('\nEntrada inválida. Encerrando o sistema...')
            break
        if opcao == '1':
            adicionar_tarefa(tarefas)
        elif opcao == '2':
            exibir_tarefas(tarefas)
        elif opcao == '3':
            remover_tarefa(tarefas)
        elif opcao == '4':
            print('Encerrando o sistema...')
            break
        else:
            print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    sistema()