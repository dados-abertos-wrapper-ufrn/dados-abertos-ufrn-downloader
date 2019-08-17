import os
import requests
from .Env import Env
from ..mixins.FilterMixin import FilterMixin


class Tag(Env, FilterMixin):
    """Classe responsável pelo tratamento de pacotes por etiqueta.

    Atributos
    ---------
    url_tag: str
        a url para a consulta de etiquetas da API da UFRN.
    available_tags: list
        lista de etiquetas que estão disponíveis.
    """

    def __init__(self):
        super().__init__()

        self.url_tag = self.url_base + 'api/rest/tag'
        self.available_tags = []
        self.load_tags()

    def load_tags(self):
        """Atualiza lista de etiquetas disponíveis."""
        self.available_tags = self._load_list('tag_list')

    def print_tags(self):
        """Imprime as etiquetas."""
        self._print_list("etiquetas", self.available_tags)

    def search_by_tag(self, tag: str) -> list:
        """ Busca pacotes com base em etiqueta.

        Parâmetros
        ----------
        tag: str
            etiqueta desejada
        """

        tags = self.search_related(tag, self.available_tags, False)
        # Imprime exceção se não houver pacotes
        if not len(tags) and self.warnings:
            self._print_not_relation(tag, 'Tag')

        packages = []
        for key in tags:
            url = self.url_tag + "/" + key
            package = self._request_get(url)
            packages += package

        return packages
