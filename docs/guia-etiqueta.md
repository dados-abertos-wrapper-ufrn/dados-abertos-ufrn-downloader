# Tag
Os métodos aqui apresentados são referentes ao uso de etiquetas de pacotes (listagem, busca, etc).

## load_tags
Atualiza a lista de etiquetas disponíveis. A lista com esses valores é a variável `available_tags`.

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Atualizando a lista de grupos disponíveis
ufrn_data.load_tags()
# Acessando a lista de grupos disponíveis
ufrn_data.available_tags
```

## print_tags
Imprime as etiquetas disponíveis. Apresenta os elementos presentes na lista `available_tags`.

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Apresentando a lista de grupos de pacotes disponíveis
ufrn_data.print_tags()
```

## search_by_tag
Busca pacotes com base em etiqueta.

**Parâmetros**:

| Parâmetro | Tipo | Valor padrão | Descrição |
| --------- | ---- | ------------ | --------- |
| `tag` | `str` | - | Etiqueta desejada. |

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Procurar grupos relacionados a pesquisa
list_tags = ufrn_data.search_by_tag('graduacao')
print(list_tags)

# Output:
# ['cursos-de-graduacao', 'discentes', 'turmas', 'cursos-ufrn', 'estruturas-curriculares']
```
