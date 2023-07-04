from src.global_var import *
from src.lex import *
from src.parse import *
from ply import yacc
from ply import lex
import chardet
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Language Server for CAIE Pseudocode!'

app.run()
