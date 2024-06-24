import json
from datetime import datetime

def ler(cArquivo):
    with open(cArquivo, 'r') as file:
        dados = json.load(file)
    return dados

def gravgar(cArquivo, dados):
    with open(cArquivo, 'w') as file:
        json.dump(dados, file, indent=4)

def addVenda(cArquivo, nova_venda):
    dados = ler(cArquivo)
    dados['vendas'].append(nova_venda)
    gravgar(cArquivo, dados)

def totalVenda(cArquivo, data_inicio, data_fim):
    dados = ler(cArquivo)
    total = 0
    data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
    data_fim = datetime.strptime(data_fim, '%Y-%m-%d')
    
    for venda in dados['vendas']:
        data_venda = datetime.strptime(venda['data_venda'], '%Y-%m-%d')
        if data_inicio <= data_venda <= data_fim:
            total += venda['total_venda']
    
    return total

def totalItens(cArquivo, nome_item):
    dados = ler(cArquivo)
    total = 0
    
    for venda in dados['vendas']:
        for item in venda['itens_vendidos']:
            if item['nome_item'] == nome_item:
                total += item['quantidade_vendida'] * item['preco_unitario']
    
    return total

def mostrarVenda(cArquivo):
    dados = ler(cArquivo)
    for venda in dados['vendas']:
        print(f"ID da Venda: {venda['id_venda']}")
        print(f"Data da Venda: {venda['data_venda']}")
        print("Itens Vendidos:")
        for item in venda['itens_vendidos']:
            print(f"  - Nome do Item: {item['nome_item']}")
            print(f"    Quantidade Vendida: {item['quantidade_vendida']}")
            print(f"    Preço Unitário: {item['preco_unitario']}")
        print(f"Total da Venda: {venda['total_venda']}")
        print("Informações do Cliente:")
        print(f"  Nome: {venda['informacoes_cliente']['nome']}")
        print(f"  Endereço: {venda['informacoes_cliente']['endereco']}")
        print("-" * 40)

cArquivo = 'brunoProdutosBDNR.json'

mostrarVenda(cArquivo)

print(f"Total de vendas no período: {totalVenda(cArquivo, '2024-06-20', '2024-06-23')}")

print(f"Total de vendas do item 'Caneca Magica': {totalItens(cArquivo, 'Caneca Magica')}")
