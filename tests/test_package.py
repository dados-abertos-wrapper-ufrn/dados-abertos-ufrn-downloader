from .utils import *


class Package(unittest.TestCase):
    def setUp(self):
        """Inicia novo objeto em todo os testes."""
        self.ufrn_data = ODUFRNDownloader()

    def test_can_print_packages(self):
        """Verifica se a lista de packages é impressa na tela."""
        assert_console(self.ufrn_data.print_packages)

    def test_can_load_packages(self):
        """Verifica se a lista de packages é carregada no objeto."""
        self.ufrn_data.load_packages()
        self.assertTrue(len(self.ufrn_data.available_packages) > 0)

    def test_search_packages(self):
        """Verifica se a procura por pacotes está funcionando."""
        list_groups = self.ufrn_data.search_related_packages('discent')
        self.assertTrue(len(list_groups) == 3)
        list_groups = self.ufrn_data.search_related_packages('disc', True)
        self.assertTrue(len(list_groups) == 3)
        list_groups = self.ufrn_data.search_related_packages('disc')
        self.assertTrue(len(list_groups) == 0)

    def test_can_print_files_from_package(self):
        """Verifica se os arquivos de um pacote podem ser impressos na tela."""
        assert_console(
            lambda: self.ufrn_data.print_files_from_package('discentes')
        )

    def test_can_print_files_from_package_with_typo(self):
        """Verifica se o tratamento de erro com o Levenshtein funciona."""
        assert_console(
            lambda: self.ufrn_data.print_files_from_package('discente')
        )
