# map - para mapear dados

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()
    
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

novos_produtos = [
    {**p, 'preco': 123} for p in produtos
]

print_iter(produtos)
print_iter(novos_produtos)