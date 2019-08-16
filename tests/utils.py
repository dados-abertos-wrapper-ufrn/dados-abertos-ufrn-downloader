import io
import sys
import unittest
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from odufrn_downloader import ODUFRNDownloader


def input_value(fun):
    """Recebe função que imprime algo na tela e retorna impressao."""
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    fun()
    sys.stdout = sys.__stdout__
    return capturedOutput.getvalue()


def assert_console(fun):
    """Recebe função que printa algo na tela e realiza assert
    que verifica se foi printado."""
    unit = unittest.TestCase()
    return unit.assertTrue(len(input_value(fun)) > 0)
