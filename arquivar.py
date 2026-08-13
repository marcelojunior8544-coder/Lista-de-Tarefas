import json

def arquivar_tarefas(lista_tarefas, nome_arquivo="tarefas.json"):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(lista_tarefas, arquivo, indent=4, ensure_ascii=False)
    print(f'Sucesso: {len(lista_tarefas)} tarefas arquivadas em {nome_arquivo}')


def carregar_tarefas(nome_arquivo="tarefas.json"):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
