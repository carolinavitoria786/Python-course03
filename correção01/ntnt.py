import copy

from p import produtos

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in produtos
]

produtos_ordenados_por_nome = sorted(
    produtos,
    key=lambda p: p['nome']
)

produtos_ordenados_por_preco = sorted(
    produtos,
    key=lambda p: p['preco']
)


print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')

