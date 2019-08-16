class LevenshteinMixin:
    """Mixin relacionado ao calculo de similaridade entre duas palavras."""

    def levenshtein(self, str1: list, str2: list) -> float:
        """Calcula a similaridade entre duas palavras de acordo com a
        distância de Levenshtein.

        Parâmetros
        ----------
        str1: list
            lista de caracteres da primeira palavra.
        str2: list
            lista de caracteres da segunda palavra.

        Retorno
        -------
        razão entre as palavras. Quanto mais próximo de 1,
        mais similares são as palavras.

        Referência
        ----------
        https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
        """
        oneago = None
        thisrow = list(range(1, len(str2) + 1)) + [0]
        for x in range(len(str1)):
            _, oneago, thisrow = oneago, thisrow, [0] \
                * len(str2) + [x + 1]
            for y in range(len(str2)):
                delcost = oneago[y] + 1
                addcost = thisrow[y - 1] + 1
                subcost = oneago[y - 1] + (str1[x] != str2[y])
                thisrow[y] = min(delcost, addcost, subcost)
        lens = len(str1) + len(str2)
        ratio = (lens - thisrow[len(str2) - 1]) / lens
        return ratio

    def search_related(self, keyword: str, input_list: list,
                       split: bool = True) -> list:
        """Busca na input_list os elementos com nomes semelhantes
        à keyword recebida.

        Parâmetros
        ----------
        keyword: str
            palavra-chave com a qual será feita a busca.
        input_list: list
            lista com os valores que irá verificar a similaridade com keyword.
        split: bool
            flag que indica se a palavra-chave deve ser dividida.

        Retorno
        -------
        lista de valores com nome similares à palavra de interesse.
        """
        str1 = list(keyword)
        filter_list = []

        for item in input_list:
            items = item.split('-') if split else [item]
            for word in items:
                ratio = self.levenshtein(str1, list(word))
                if ratio > 0.87:
                    filter_list.append(item)
                    continue

        return filter_list

    def str_related(self, related_packages: list):
        """Formata mensagem de lista com buscas relacionadas.

        Parâmetros
        ----------
        related_packages: list
            lista de palavras relacionadas.
        Retorno
        -------
        string "" se lista vazia, formatada caso contrário.
        """
        msg = " ou ".join(related_packages)
        if msg == "":
            return msg

        return "\nVocê pode estar procurando por {}".format(msg)
