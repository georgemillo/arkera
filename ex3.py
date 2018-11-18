import unittest

class Query:
    def __init__(self, tableName):
        self.tableName = tableName
        self.conditions = []


    def addCondition(self, condition):
        self.conditions.append(condition)


    def toSql(self):
        conds = ' AND '.join(map(lambda c: c.toSql(), self.conditions))
        return 'SELECT * FROM ' + self.tableName + ' WHERE ' + conds


        

class Condition:
    OPERATORS = ['IN', 'NOTIN', '=', '<', '>']

    def __init__(self, colName, operator, value):
        self.colName = colName
        if not (operator in self.OPERATORS):
            raise "Unrecognised operator '" + operator + "'"
        self.operator = operator
        self.value = value


    def toSql(self):
        return self.colName + ' ' + self.operator + ' ' + self.value
        
        

class TestQuery(unittest.TestCase):
    def test(self):
        query = Query('widgets')
        query.addCondition(Condition('id', '=', '123'))
        self.assertEqual(query.toSql(), 'SELECT * FROM widgets WHERE id = 123')

        query = Query('widgets')
        query.addCondition(Condition('id', 'NOTIN', '[123, 456]'))
        query.addCondition(Condition('rating', '>', '5'))
        query.addCondition(Condition('url', '=', '"example.com"'))
        self.assertEqual(
            query.toSql(),
            'SELECT * FROM widgets WHERE id NOTIN [123, 456] AND rating > 5 AND url = "example.com"'
        )


if __name__ == '__main__':
    unittest.main()
