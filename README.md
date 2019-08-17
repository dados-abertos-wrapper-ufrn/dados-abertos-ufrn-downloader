# Open Data UFRN Downloader
[![PyPI version](https://badge.fury.io/py/odufrn-downloader.svg)](https://badge.fury.io/py/odufrn-downloader)
[![Build Status](https://travis-ci.org/odufrn/odufrn-downloader.svg?branch=master)](https://travis-ci.org/odufrn/odufrn-downloader)
[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://img.shields.io/badge/license-MIT-red.svg)

Pacote para baixar os dados do portal de [dados abertos da UFRN](http://dados.ufrn.br/).

## Instalação
```bash
pip install odufrn-downloader
```

## Guia de uso
Veja a documentação [clicando aqui](https://odufrn.github.io/odufrn-downloader/).

Como começar a usar o pacote:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()
```

### Métodos
Abaixo estão listados os métodos disponíveis no pacote:

| Método | Descrição |
| ------ | ------- |
| `download_all` | Baixa todos os conjuntos de dados disponíveis. |
| `download_package` | Baixa o pacote de dados desejado. |
| `download_packages` | Baixa uma lista de pacotes de dados desejado. |
| `download_from_file` | Baixa os pacotes de dados que estão escritos em um arquivo de texto. |
| `download_group` | Baixa um grupo de conjuntos de dados desejado. |
| `download_groups` | Baixa uma lista de grupos de pacotes de dados desejado. |
| `load_packages` | Atualiza a lista de pacotes disponíveis. |
| `load_groups` | Atualiza a lista de grupos disponíveis. |
| `list_packages` | Lista os pacotes de dados. |
| `list_groups` | Lista os grupos de conjuntos de dados. |
| `search_related_packages` | Retorna uma lista de pacotes de dados relacionados a uma entrada. |
| `search_related_groups` | Retorna uma lista de grupos de conjuntos de dados relacionados a uma entrada. |

### Exemplo
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Lista os conjuntos de dados
ufrn_data.list_packages()

# Baixa um conjunto de dados
ufrn_data.download_package('discentes')

# Baixa uma lista de conjuntos de dados
packages = ['discentes', 'dados-complementares-de-discentes', 'dados-socio-economicos-de-discentes']
ufrn_data.download_packages(packages)
```
