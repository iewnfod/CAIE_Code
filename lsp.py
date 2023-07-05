from lsprotocol.types import *
from pygls.server import LanguageServer

from main import *
from src.AST.data import stack

cpc_server = LanguageServer('cpc', 'v0.1.0')

@cpc_server.feature(INITIALIZE)
def initialize(params: InitializeParams):
    # 预加载文件
    preload_scripts()

@cpc_server.feature(TEXT_DOCUMENT_COMPLETION)
def completion(params: CompletionParams):
    variables = []
    functions = []
    for space_name, space_vars, space_functions in stack.spaces:
        for v in space_vars.keys():
            variables.append(CompletionItem(label=v))
        for f in space_functions.keys():
            functions.append(CompletionItem(label=f))

    return CompletionList(
        is_incomplete=False,
        items=variables
    )


# 运行
def __init__():
    cpc_server.start_tcp('127.0.0.1', 8080)
