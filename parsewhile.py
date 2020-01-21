#There are three types syntaxs Aexpr Bexpr and Satements
#All token types for INT, VAR, BOOL, ARR, PLUS, MINUS, MUL, LESSTHAN, EQUAL, NOT, AND, OR, SKIP, ASSIGN, WHILE, { , }, IF, THEN, ELSE ;

#Additonal feature is array
#states managed by python dictionary

'''
uncomment this when it is all done.
import sys
sys.tracebacklimit = 0
'''
#lexer
class Token():
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __repr__(self):
        return 'Token({type}, {value})'.format(type = self.type, value = self.value)

class Lexer():
    def __init__(self, text):
        self.text = text
        #keep track of reading 
        self.pos = 0
        self.current_char = self.text[self.pos]

    def Error(self):
        raise Exception("This input is not supported")

    #increase the cursor to the next position, if valid then set current_char to the new char
    def next(self):
        self.pos += 1
        #check if it is the end of line
        if self.pos > len(self.text)-1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
    
    #skip all spaces and new lines
    def skipchar(self):
        #spaces work but linebreak is still a bit funky
        while self.current_char is not None and self.current_char in (" ", "\n", "\r"):
            self.next()
#All token types for  ARR, PLUS, MINUS, MUL, LESSTHAN, EQUAL, NOT, AND, OR, SKIP, ASSIGN, WHILE, { , }, IF, THEN, ELSE ;    
    def num(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result = result + self.current_char
            self.next()
        return int(reuslt)

    def bool(self):
        result = ''
        if self.current_char == 't':
            while self.current_char is not None and self.current_char in ('t', 'r', 'u', 'e'):
                result = result + self.current_char
                self.next()
            if result == "true":
                return True
            else:
                self.error()
        else:
            while self.current_char is not None and self.current_char in ('f', 'a', 'l', 's', 'e'):
                result = result + self.current_char
                self.next()
            if result == "false":
                return False
            else:
                self.error()

    def arr(self):
        pass

    def skipskip(self):
        while self.current_char is not None and self.current_char in ('s', 'k', 'i', 'p'):
            self.next()

    def assign(self):
        reuslt = ''
        while self.current_char is not None and self.current_char in (':', '='):
            result = result + self.current_char
            self.next()
            if result == ":=":
                return "ASSIGN"
            else:
                self.error()
    
    def twhile(self):
        reuslt = ''
        while self.current_char is not None and self.current_char in ('w','h','i','l','e'):
            result = result + self.current_char
            self.next()
            if result == "while":
                return "WHILE"
            else:
                self.error()

    def tif(self):
        reuslt = ''
        while self.current_char is not None and self.current_char in ('i','f'):
            result = result + self.current_char
            self.next()
            if result == "while":
                return "WHILE"
            else:
                self.error()
    
    def tthen(self):
        reuslt = ''
        while self.current_char is not None and self.current_char in ('t', 'h', 'e', 'n'):
            result = result + self.current_char
            self.next()
            if result == "then":
                return 'THEN'
            else:
                self.error()

    def telse(self):
        reuslt = ''
        while self.current_char is not None and self.current_char in ('e', 'l', 's', 'e'):
            result = result + self.current_char
            self.next()
            if result == "else":
                return 'ELSE'
            else:
                self.error()
'''
def main():
    while True:
        try:
            text = input()
        except EOFError:
            break
        print(Lexer(text).skipchar())
if __name__ == '__main__':
    main()
'''