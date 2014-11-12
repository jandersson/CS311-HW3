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
    'RIGHT_PAREN': 26,
    'EOF': -1
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

input_string = "(sum + 47) / total"
input_list = []

def lookup(char):
    global next_token
    add_char()
    token_lookup.setdefault(char, 'DEFAULT')
    next_token = token_lookup[char]
    return next_token


def add_char():
    global lexeme
    lexeme += next_char


def get_char():
    global next_char, char_class
    if input_list:
        next_char = input_list.pop(0)
        if next_char.isalpha():
            char_class = 'LETTER'
        elif next_char.isdigit():
            char_class = 'DIGIT'
        else:
            char_class = 'UNKNOWN'
    else:
        char_class = 'EOF'


def get_non_blank():
    while next_char == " ":
        get_char()


def lex():
    global next_token, lex_len, lexeme
    lexeme = ""
    get_non_blank()
    if char_class == 'LETTER':
        add_char()
        get_char()
        while (char_class == 'LETTER') or (char_class == 'DIGIT'):
            add_char()
            get_char()
        next_token = 'IDENT'
    elif char_class == 'DIGIT':
        add_char()
        get_char()
        while char_class == 'DIGIT':
            add_char()
            get_char()
        next_token = 'INT_LIT'
    elif char_class == 'UNKNOWN':
        lookup(next_char)
        get_char()
    elif char_class == 'EOF':
        next_token = 'EOF'
        lexeme = 'EOF'
    print("Next token is: " + str(token_codes[next_token]) + ", Next Lexeme is " + lexeme)
    if not input_list:
        print("Next token is: " + "-1" + ", Next Lexeme is " + "EOF")
    return next_token


if __name__ == '__main__':
    for char in input_string:
        input_list.append(char)
    get_char()
    while input_list:
        lex()