# 📊 Desafio Analista de Dados – SEFAZ Maceió

## Sobre o projeto

Este repositório apresenta a solução desenvolvida para o desafio técnico da vaga de Estágio em Análise de Dados da Secretaria Municipal da Fazenda de Maceió.

O objetivo foi desenvolver um pipeline completo de ETL (Extração, Transformação e Carga), consolidando os dados financeiros públicos das capitais brasileiras entre 2020 e 2025 para gerar análises e indicadores que auxiliem na tomada de decisão.

Além do processamento dos dados, foram produzidos rankings, indicadores financeiros e análises específicas para o município de Maceió.

---

# Objetivos

- Automatizar a extração dos arquivos ZIP fornecidos.
- Consolidar os dados financeiros em um único DataFrame.
- Padronizar e enriquecer os dados.
- Armazenar os dados em formato Parquet.
- Desenvolver análises exploratórias.
- Criar indicadores para apoiar decisões.

---

# Tecnologias utilizadas

- Python 3
- Pandas
- PyArrow
- Pathlib

---

# Estrutura do projeto

```
Desafio-Analista-de-Dados-Sefaz-Macei-
│
├── dados_compactos/
│
├── data/
│   ├── extracted/
│   └── parquet/
│       └── finbra_consolidado.parquet
│
├── docs/
│
├── src/
│   ├── extracao.py
│   ├── leitura.py
│   ├── tratamento.py
│   ├── analise.py
│   └── utils.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Organização do ETL

O pipeline foi dividido em módulos independentes.

## 1 - Extração

Responsável por localizar automaticamente todos os arquivos ZIP e realizar a extração para suas respectivas pastas.

Arquivo:

```
extracao.py
```

---

## 2 - Leitura

Responsável por:

- localizar todos os CSVs;
- identificar o ano de cada arquivo;
- realizar a leitura utilizando:

- separador ";"
- encoding latin-1
- decimal ","

Arquivo:

```
leitura.py
```

---

## 3 - Tratamento

Nesta etapa são realizadas:

- consolidação dos DataFrames;
- padronização dos nomes das colunas;
- criação da coluna Ano;
- identificação de Funções e Subfunções;
- criação das colunas:

- tipo_conta
- codigo_conta
- nome_conta

Também é realizada a padronização do estágio da despesa.

Ao final, o conjunto consolidado é salvo em formato Parquet.

Arquivo:

```
tratamento.py
```

---

## 4 - Análise

A etapa final realiza:

- panorama geral dos dados;
- quantidade de capitais por ano;
- quantidade de registros por ano;
- panorama dos estágios da despesa;
- ranking de gastos em Saúde;
- taxa de execução financeira;
- indicadores específicos para Maceió.

Arquivo:

```
analise.py
```

---

# Por que utilizar Parquet?

Foi escolhido o formato Parquet por ser um formato colunar otimizado para análise de dados.

Entre suas vantagens estão:

- menor espaço em disco;
- leitura mais rápida;
- melhor desempenho para análises;
- evita consolidar novamente todos os arquivos CSV a cada execução.

---

# Principais análises

Durante o desenvolvimento foram produzidas as seguintes análises:

- Quantidade de capitais por ano;
- Quantidade de registros por ano;
- Panorama financeiro dos estágios da despesa;
- Ranking de gastos pagos em Saúde;
- Ranking de Execução Financeira;
- Indicadores específicos para o município de Maceió.

---

# Indicadores desenvolvidos para Maceió

Como diferencial, foram criados indicadores específicos para a Prefeitura de Maceió.

São apresentados:

- posição nacional em gastos com Saúde;
- valor total investido;
- taxa de execução financeira;
- posição nacional em execução;
- população;
- gasto por habitante;
- insight automático interpretando os resultados.

---

# Como executar

## 1 - Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/Desafio-Analista-de-Dados-Sefaz-Macei-.git
```

---

## 2 - Crie um ambiente virtual

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3 - Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 4 - Execute o pipeline

Extração

```bash
python src/extracao.py
```

Tratamento

```bash
python src/tratamento.py
```

Análises

```bash
python src/analise.py
```

---

# Resultados

O projeto gera um relatório contendo:

- resumo geral;
- rankings;
- panorama financeiro;
- indicadores para Maceió;
- insights automáticos.

---

# Possíveis melhorias

Como evolução futura do projeto, podem ser implementados:

- Dashboard interativo (Streamlit ou Power BI);
- Exportação automática de relatórios;
- Novos indicadores financeiros;
- Comparação temporal entre municípios;
- API para consulta dos indicadores.

---

# Autor

Lucas Gabriel Alves

Projeto desenvolvido como solução para o desafio técnico da vaga de Estágio em Análise de Dados da Secretaria Municipal da Fazenda de Maceió.