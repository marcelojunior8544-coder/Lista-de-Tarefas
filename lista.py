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

    def adicionar_tarefa(self, tarefa: str) -> str:
        tarefa = str(tarefa).strip()

        if not tarefa:
            raise ValueError('A tarefa não pode ficar sem nome!')

        self.tarefas.append(tarefa)
        return tarefa

    def adicionar_tarefa_cli(self):
        tarefa = input('Digite a tarefa: ').strip()

        try:
            tarefa = self.adicionar_tarefa(tarefa)
        except ValueError as error:
            print(error)
            return

        print(f'Tarefa "{tarefa}" adicionada com sucesso!')

    def listar_tarefas(self) -> list[str]:
        return list(self.tarefas)

    def exibir_tarefas(self):
        if not self.tarefas:
            print('Nenhuma tarefa cadastrada.')
            return

        print('\n--- Lista de Tarefas ---')
        for indice, tarefa in enumerate(self.tarefas, start=1):
            print(f'{indice} - {tarefa}')

    def remover_tarefa(self, numero: int) -> str:
        if not self.tarefas:
            raise IndexError('Nenhuma tarefa cadastrada.')

        if not 1 <= numero <= len(self.tarefas):
            raise IndexError('Número inválido. Tente novamente.')

        return self.tarefas.pop(numero - 1)

    def remover_tarefa_cli(self):
        if not self.tarefas:
            print('Nenhuma tarefa cadastrada.')
            return

        self.exibir_tarefas()

        try:
            numero = int(input('Digite o número da tarefa que deseja remover: '))
        except ValueError:
            print('Entrada inválida. Por favor, digite um número válido.')
            return

        try:
            tarefa_removida = self.remover_tarefa(numero)
        except IndexError as error:
            print(error)
            return

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
                self.adicionar_tarefa_cli()
            elif opcao == '2':
                self.exibir_tarefas()
            elif opcao == '3':
                self.remover_tarefa_cli()
            elif opcao == '4':
                print('Encerrando o sistema...')
                break
            else:
                print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    ToDoList().executar()
    