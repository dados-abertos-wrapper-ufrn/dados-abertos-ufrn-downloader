# Contribuindo

Ao contribuir com o odufrn-download, o primeiro passo é discutir as alterações desejadas,
via issue, utilizando a tag `question`. Criação de issues para reportar bugs e requisitar
funcionalidades são sempre bem vindas, assim como PR para melhorar os testes unitários.

Note que nós temos um [código de conduta](https://github.com/odufrn/.github/blob/master/CODE_OF_CONDUCT.md),
pedimos que ele seja seguido para interagir com o projeto.

## Processo de Pull Request

1. Pull requests devem passar pelo build do Travis e depois ser revisados pelos mantenedores.
2. Ao contribuir com o código deve-se escrever os testes e documentar as alterações.
3. Qualquer adição de dependência devem ser descritos na descrição do pull request.
4. Após a revisão de código por dois ou mais mantenedores, se aceitas as mudanças,
o pull request é aceito.
5. Os pulls request devem ser feitos para a branch development, pois as modicações serão 
lançadas na próxima versão do sistema.
6. Um mantenedor não pode aceitar o próprio pull request

## Instalando ambiente para desenvolvimento

Para instalar o pacote localmente utiliza-se o ` pip install -e . `. Instalado o pacote, basta
criar um arquivo no projeto e testar seu código, exemplo:

```python
from odufrn_downloader import ODUFRNDownloader

ufrn_data = ODUFRNDownloader()
ufrn_data.fun()
```

Após modificar o pacote e realizar os testes iniciais é necessário verificar se o código passa pelo
estilo pep8, utilizando ` find . -name \*.py -exec pycodestyle --ignore=E402 {} + ` e depois verificar
se todos os testes passaram, utilizando ` python -m unittest -v `, isso garante que o código irá passar
pelo build do travis.

Obs:. Não esqueça de escrever testes unitários para o que foi implementado, de documentar a função e de 
adicionar essa documentação em nossa ` /docs `.
