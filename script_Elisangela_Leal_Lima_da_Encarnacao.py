# =================================================================================
# MINI-PROJETO AVALIATIVO: ANÁLISE EXPLORATÓRIA DE DADOS (AED) APLICADA AO VAREJO
# =================================================================================

# ==================================================
# 1. IMPORTAÇÃO DA BIBLIOTECA CARREGAMENTO DA BASE 
# ==================================================

print("\n" + "=" * 50)
print("1. IMPORTAÇÃO DA BIBLIOTECA CARREGAMENTO DA BASE")
print("=" * 50)

# Importação das bibliotecas

import pandas as pd # Pandas: biblioteca principal para manipulação de dados em tabelas

import numpy as np # Biblioteca utilizada para operações numéricas e tratamento de valores nulos (NaN).

# Caminho do arquivo CSV

caminho = r"C:\\Python\\mini_projeto_avaliativo\\Miniprojeto_Elisangela_Leal_lima_da_Encarnacao_T1\\dados\\nao_processados\\base varejo.csv"

df_varejo = pd.read_csv(caminho) 



# Separação das informações

df_varejo = pd.read_csv(caminho, sep=";")

print(df_varejo.info())

# Visualização inicial das 10 primeiras linhas

print(df_varejo.head(10))

# Visualização do tamanho da tabela (quantidade de linhas e colunas)

print(df_varejo.shape)

#Visualização das colunas da tabela em lista
print(df_varejo.columns.to_list())



"""
Nome das colunas:
['DATA;CO_ID;CL_ID;CL_GENERO;CL_EC;CL_FHL;CL_SEG;PR_ID;PR_CAT;PR_NOME']
"""


# Tipos de dados

print(df_varejo.dtypes)

# Dicionário de dados

dicionario_dados = {
    "DATA": "Data da compra",
    "CO_ID": "Identificação da compra (número da nota fiscal)",
    "CL_ID": "Identificação do cliente",
    "CL_GENERO": "Sexo biológico informado pelo cliente",
    "CL_EC": {
        1: "Casado ou união estável",
        2: "Divorciado",
        3: "Separado",
        4: "Solteiro",
        5: "Viúvo"
    },
    "CL_FHL": "Número de filhos do cliente",
    "CL_SEG": "Segmentação econômica do cliente (Classe A, B ou C)",
    "PR_ID": "Código do produto (SKU)",
    "PR_CAT": "Categoria do produto",
    "PR_NOME": "Nome do produto"
}

# Exibir o dicionário de dados

print("\n" + "=" * 50)
print("DICIONÁRIO DE DADOS")
print("=" * 50)

for chave, valor in dicionario_dados.items():
    print(f"{chave}: {valor}")

# ==================================================
# 2. VERIFICAÇÃO DE PROBLEMAS
# ==================================================

print("\n" + "=" * 50)
print("2. VERIFICAÇÃO DE PROBLEMAS")
print("=" * 50)

# Visualização das informações da tabela (nome das colunas, tipo de dado e quantidade de valores nulos)
print(df_varejo.info())

# Verificação de Valores Nulos

nulos = df_varejo.isnull().sum().sum()
if nulos > 0:
    print(f"\nForam encontrados {nulos} valores nulos na base.")
else:
    print("\nNão foram encontrados valores nulos na base.")

# Categorias vazias

if "Categoria" in df_varejo.columns:

    categorias_vazias = (
        df["Categoria"].isna().sum()
        + (df["Categoria"] == "").sum()
    )

    print("\nCategorias vazias:")
    print(categorias_vazias)

# Datas inválidas

if "Data_Compra" in df_varejo.columns:

    datas_teste = pd.to_datetime(
        df["Data_Compra"],
        errors="coerce"
    )

# ==================================================
# 3. LIMPEZA DOS DADOS
# ==================================================

print("\n" + "=" * 50)
print("3. LIMPEZA DOS DADOS")
print("=" * 50)

# Visualização das estatísticas numéricas (contagem, média, desvio padrão, mínimo, máximo e quartis)
print(df_varejo.describe())

# Registros duplicados

duplicados = df_varejo.duplicated().sum()

print("\nQuantidade de registros duplicados:")
print(duplicados)


# Remoção de duplicados

df = df_varejo.drop_duplicates()

# Conversão de datas

if "Data_Compra" in df.columns:

    df["Data_Compra"] = pd.to_datetime(
        df["Data_Compra"],
        errors="coerce"
    )

# ==================================================
# 4. TRATAMENTO DE VALORES NULOS
# ==================================================

print("\n" + "=" * 50)
print("4. TRATAMENTO DE VALORES NULOS")
print("=" * 50)

print("\nTratamento dos valores nulos:")

for coluna in df_varejo.columns:

    nulos = df_varejo[coluna].isnull().sum()

    if nulos > 0:

        # Se a coluna for texto
        if df_varejo[coluna].dtype == "object":

            df_varejo[coluna] = df_varejo[coluna].fillna("Não Informado")

            print(
                f"{coluna}: {nulos} valores nulos preenchidos com 'Não Informado'."
            )

        # Se a coluna for numérica
        else:

            df_varejo[coluna] = df_varejo[coluna].fillna(
                df_varejo[coluna].median()
            )

            print(
                f"{coluna}: {nulos} valores nulos preenchidos pela mediana."
            )

    else:

        print(f"{coluna}: não possui valores nulos.")



print("\nLimpeza concluída com sucesso!")

# ==================================================
# 5. ESTATÍSTICAS DESCRITIVAS
# ==================================================

print("\n" + "=" * 50)
print("5. ESTATÍSTICAS DESCRITIVAS")
print("=" * 50)

# Verificação da Coluna Número de Filhos

if "CL_FHL" in df_varejo.columns:
    print("\nColuna Número de Filhos foi encontrada.")
else:
    print("\nA coluna Número de Filhos não foi encontrada.")

# Ajuste o nome da coluna se necessário

coluna_filhos = "CL_FHL"

# Visualização dos dados estatísticos

if coluna_filhos in df_varejo.columns:

    print("\nEstatísticas da coluna Número de Filhos")

    print("Média:", df_varejo[coluna_filhos].mean())

    print("Mediana:", df_varejo[coluna_filhos].median())

    print("Moda:", df_varejo[coluna_filhos].mode()[0])

    print("Desvio padrão:", df_varejo[coluna_filhos].std())

    print("Máximo:", df_varejo[coluna_filhos].max())

    print("Mínimo:", df_varejo[coluna_filhos].min())

    print("Contagem:", df_varejo[coluna_filhos].count())
else:
    print(f"A coluna '{coluna_filhos}' não foi encontrada.")

# ==================================================
# 6. ANÁLISE DE AGRUPAMENTOS
# ==================================================

print("\n" + "=" * 50)
print("6. ANÁLISE DE AGRUPAMENTOS")
print("=" * 50)

# Agrupamento 1: Gênero x Quantidade de Compras

if "CL_GENERO" in df_varejo.columns:

    genero_compras = (
        df_varejo.groupby("CL_GENERO")
        .size()
        .sort_values(ascending=False)
    )

    print("\nCompras por gênero:")
    print(genero_compras)



# Agrupamento 2: Categoria x Quantidade


if "PR_CAT" in df_varejo.columns:

    categoria_vendas = (
        df_varejo.groupby("PR_CAT")
        .size()
        .sort_values(ascending=False)
    )

    print("\nQuantidade por categoria:")
    print(categoria_vendas)



# Pivot Table: Gênero x Categoria

if (
    "CL_GENERO" in df_varejo.columns
    and "PR_CAT" in df_varejo.columns
):

  tabela = pd.pivot_table(
    df_varejo,
    index="CL_GENERO",
    columns="PR_CAT",
    aggfunc="size",
    fill_value=0
)

print("\nPivot Table - Gênero x Categoria")
print(tabela)

print("Fim do script")

# ==================================================
# 7. EXPORTAÇÃO DOS DADOS LIMPOS
# ==================================================

print("\n" + "=" * 50)
print("7. EXPORTAÇÃO DOS DADOS LIMPOS")
print("=" * 50)

# Caminho da pasta de saída
caminho_saida = r"C:\Python\mini_projeto_avaliativo\Miniprojeto_Elisangela_Leal_lima_da_Encarnacao_T1\dados\processados_limpos\Base_Varejo_Limpo.csv"


# Salvando o arquivo em csv

df_varejo.to_csv(
    caminho_saida,
    sep=";",
    index=False,
    encoding="utf-8-sig"
)

print("\nArquivo limpo exportado com sucesso!")
print(f"Local do arquivo: {caminho_saida}")
