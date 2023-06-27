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

class For:
    def __init__(self, id, left, right, body_statement, next_id):
        self.type = 'FOR'
        self.id = id
        self.left = left
        self.right = right
        self.body_statement = body_statement
        self.next_id = next_id

    def get_tree(self, level=0):
        result = LEVEL_STR * level
        result += 'FOR\n' + str(self.id)
        result += '\n' + self.left.get_tree(level+1) + '\n' + str(self.right.get_tree(level+1))
        result += 'NEXT\n' + str(self.next_id)

    def exe(self):
        left = self.left.exe()
        right = self.right.exe()
        if left[1] == 'INTEGER' and right[1] == 'INTEGER':
            for i in range(left[0], right[0]+1):
                # 给 index 赋值
                stack.new_variable(self.id, 'INTEGER')
                stack.set_variable(self.id, i, 'INTEGER')
                # 执行内部操作
                self.body_statement.exe()
                # 核对id是否相同
                if self.id == self.next_id:
                    continue
                else:
                    print(f'Expect `{self.id}` for next id, but found `{self.next_id}`')
                    break
        else:
            print(f'Expect `INTEGER` for index, but found `{left[1]}` and `{right[1]}`. ')
