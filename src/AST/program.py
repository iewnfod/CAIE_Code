from src.AST.data import *

class Statements:
    def __init__(self):
        self.type = 'STATEMENTS'
        self.statements = []

    def add_statement(self, statement):
        self.statements.append(statement)

    def get_tree(self, level=0):
        result = ''
        for statement in self.statements:
            result += '\n' + statement.get_tree(level)
        return result

    def exe(self):
        result = []
        for statement in self.statements:
            try:
                result.append(statement.exe())
            except Exception as e:
                raise e

        return result

class If:
    def __init__(self, condition, true_statement, false_statement=None):
        self.type = 'IF'
        self.condition = condition
        self.true_statement = true_statement
        self.false_statement = false_statement

    def get_tree(self, level=0):
        result = LEVEL_STR * level
        result += 'IF\n' + self.condition.get_tree(level+1)
        result += '\n' + self.true_statement.get_tree(level+1)
        result += ( 'ELSE\n' + self.false_statement.get_tree(level+1) ) if self.false_statement else ''

        return result

    def exe(self):
        if self.condition.exe()[0]:
            self.true_statement.exe()
        else:
            if self.false_statement:
                self.false_statement.exe()
