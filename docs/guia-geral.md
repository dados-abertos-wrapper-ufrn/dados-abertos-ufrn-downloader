# Geral
Como começar a usar o pacote:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()
```

# Métodos
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
| `load_tags` | Atualiza lista de etiquetas disponíveis. |
| `print_files_from_package` | Imprime no terminal a lista de arquivos referentes ao pacote de entrada. |
| `print_files_from_group` | Imprime no terminal a lista de arquivos referentes ao grupo de entrada. |
| `print_packages` | Lista os pacotes de dados. |
| `print_groups` | Lista os grupos de conjuntos de dados. |
| `print_tags` | Lista as etiquetas. |
| `search_by_tag` | Retorna uma lista de pacotes de dados relacionados a uma etiqueta. |
| `search_related_packages` | Retorna uma lista de pacotes de dados relacionados a uma entrada. |
| `search_related_groups` | Retorna uma lista de grupos de conjuntos de dados relacionados a uma entrada. |
