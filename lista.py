class ToDoList:
    def __init__(self):
        self.tarefas = []

    @staticmethod
    def menu():
        print('--- Lista de Tarefas ---')
        print('1 - Adicionar tarefa')
        print('2 - Exibir tarefas')
        print('3 - Remover tarefa')
        print('4 - Sair')

    def adicionar_tarefa(self):
        tarefa = input('Digite a tarefa: ').strip()

        if not tarefa:
            print('A tarefa não pode ficar sem nome!')
            return

        self.tarefas.append(tarefa)
        print(f'Tarefa "{tarefa}" adicionada com sucesso!')

    def exibir_tarefas(self):
        if not self.tarefas:
            print('Nenhuma tarefa cadastrada.')
            return

        print('\n--- Lista de Tarefas ---')
        for indice, tarefa in enumerate(self.tarefas, start=1):
            print(f'{indice} - {tarefa}')

    def remover_tarefa(self):
        if not self.tarefas:
            print('Nenhuma tarefa cadastrada.')
            return

        self.exibir_tarefas()

        try:
            numero = int(input('Digite o número da tarefa que deseja remover: '))
        except ValueError:
            print('Entrada inválida. Por favor, digite um número válido.')
            return

        if not 1 <= numero <= len(self.tarefas):
            print('Número inválido. Tente novamente.')
            return

        tarefa_removida = self.tarefas.pop(numero - 1)
        print(f'Tarefa "{tarefa_removida}" removida com sucesso!')

    def executar(self):
        while True:
            self.menu()

            try:
                opcao = input('\nEscolha uma opção: ').strip()
            except EOFError:
                print('\nEntrada inválida. Encerrando o sistema...')
                break

            if opcao == '1':
                self.adicionar_tarefa()
            elif opcao == '2':
                self.exibir_tarefas()
            elif opcao == '3':
                self.remover_tarefa()
            elif opcao == '4':
                print('Encerrando o sistema...')
                break
            else:
                print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    ToDoList().executar()