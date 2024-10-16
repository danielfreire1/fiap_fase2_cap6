# Fase 2 - Cap 6 - Python e além

## Objetivo


**Solução**: Foi desenvolvido um sistema de controle de estoque de insumos, fertilizantes e pesticidas. Com objetivo de controlar o estoque e conseguir prever o consumo. Para um melhor gestão e lucratividade do cultivo.

A ideia foi mostrar o que foi passado nas aulas de Python.

## Estrutura do projeto (Arquivos principais)

* **menu.py** - Responsável pela gestão de todo menu do software, utilizando função, metodo, recursividade, dicionarios, etc
* **repository/*** - Responsável pela persistencia e consulta de dados no banco de dados oracle.
* **scripts** - Todos os scripts para criação e seed para testar a solução
    > Estou utilizando o banco fornecido pela Fiap, este banco já esta com toda estrutura cadastrada.
* **relatorio.py** - Geração de graficos e analise estatística descritiva.


## Requisitos para rodar o projeto

* Python 3.11
* Gerenciador de pacotes **poetry**

## Rodar sistema

```bash
    poetry install
    python src/main.py
```


