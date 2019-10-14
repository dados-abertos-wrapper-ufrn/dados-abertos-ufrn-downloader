from .utils import *


class Group(unittest.TestCase):
    def setUp(self):
        """Inicia novo objeto em todo os testes """
        self.ufrn_data = ODUFRNDownloader()

    def test_can_print_groups(self):
        """Verifica se a lista de grupos é impressa na tela """
        assert_console(self.ufrn_data.print_groups,"""Os grupos de dados disponíveis são:
[   'biblioteca',
    'comunicados-e-documentos',
    'contratos-e-convenios',
    'despesas-e-orcamento',
    'ensino',
    'extensao',
    'institucional',
    'materiais',
    'patrimonio',
    'pesquisa',
    'pessoas',
    'processos']\n""")

    def test_can_load_groups(self):
        """Verifica se a lista de grupos é carregada no objeto """
        self.ufrn_data.load_groups()
        self.assertTrue(len(self.ufrn_data.available_groups) > 0)

    def test_can_get_packages_group(self):
        """Verifica se a lista de datasets em um grupo é retornada."""
        group = 'extensao'
        self.assertTrue(len(self.ufrn_data.get_packages_group(group)) > 0)

    def test_can_raise_exception_on_get_packages_group(self):
        """Verifica se digitando um nome errado de um grupo
        consegue-se lançar exceção de grupo não encontrado."""
        group = 'despesas-e-orcam'
        self.assertTrue(
            "não foi encontrado" in (
                input_value(lambda: self.ufrn_data.get_packages_group(group))
            )
        )

    def test_can_download_group(self):
        """Verifica se baixa-se arquivos de um grupo."""
        self.ufrn_data.download_group('extensao', './tmp')
        self.assertTrue(os.path.exists('./tmp/extensao'))
        if os.path.exists('./tmp'):
            shutil.rmtree('./tmp')

    def test_can_download_groups(self):
        """Verifica se baixa-se arquivos de vários grupos."""
        self.ufrn_data.download_groups(['biblioteca', 'extensao'], './tmp')
        path_extensao = os.path.exists('./tmp/extensao')
        path_biblioteca = os.path.exists('./tmp/biblioteca')
        self.assertTrue(
            path_extensao and path_biblioteca
        )
        if os.path.exists('./tmp'):
            shutil.rmtree('./tmp')

    def test_can_search_groups(self):
        """Verifica se a procura por grupos está funcionando."""
        list_groups = self.ufrn_data.search_related_groups('pesquis')
        self.assertTrue(len(list_groups) == 1)
        list_groups = self.ufrn_data.search_related_groups('pesq', True)
        self.assertTrue(len(list_groups) == 1)
        self.ufrn_data.warnings = True
        list_groups = self.ufrn_data.search_related_groups('pesq')
        self.assertTrue(len(list_groups) == 0)

    def test_can_print_files_from_group(self):
        """Verifica se os arquivos de um grupo podem ser impresso na tela."""
        #Uma vez que os arquivos não são estáticos
        #e que a extensão de alguns pode mudar, não seria
        #dinâmico fazer esse assert com mensagem especificada (message!=None)
        assert_console(
            lambda: self.ufrn_data.print_files_from_group('processos')
        )

    def test_can_print_files_from_group_with_typo(self):
        """Verifica se o tratamento de erro com o Levenshtein funciona."""
        assert_console(
            lambda: self.ufrn_data.print_files_from_package('process'),"""[91mTypeError[0m

Você pode estar procurando por processos ou processos-seletivos\n"""
        )
