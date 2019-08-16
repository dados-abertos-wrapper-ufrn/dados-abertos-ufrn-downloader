from abc import ABC
import requests
import os
import pprint


class Env(ABC):
    """Classe com os atributos e métodos responsáveis pelo
    funcionamento correto do pacote.

    Atributos
    ---------
    url_base: str
        a url para a API de dados abertos da UFRN.
    url_action: str
        a url para a página de ações da API.
    """

    """Constante com mensagens de erros"""
    MSG_ERRORS = {
        'download_error': (
            "Ocorreu algum erro durante o download do pacote."
            "Verifique sua conexão, o nome do conjunto de dados"
            "e tente novamente."
        ),
        'none_package': 'Nenhum pacote foi encontrado',
    }

    def __init__(self):
        self.url_base = 'http://dados.ufrn.br/'
        self.url_action = self.url_base + 'api/action/'
        self.warnings = False

    def _print_exception(self, ex: Exception,
                         msg: str = MSG_ERRORS['download_error']):
        """Imprime mensagem padrão para exceções."""
        print('\033[91m{}\033[0m'.format(ex))
        print(msg)

    def _print_not_found(self, name: str, type_name: str):
        """Imprime mensagem padrão para nome de dados não encontrados.
        """
        print('{} de dados "{}" não foi encontrado.'.format(type_name, name))

    def _print_not_relation(self, name: str, type_name: str):
        """Imprime mensagem padrão para nome de dados semelhantes não
        encontrados.
        """
        print('Não há {} semelhante a {}'.format(type_name, name))

    def _print_list(self, name: str, variable: list):
        """Mostra na tela a lista desejada."""
        print("Os {} disponíveis são:".format(name))
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(variable)

    def _load_list(self, option: str) -> list:
        """Atualiza a lista desejada através de uma consulta.

        Parâmetros
        ----------
        option: str
            indica o que se deseja consultar pelo request.
        """
        try:
            packages = requests.get(self.url_action + option).json()
            return packages['result']
        except Exception as ex:
            self._print_exception(ex)

    def _make_dir(self, path: str) -> str:
        """Cria o diretório, caso ele não exista.

        Parâmetros
        ----------
        path: str
            o caminho da pasta onde serão adicionados os arquivos."""
        if not os.path.exists(path):
            os.makedirs(path)

        return path

    def _request_get(self, url: str) -> dict:
        """Realiza a requisição desejada e retorna os dados
        e o caminho formado para download.

        Parâmetros
        ----------
        url: str
            a url que se deseja realizar a requisição.

        Retorno
        ----------
        dict:
            a resposta da requisição em json (dicionário)."""
        request_get = requests.get(url)

        return request_get.json()
