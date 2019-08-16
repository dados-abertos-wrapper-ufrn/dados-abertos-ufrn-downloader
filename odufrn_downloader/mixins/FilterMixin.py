from .filters.LevenshteinMixin import LevenshteinMixin
from .filters.SimpleSearchMixin import SimpleSearchMixin
from .filters.YearsMixin import YearsMixin


class FilterMixin(LevenshteinMixin, SimpleSearchMixin, YearsMixin):
    """Mixin que engloba os métodos de filtros."""
