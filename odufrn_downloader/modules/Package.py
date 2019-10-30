import os
import requests
from .Env import Env
from ..mixins.FilterMixin import FilterMixin
from .Tag import Tag


class Package(Env, FilterMixin):
    """Classe responsável pelo download de pacotes.

    Atributos
    ---------
    url_package: str
        a url para a consulta de pacotes da API da UFRN.
    available_packages: list
        lista de pacotes de dados que estão disponíveis para download.
    tag: Tag
        instância da classe Tag usada na classe.
    """

    def __init__(self):
        super().__init__()

        self.url_package = self.url_base + 'api/rest/dataset/'
        self.available_packages = []
        self.load_packages()
        self.tag = Tag()

    def _get_related_package_search(self, keyword: str,
                                    dictionary: bool = False):
        """Retorna packages relacionados de acordo com o nome

        Parâmetros
        ----------
        keyword: str
            keyword que deseja pesquisar similaridade
        """
        url_search_related = self.url_base + 'api/action/package_search?q='
        request = self._request_get(url_search_related + keyword)
        list_related_packages = []
        for response in request['result']['results']:
            for r in response['resources']:
                if not dictionary and 'Dicion' in r['name']:
                    continue
                list_related_packages.append(r['name'])

        return list_related_packages

    def load_packages(self):
        """Atualiza lista de pacotes disponíveis."""
        self.available_packages = self._load_list('package_list')

    def print_packages(self):
        """Lista os conjuntos de dados."""
        self._print_list("pacotes de dados", self.available_packages)

    def download_package(self, name: str, path: str = os.getcwd(),
                         dictionary: bool = True, years: list = None):
        """Exibe pacote de dados de acordo com seu nome
        e baixa-os em pastas com o nome do respectivo
        conjunto de dado.

        > Exemplo: download_package('acervo-biblioteca')

        Parâmetros
        ----------
        name: str
            nome do pacote.
        path: str
            o caminho da pasta onde serão adicionados os arquivos
            (por padrão, a pasta atual).
        dictionary: bool
            flag para baixar o dicionário dos dados (por padrão, True).
        years: list
            define os anos dos dados que serão baixados, se existir
            realiza-se o download.
        """

        # Checa se o pacote está disponível
        if not (name in self.available_packages) and self.warnings:
            self._print_not_found(name, 'Pacote')
            return

        response = self._request_get(self.url_package + name)
        path = self._make_dir('{}/{}'.format(path, name))

        try:
            for resource in response['resources']:
                year_find = self.year_find(resource['name'], years)

                if not dictionary and 'Dicion' in resource['name']:
                    continue

                if years is None or year_find:
                    print("Baixando {}...".format(resource['name']))
                    file_path = '{}/{}.{}'.format(
                        path, resource['name'], resource['format'].lower()
                    )

                    with open(file_path, 'wb') as f:
                        f.write(requests.get(resource['url']).content)
        except Exception as ex:
            self._print_exception(ex)

    def download_packages(self, packages: list, path: str = os.getcwd(),
                          dictionary: bool = True, years: list = None):
        """Exibe os pacotes de dados de acordo com seu nome
        e baixa-os em pastas com o nome do respectivo
        conjunto de dado.

        > Exemplo: download_packages(['discentes', \
            'dados-complementares-de-discentes'])

        Parâmetros
        ----------
        packages: list
            lista com os nomes dos pacotes desejados.
        path: str
            o caminho da pasta onde serão adicionados os arquivos.
            (por padrão, a pasta atual).
        dictionary: bool
            flag para baixar o dicionário dos dados (por padrão, True).
        years: list
            define os anos dos dados que serão baixados, se existir
            realiza-se o download.
        """
        for package in packages:
            self.download_package(package, path, dictionary, years)

    def search_related_packages(self, keyword: str,
                                simple_filter: bool = False,
                                related_search: bool = False,
                                search_tag: bool = False) -> list:
        """Procura os pacotes de dados que possuam nomes
        semelhantes à palavra recebida.

        > Exemplo: search_related_packages('discente')

        Parâmetros
        ----------
        keyword: str
            palavra-chave com a qual será feita a busca.
        simple_filter: bool = False
            indica o uso de um filtro mais simples que o Levenshtein.
        search_tag: bool
            flag que indica se a palavra-chave deve ser usada como etiqueta
            (por padrão, False).
        """
        # Busca nomes de pacotes semelhantes à palavra passada
        if simple_filter:
            related = self.simple_search(keyword, self.available_packages)
        elif related_search:
            related = self._get_related_package_search(keyword)
        else:
            related = self.search_similar(keyword, self.available_packages)

        # Busca nomes relacionados à tag, se for o caso
        if search_tag:
            packages = self.tag.search_by_tag(keyword)
            for package in packages:
                if package not in related:
                    related.append(package)

        # Imprime exceção se não houver pacotes similares
        if not len(related) and self.warnings:
            self._print_not_relation(keyword, 'Package')

        return related

    def download_all(self, path: str = os.getcwd(),
                     dictionary: bool = True, years: list = None):
        """Exibe todos os pacotes de dados e baixa-os
        em pastas com o nome do respectivo conjunto de dado.

        > Exemplo:
            download_all(dictionary = False, years = list(range(2009, 2014)))

        Parâmetros
        ----------
        path: str
            o caminho da pasta onde serão adicionados os arquivos
            (por padrão, a pasta atual).
        dictionary: bool
            flag para baixar o dicionário dos dados (por padrão, True).
        years: list
            define os anos dos dados que serão baixados, se existir
            realiza-se o download.
        """
        self.download_packages(
            self.available_packages, path, dictionary, years
        )

    def download_packages_by_tag(self, tag: str, path: str = os.getcwd()):
        """ Baixa pacotes pertencentes a uma etiqueta.

        Parâmetros
        ----------
        tag: str
            etiqueta desejada.
        path: str
            o caminho da pasta onde serão adicionados os arquivos
            (por padrão, a pasta atual).
        """
        # Recupera pacotes
        packages = self.tag.search_by_tag(tag)

        self.download_packages(packages, path)

    def print_files_from_package(self, name: str):
        """Printa os arquivos do pacote.

        Parâmetros
        ----------
        name: str
            nome do recurso a ser pesquisado.
        """
        request = self._request_get(self.url_package + name)
        try:
            for resource in request['resources']:
                print(resource['url'].split('/')[-1])
        except TypeError as e:
            self._print_exception(
                e, self.str_related(self.search_related_packages(name))
            )
