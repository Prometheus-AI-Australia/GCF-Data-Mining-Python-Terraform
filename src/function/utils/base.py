

class LazyClient:
    """Lazily initialises the meta client. Helpful for shimming during testing."""

    def __init__(self):
        self.client = lambda: None
        self._initialised = False

    def lazy_init(self, f):

        def wrapper(*args, **kwargs):
            if not self._initialised:
                self.client = self.client()
                self._initialised = True
            return f(*args, **kwargs)

        return wrapper
