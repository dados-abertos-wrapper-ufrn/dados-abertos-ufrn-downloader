import os
from .Package import Package


class Group(Package):
    """Classe responsável pelo download de grupos de pacotes.

    Atributos
    ---------
    url_group: str
        a url para a consulta de grupos de conjuntos de dados da API da UFRN.
    available_groups: list
        lista de grupos de conjuntos de dados que estão disponíveis
        para download.
    """

    def __init__(self):
        super().__init__()

        self.url_group = self.url_base + 'api/rest/group/'
        self.available_groups = []
        self.load_groups()

    def load_groups(self):
        """Atualiza lista de grupos de pacotes disponíveis."""
        self.available_groups = self._load_list('group_list')

    def print_groups(self):
        """Imprime os grupos de pacotes."""
        self._print_list("grupos de dados", self.available_groups)

    def get_packages_group(self, name: str):
        """Imprime os packages que possuem no grupo

        Parâmetros
        ----------
        name: str
            nome do grupo
        """

        # Checa se o grupo está disponível
        if not (name in self.available_groups):
            print("O grupo de dados \"{}\" não foi encontrado.".format(name))
            return

        response = self._request_get(self.url_group + name)

        return response['packages']

    def download_group(self, name: str, path: str = os.getcwd(),
                       dictionary: bool = True, years: list = None):
        """Exibe grupo de pacotes de acordo com seu nome
        e baixa-os em pastas com o nome do respectivo
        grupo de dados.

        > Exemplo: download_group('pessoas')

        Parâmetros
        ----------
        name: str
            nome do grupo.
        years: list
            define os anos dos dados que serão baixados, se existir
            realiza-se o download.
        path: str
            o caminho da pasta onde serão adicionados os arquivos
            (por padrão, a pasta atual).
        dictionary: bool
            flag para baixar o dicionário dos dados (por padrão, True).
        """

        # Checa se o grupo está disponível
        if not (name in self.available_groups) and self.warnings:
            self._print_not_found(name, 'Grupo')
            return

        groups = self._request_get(self.url_group + name)
        path = self._make_dir('{}/{}'.format(path, name))

        try:
            for package in groups['packages']:
                self.download_package(package, path, dictionary, years)

        except Exception as ex:
            self._print_exception(ex)

    def download_groups(self, groups: list, path: str = os.getcwd(),
                        dictionary: bool = True, years: list = None):
        """Exibe os grupos de pacotes de acordo com seu nome
        e baixa-os em pastas com o nome do respectivo
        grupo de dados.

        > Exemplo: download_groups(['biblioteca', 'ensino'])

        Parâmetros
        ----------
        groups: list
            lista com os nomes dos grupos desejados.
        years: list
            define os anos dos dados que serão baixados, se existir
            realiza-se o download.
        path: str
            o caminho da pasta onde serão adicionados os arquivos
            (por padrão, a pasta atual).
        dictionary: bool
            flag para baixar o dicionário dos dados (por padrão, True).
        """

        for group in groups:
            self.download_group(group, path, dictionary, years)

    def search_related_groups(self, keyword: str,
                              simple_filter: bool = False) -> list:
        """Procura os grupos de pacotes que possuam nomes
        semelhantes à palavra recebida.

        > Exemplo: search_related_groups('pesquisa')

        Parâmetros
        ----------
        keyword: str
            palavra-chave com a qual será feita a busca.
        simple_filter: bool = False
            indica o uso de um filtro mais simples que o Levenshtein.
        """
        # Busca nomes de grupos semelhantes à palavra passada
        if simple_filter:
            related = self.simple_search(keyword, self.available_groups)
        else:
            related = self.search_related(keyword, self.available_groups)

        # Imprime exceção se não houver grupos similares
        if not len(related) and self.warnings:
            self._print_not_relation(keyword, 'Grupo')

        return related

    def print_files_from_group(self, name: str):
        """Printa os arquivos dos pacotes de um grupo.

        > Exemplo: print_files_from_group('processos')

        Parâmetros
        ----------
        name: str
            nome do recurso a ser pesquisado.
        """
        try:
            for resource in self.get_packages_group(name):
                self.print_files_from_package(resource)
        except TypeError as e:
            self._print_exception(
                e, self.str_related(self.search_related_packages(name))
            )
