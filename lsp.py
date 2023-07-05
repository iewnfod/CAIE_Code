from lsprotocol import types
from pygls.server import LanguageServer

class cpc_server(LanguageServer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.documents = {}

    @self.feature(types.INITIALIZE)
    def initialize(self, params: types.InitializeParams):
        opts = params.initialization_options
        method = getattr(opts, 'method', 'builtin')
