import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


from repository import registro_repository

def analise_descretiva():
    print("=" * 50)
    print("Gerando analise descritiva de consumo por tipo de produto")
    print("=" * 50)
    registros = registro_repository.listar_consumos()
    df = pd.DataFrame.from_records(registros, columns=["Id", "Nome", "Tipo", "Consumo", "Data"])
    df_tipo = df.groupby('Tipo')

    resultado = df_tipo['Consumo'].agg(['mean', 'std', 'min', 'max'])
    resultado.rename(columns={
        'mean': 'média',
        'std': 'desvio_padrão',
        'min': 'mínimo',
        'max': 'máximo'
    }, inplace=True)

    print(resultado)

def grafico_consumo():
    print("=" * 50)
    print("Gerando grafico de consumo por tipo de produto")
    print("=" * 50)
    registros = registro_repository.listar_consumos_por_por_dia()
    df = pd.DataFrame.from_records(registros, columns=["Tipo", "Total_Consumo", "Data"])
    df.set_index('Data', inplace=True)
    df_mensal = df.groupby('Tipo').resample('ME').sum().unstack(level=0)  # Unstack para organizar os dados por tipo

    plt.figure(figsize=(12, 6))
    df_mensal.plot(kind='bar', width=0.8, ax=plt.gca())
    plt.title('Consumo Total de Produtos por Tipo ao Longo do Tempo')
    plt.xlabel('Mês')
    plt.ylabel('Consumo')
    plt.xticks(rotation=45) 
    plt.legend(title='Tipo de Produto')
    plt.tight_layout()  
    plt.show()