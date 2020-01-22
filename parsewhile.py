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
#test string: "x:=1; y:=2; skip; if a=b then x:=x+1 else x:=x*1; while {b<d do x-y};a∧b; d∨c;"
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
    #error handling
    def error(self):
        raise Exception("This input is not supported")
    #increase the cursor to the next position, if valid then set current_char to the new char
    def next(self):
        self.pos += 1
        #check if it is the end of line
        if self.pos > len(self.text)-1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
    def num(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result = result + self.current_char
            self.next()
        return int(result)
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
        result = ''
        while self.current_char is not None and self.current_char in (':', '='):
            result = result + self.current_char
            self.next()
        if result == ":=":
            return "ASSIGN"
        else:
            self.error()   
    def twhile(self):
        result = ''
        while self.current_char is not None and self.current_char in ('w','h','i','l','e'):
            result = result + self.current_char
            self.next()
        if result == "while":
            return "while"
        else:
            self.error()
    
    def tdo(self):
        result = ''
        while self.current_char is not None and self.current_char in ('d','o'):
            result = result + self.current_char
            self.next()
        if result == "do":
            return "do"
        else:
            self.error()
    def tif(self):
        result = ''
        while self.current_char is not None and self.current_char in ('i','f'):
            result = result + self.current_char
            self.next()
        if result == "if":
            return "if"
        else:
            self.error()   
    def tthen(self):
        result = ''
        while self.current_char is not None and self.current_char in ('t', 'h', 'e', 'n'):
            result = result + self.current_char
            self.next()
        if result == "then":
            return 'then'
        else:
            self.error()
    def telse(self):
        result = ''
        while self.current_char is not None and self.current_char in ('e', 'l', 's', 'e'):
            result = result + self.current_char
            self.next()
        if result == "else":
            return 'else'
        else:
            self.error()
    def tokenize(self):
        while self.current_char is not None:
            if self.current_char in (" ", "\n", "\r"):
                self.next()
            if self.current_char.isdigit():
                return Token("INT", self.num())
            if self.current_char == "+":
                self.next()
                return Token('PLUS', "+")
            if self.current_char == "-":
                self.next()
                return Token("MINUS", "-")
            if self.current_char == "*":
                self.next()
                return Token("MUL", "*")
            if self.current_char == ";":
                self.next()
                return Token('COMP', ";")
            if self.current_char == "=":
                self.next()
                return Token('EQUAL', "=")
            if self.current_char == "<":
                self.next()
                return Token("LESSTHAN", "<")
            if self.current_char == "¬":
                self.next()
                return Token('NOT', "¬")
            if self.current_char == "∧":
                self.next()
                return Token('AND', "∧")
            if self.current_char == "∨":
                self.next()
                return Token('OR', "∨")
            if self.current_char == "{":
                self.next()
                return Token("LEFTCURL", "{")
            if self.current_char == "}":
                self.next()
                return Token("RIGHTCURL", "}")
            if self.current_char == ":":
                return Token("ASSIGN", self.assign())

            #Alphebetical inputs
            if self.current_char.isalpha():
                if self.pos +1 < len(self.text) and not self.text[self.pos+1].isalpha():
                    var = self.current_char
                    self.next()
                    return Token("VAR", var)

                if self.pos +1 < len(self.text) and self.text[self.pos+1].isalpha():
                    if self.current_char == "s":
                        return Token("SKIP", self.skipskip())
                    elif self.current_char == "w":
                        return Token("WHILE", self.twhile())
                    elif self.current_char == "d":
                        return Token("DO", self.tdo())
                    elif self.current_char == "i":
                        return Token("IF", self.tif())
                    elif self.current_char == "t":
                        return Token("THEN", self.tthen())
                    elif self.current_char == "e":
                        return Token("ELSE", self.telse())
                    elif self.current_char in ('t','f'):
                        return Token("ELSE", self.bool())
                    else:
                        self.error()
            self.error()

'''
def main():
    while True:
        try:
            text = input()
        except EOFError:
            break
        print(Lexer(text).skipchar())

https://stackoverflow.com/questions/30239092/how-to-get-multiline-input-from-user
contents = []
while True:
    try:
        line = input()
        if line == "":
            break
    except EOFError:
        break
    contents.append(line)
print(contents)

if __name__ == '__main__':
    main()
'''