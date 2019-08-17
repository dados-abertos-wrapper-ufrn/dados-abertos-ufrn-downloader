class YearsMixin:
    """Mixin que adiciona métodos relacionados a filtragem
    de pacotes e grupos por anos"""

    def year_find(self, package_name: str, years: list) -> bool:
        """Verifica se o pacote pertence a uma ano específico da lista years.

        Parâmetros
        ----------
        package_name: str
            nome do pacote a ser filtrado.
        years: list
            anos que serão filtrados na pesquisa.

        Retorno
        ----------
        bool
            True se o ano foi encontrado no nome do pacote se não false."""
        if years is None:
            return True

        if years:
            for _, year in enumerate(years):
                if str(year) in package_name:
                    return True
        return False
