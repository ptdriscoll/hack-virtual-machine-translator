class SymbolTable:
    ##predefined symbols
    preSymbols = {'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4, 'R0': 0,
                  'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7,
                  'R8': 8, 'R9': 9,' R10': 10, 'R11': 11, 'R12': 12, 'R13': 13,
                  'R14': 14, 'R15': 15, 'SCREEN': 16384, 'KBD': 24576}
    
    def __init__(self):
        """Creates a new empty symbol table fill with predefined symbols"""
        self.s_table = SymbolTable.preSymbols

    def contains(self, symbol):
        """Does the symbol table contain the given symbol? """
        return symbol in self.s_table

    def address(self, symbol):
        """Return the address associated with the symbol """
        return self.s_table[symbol]

    def addPair(self, symbol, address):
        """Adds the pair (symbol, address) to the table"""
        self.s_table[symbol] = address
