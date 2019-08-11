# Package
Os métodos aqui apresentados são referentes ao uso de pacotes (listagem, download, etc).

## download_all
Baixa todos os conjuntos de dados disponíveis.

**Parâmetros**:

| Parâmetro | Tipo | Valor padrão | Descrição |
| --------- | ---- | ------------ | --------- |
| `path` | `str` | `os.getcwd()` | O caminho da pasta onde serão adicionados os arquivos. |
| `dictionary` | `bool` | `True` | Indica se é para baixar o dicionário dos dados. |
| `years` | `list[int]` | `None` | Define os anos dos dados que serão baixados. |

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Baixar todos os packages de 2013 a 2018, sem dicionário
ufrn_data.download_all(dictionary=False, years=list(range(2013,2019)))
```

## download_package
Baixa o pacote de dados desejado.

**Parâmetros**:

| Parâmetro | Tipo | Valor padrão | Descrição |
| --------- | ---- | ------------ | --------- |
| `name` | `str` | - | Nome do pacote que se deseja baixar. |
| `path` | `str` | `os.getcwd()` | O caminho da pasta onde serão adicionados os arquivos. |
| `dictionary` | `bool` | `True` | Indica se é para baixar o dicionário dos dados. |
| `years` | `list[int]` | `None` | Define os anos dos dados que serão baixados. |

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Baixar os datasets de discentes sem dicionário
ufrn_data.download_package('discentes', dictionary=False)
```

## download_packages
Baixa uma lista de pacotes de dados desejado.

**Parâmetros**:

| Parâmetro | Tipo | Valor padrão | Descrição |
| --------- | ---- | ------------ | --------- |
| `packages` | `list[str]` | - | Lista com os nomes dos pacotes desejados. |
| `path` | `str` | `os.getcwd()` | O caminho da pasta onde serão adicionados os arquivos. |
| `dictionary` | `bool` | `True` | Indica se é para baixar o dicionário dos dados. |
| `years` | `list[int]` | `None` | Define os anos dos dados que serão baixados. |

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Baixar os packages de discentes e seus dados complementares, sem dicionários
ufrn_data.download_packages(['discentes', 'dados-complementares-de-discentes'], dictionary=False)
```

## download_packages_by_tag
Baixa pacotes pertencentes a uma etiqueta.

**Parâmetros**:

| Parâmetro | Tipo | Valor padrão | Descrição |
| --------- | ---- | ------------ | --------- |
| `tag` | `str` | - | Etiqueta desejada. |
| `path` | `str` | `os.getcwd()` | O caminho da pasta onde serão adicionados os arquivos. |

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Baixar os packages de discentes e seus dados complementares, sem dicionários
ufrn_data.download_packages_by_tag('graduacao')
```

## download_from_file
Baixa os pacotes de dados que estão escritos em um arquivo de texto.

**Parâmetros**:

| Parâmetro | Tipo | Valor padrão | Descrição |
| --------- | ---- | ------------ | --------- |
| `filename` | `str` | - | Nome do arquivo que contêm os pacotes. |
| `path` | `str` | `os.getcwd()` | O caminho da pasta onde serão adicionados os arquivos. |
| `dictionary` | `bool` | `True` | Indica se é para baixar o dicionário dos dados. |
| `years` | `list[int]` | `None` | Define os anos dos dados que serão baixados. |

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Baixar os packages escritos em um arquivo
ufrn_data.download_from_file('discentes_ufrn.txt')
```

**Observação**: Cada pacote deve ser declarado em uma linha, dessa forma, um arquivo com os pacotes de discentes ficaria assim ("discentes_ufrn.txt"):
```text
discentes
dados-complementares-de-discentes
dados-socio-economicos-de-discentes
```

## load_packages
Atualiza a lista de pacotes disponíveis. A lista com esses valores é a variável `available_packages`.

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Atualizando a lista de packages disponíveis
ufrn_data.load_packages()
# Acessando a lista de packages disponíveis
ufrn_data.available_packages
```

## print_files_from_package
Imprime no terminal a lista de arquivos referentes ao pacote de entrada.
Atualmente usa-se o cálculo de Levenshtein para verificar a similaridade
entre a entrada e os nomes dos pacotes.

**Parâmetros**:

| Parâmetro | Tipo | Valor padrão | Descrição |
| --------- | ---- | ------------ | --------- |
| `name` | `str` | - | Nome do pacote que será buscado. |

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Listar arquivos do pacote discentes
ufrn_data.print_files_from_package('discentes')

# Output:
# Ingressantes em 2019
# Ingressantes em 2018
# ...
# Dicionário de Dados - Discentes
```

## print_packages
Lista os pacotes de dados. Apresenta os elementos presentes na lista `available_packages`.

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Apresentando a lista de packages disponíveis
ufrn_data.print_packages()
```

## search_related_packages
Retorna uma lista de pacotes de dados relacionados a uma entrada.
Atualmente usa-se o cálculo de Levenshtein para verificar a similaridade
entre a entrada e os nomes dos pacotes.

**Parâmetros**:

| Parâmetro | Tipo | Valor padrão | Descrição |
| --------- | ---- | ------------ | --------- |
| `keyword` | `str` | - | Palavra-chave com a qual será feita a busca. |
| `simple_filter` | `bool` | `False` | Indica o uso de um filtro mais simples que o Levenshtein. |
| `search_tag` | `bool` | `False` | Flag que indica se a palavra-chave deve ser usada como etiqueta. |

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Procurar packages relacionados a discente
list_discentes = ufrn_data.search_related_packages('discente')
print(list_discentes)

# Output:
# ['dados-complementares-de-discentes', 'dados-socio-economicos-de-discentes', 'discentes']
```