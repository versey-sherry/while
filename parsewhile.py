#There are three types syntaxs Aexpr Bexpr and Satements
#There are tokens for INT, VAR, BOOL, WHILE, { , }, IF, THEN, ELSE ;, ARR
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

    def next(self):
        self.pos += 1
        #check if it is the end of line
        if self.pos > len(self.text)-1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skipchar(self):
        #need to skip spaces and line break, spaces work but linebreak is still a bit funky
        while self.current_char is not None and self.current_char in (" ", "\n", "\r"):
            self.next()




def main():
    while True:
        try:
            text = input()
        except EOFError:
            break
        print(Lexer(text).skipchar())
if __name__ == '__main__':
    main()
