class SymbolTable:
    def __init__(self):
        self.tables = []

        self.open_scope()

    def add_symbol(self, name, c_type, size, binding, scope_type):
        curr_table = self.tables[len(self.tables) - 1]
        curr_table[name] = {'name': name,
                            'c_type': c_type,
                            'size': size,
                            'binding': binding,
                            'scope_type': scope_type}
    
    def lookup(self, name):
        symbol = None
        for table in self.tables[::-1]:
            print(table)
            print()
            if name in table:
                symbol = table[name]
                break
        print(symbol)
        return symbol

    def open_scope(self):
        self.tables.append({})
    
    def close_scope(self):
        self.tables.pop()