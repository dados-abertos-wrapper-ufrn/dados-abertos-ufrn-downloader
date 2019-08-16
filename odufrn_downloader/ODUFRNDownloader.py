from .modules.Group import Group
from .modules.File import File
from .modules.Tag import Tag


class ODUFRNDownloader(Group, File, Tag):
    """Classe que reune todos os módulos do pacote."""

    def __init__(self):
        super().__init__()
