1.	README_Elisangela_Leal_Lima_da_Encarnacao_T1

1.1.	Identificação Mini Projeto Avaliativo:
1.1.1.	Disciplina: Visualização de Dados e Business Intelligence
1.1.2.	Curso: SENAI/SC - Lab 365 
1.1.3.	Turma: T1
1.1.4.	Aluna: Elisângela Leal Lima da Encarnação
1.1.5.	E-mail: elisencarnacao01@gmail.com

1.2.	Base de dados utilizada no projeto (Kaggle):
1.2.1.	Fonte do arquivo Varejo.csv: https://www.kaggle.com/datasets/namespaiva/base-varejo/data

2.	Sobre o Projeto
Este projeto foi desenvolvido utilizando Python e Pandas com o objetivo de realizar a limpeza, tratamento e análise de uma base de dados de varejo.
A proposta do trabalho é aplicar conceitos básicos de análise de dados, manipulação de tabelas e geração de insights utilizando uma base em formato CSV.
A base utilizada contém informações relacionadas a clientes, compras e comportamento de consumo no varejo.

3.	Objetivo:
3.1.	Carregar e explorar uma base de dados CSV
3.2.	Identificar problemas nos dados
3.3.	Realizar limpeza e tratamento das informações
3.4.	Gerar estatísticas descritivas
3.5.	Explorar agrupamentos e padrões
3.6.	Desenvolver prática com Python e Pandas
3.7.	Utilizar Git e GitHub para divulgação do projeto

4.	Tecnologias Utilizadas
4.1.	Python
4.2.	Pandas
4.3.	NumPy
4.4.	VS Code
4.5.	Git
4.6.	GitHub

5.	Dicionário de Dados
5.1.	DATA: Data da compra; 
5.2.	CO_ID: Identificação do número de compra (número da nota fiscal); 
5.3.	CL_ID: Identificação do cliente (número do cliente);
5.4.	CL_GENERO: Sexo biológico informado pelo cliente;
5.5.	CL_EC: Estado civil do cliente:
5.5.1.	1: Casado ou união estával;
5.5.2.	2: Divorciado; 
5.5.3.	3: Separado; 
5.5.4.	4: Solteiro;
5.5.5.	5: Viúvo. 
5.6.	CL_FHL: Número de filhos do cliente; 
5.7.	CL_SEG: Segmentação econômica do cliente (classe A, B ou C); 
5.8.	PR_ID: Código do produto (SKU) adquirido; 
5.9.	PR_CAT: Categoria do produto adquirido;
5.10.	PR_NOME: Nome do produto adquirido

6.	Etapas Desenvolvidas
6.1.	Carregamento da Base
6.1.1.	Nesta etapa foi realizado:
6.1.1.1.	Leitura do arquivo CSV com Pandas
6.1.1.2.	Verificação da quantidade de registros
6.1.1.3.	Visualização das colunas
6.1.1.4.	Identificação dos tipos de dados

6.2.	Verificação de Problemas na Base
6.2.1.	Foram analisados possíveis problemas nos dados, como:
6.2.1.1.	Valores nulos
6.2.1.2.	Registros duplicados
6.2.1.3.	Datas inválidas
6.2.1.4.	Categorias vazias
6.2.1.5.	Inconsistências em colunas

6.3.	Limpeza dos Dados
6.3.1.	As seguintes ações de tratamento foram realizadas:
6.3.1.1.	Remoção ou preenchimento de valores nulos
6.3.2.	Exclusão de registros duplicados
6.3.3.	Conversão de tipos de dados
6.3.4.	Ajuste da coluna de datas para datetime

6.4.	Estatísticas Descritivas
6.4.1.	Foram calculadas estatísticas da coluna relacionada ao número de filhos dos clientes:
6.4.1.1.	Média
6.4.1.2.	Mediana
6.4.1.3.	Moda
6.4.1.4.	Desvio padrão
6.4.1.5.	Valor máximo
6.4.1.6.	Valor mínimo
6.4.1.7.	Contagem de registros

6.5.	Análise de Agrupamentos
6.5.1.	Foram realizados agrupamentos utilizando:
6.5.1.1.	groupby()
6.5.1.2.	pivot_table()
6.5.2.	Exemplos de análises:
6.5.2.1.	Gênero com maior volume de compras
6.5.2.2.	Comparação de vendas por categoria
6.5.2.3.	Relação entre perfil do cliente e consumo

6.6.	Principais Insights
6.6.1.	Alguns insights encontrados durante a análise:
6.6.2.	Existência de valores nulos em colunas importantes
6.6.3.	Presença de registros duplicados
6.6.4.	Diferença de comportamento de compra entre grupos
6.6.5.	Necessidade de padronização de alguns dados
6.6.6.	Possíveis inconsistências em informações de clientes

7.	Estrutura do Projeto
projeto-varejo/
│
├── dados/
│   └── Varejo.csv
│
├── src/
│   └── analise_varejo.py
│
├── README.md

8.	Reflexão Teórica: ETL e Qualidade dos Dados
O processo de ETL (Extração, Transformação e Carga) é fundamental para garantir a qualidade dos dados utilizados em análises. Neste projeto, a extração ocorreu por meio da leitura do arquivo CSV, enquanto a transformação envolveu o tratamento de valores nulos, remoção de duplicidades e conversão de tipos de dados. Essas etapas permitiram melhorar a consistência e a confiabilidade das informações, demonstrando a importância da qualidade dos dados para a obtenção de análises e insights mais precisos.

9.	Conclusão do projeto
Este projeto permitiu realizar a limpeza, padronização e análise de uma base de dados de varejo utilizando Python e Pandas. Foram identificados e tratados valores nulos, registros duplicados e inconsistências nos dados, além da conversão adequada dos tipos de informações. Também foram geradas estatísticas descritivas da variável "Número de Filhos" e realizadas análises de agrupamento para identificar padrões de comportamento dos clientes. Os resultados demonstram a importância do tratamento dos dados para garantir análises mais confiáveis e gerar insights relevantes para futuras tomadas de decisão.
