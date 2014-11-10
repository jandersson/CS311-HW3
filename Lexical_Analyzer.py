__author__ = 'jonas'

'''
The purpose of this program is to do lexical analysis on arithmetic
expressions. This program uses a hardcoded string to represent the
input to minimize code.
'''

token_codes = {
    'INT_LIT': 10,
    'IDENT': 11,
    'ASSIGN_OP': 20,
    'ADD_OP': 21,
    'SUB_OP': 22,
    'MULT_OP': 23,
    'DIV_OP': 24,
    'LEFT_PAREN': 25,
    'RIGHT_PAREN': 26
}
token_lookup = {
    '(': 'LEFT_PAREN',
    ')': 'RIGHT_PAREN',
    '+': 'ADD_OP',
    '-': 'SUB_OP',
    '*': 'MULT_OP',
    '/': 'DIV_OP'
}
character_classes = {
    'LETTER': 0,
    'DIGIT': 1,
    'UNKNOWN': 99
}
lexeme = []
next_char = None
input_string = "1 + 2 * 3 * (4 + 5)"
input_list = []
char_class = None

for char in input_string:
    input_list.append(char)

def lookup(char):
    add_char()
    nextToken = token_lookup[char]


def add_char():
    global lexeme
    if lex_len <= 98:
        lexeme.append(next_char)
    else:
        print("Error - Lexeme is too long.")
    pass


def get_char():
    global next_char, char_class
    next_char = input_list.pop()
    if char.isalpha():
        char_class = 'LETTER'
    elif next_char.isdigit():
        char_class = 'DIGIT'
    else:
        char_class = 'UNKNOWN'


def get_non_blank():
    pass


def lex():
    pass

