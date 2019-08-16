from .utils import *
import tempfile


class Group(unittest.TestCase):
    def setUp(self):
        """Inicia novo objeto em todo os testes """
        self.ufrn_data = ODUFRNDownloader()

    def test_can_download_packages_from_file(self):
        """Verifica se dado um arquivo com pacotes realiza-se download."""
        with tempfile.NamedTemporaryFile() as tmp:
            tmp.write(b'telefones\n')
            tmp.write(b'unidades-academicas')
            tmp.seek(0)
            self.ufrn_data.download_from_file(tmp.name, './tmp')
            path_telefones = os.path.exists('./tmp/telefones')
            path_unidades = os.path.exists('./tmp/unidades-academicas')
            self.assertTrue(
                path_telefones and path_unidades
            )
            if os.path.exists('./tmp'):
                shutil.rmtree('./tmp')
