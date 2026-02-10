# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópiaa profunda)

def porcentagem(valor):
    numero = valor * 1.1
    return numero

def produtos_ordenados_por_nome(nome_lista):
    ordem = sorted(nome_lista, key=lambda nome: nome['nome'], reverse = True)
    return ordem

def produtos_ordenados_por_preco(preco_lista):
    ordem_valor = sorted(preco_lista, key=lambda preco: preco['preco'])
    return ordem_valor
    

aumento = [{'nome': p['nome'], 'preco': porcentagem(p['preco'])} for p in produtos]
nome = produtos_ordenados_por_nome(produtos)
valor = produtos_ordenados_por_preco(produtos)
    
# print(f'Preços com aumento de 10% :{aumento} \n'
#       f'Ordenados por nome:{nome} \n'
#       f'Ordenados por valor: {valor}'
#     )

print("Preços com aumento de 10%:") 
for p in aumento: 
    print(f"{p['nome']} - {p['preco']}") 
    
print("\nOrdenados por nome:") 
for p in nome: 
    print(f"{p['nome']} - {p['preco']}") 

print("\nOrdenados por valor:") 
for p in valor: 
    print(f"{p['nome']} - {p['preco']}")