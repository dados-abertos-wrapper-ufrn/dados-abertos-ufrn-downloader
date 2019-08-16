from .utils import *


class Tag(unittest.TestCase):
    def setUp(self):
        """ Inicia novo objeto em todo os testes """
        self.ufrn_data = ODUFRNDownloader()

    def test_can_print_packages(self):
        """ Verifica se a lista de tags é impressa na tela """
        assert_console(self.ufrn_data.print_tags)

    def test_can_load_packages(self):
        """ Verifica se a lista de packages é carregada no objeto """
        self.ufrn_data.load_packages()
        self.assertTrue(len(self.ufrn_data.available_tags) > 0)

    def test_search_tags(self):
        """Verifica se a procura por etiquetas está funcionando."""
        list_tags = self.ufrn_data.search_related_packages('graduacao',
                                                           search_tag=True)
        expected = ['cursos-de-graduacao', 'cursos-de-pos-graduacao',
                    'programas-de-pos-graduacao', 'discentes', 'turmas',
                    'cursos-ufrn', 'estruturas-curriculares']
        self.assertTrue(sorted(list_tags) == sorted(expected))

        packages = self.ufrn_data.search_by_tag('graduacao')
        expected = ['cursos-de-graduacao', 'discentes', 'turmas',
                    'cursos-ufrn', 'estruturas-curriculares']
        self.assertTrue(sorted(packages) == sorted(expected))
