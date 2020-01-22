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
#test string: "a := 369; b := 1107; a:= a+b*c-d; while ¬(a=b) do { if a < b then b := b - a else a := a - b}"
class Token():
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __repr__(self):
        return 'Token({type}, {value})'.format(type = self.type, value = self.value)

class Lexer():
    def __init__(self, text):
        self.state = {}
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
    #integer arrays reprented by lists
    def arr(self):
        result = ''
        self.next()
        while self.current_char is not None and self.current_char != "]":
            result = result+self.current_char
            self.next()
        self.next()
        result = [int(t) for t in result.split(',')]
        return result
    def skipskip(self):
        while self.current_char is not None and self.current_char in ('s', 'k', 'i', 'p'):
            self.next()
    def assign(self):
        result = ''
        while self.current_char is not None and self.current_char in (':', '='):
            result = result + self.current_char
            self.next()
        if result == ":=":
            return "assign"
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
            if self.current_char == "[":
                return Token("ARR", self.arr())
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
            if self.current_char == "(":
                self.next()
                return Token("LEFTPAR", "(")
            if self.current_char == ")":
                self.next()
                return Token("RIGHTPAR", ")")
            if self.current_char == ":":
                return Token("ASSIGN", self.assign())

            #Alphebetical inputs
            if self.current_char.isalpha():
                if (self.pos +1 == len(self.text) or (not self.text[self.pos+1].isalpha())):
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
                    elif self.current_char == "t" and self.text[self.pos+1] =="h":
                        return Token("THEN", self.tthen())
                    elif self.current_char == "e":
                        return Token("ELSE", self.telse())
                    elif self.current_char in ('t','f'):
                        return Token("BOOL", self.bool())
            self.error()
        return(Token("EOF", None))

#create all the needed nodes
class IntNode():
    def __init__(self, token):
        self.value = token.value
        self.op = token.type
class ArrNode():
    def __init__(self, token):
        self.value = token.value
        self.op = token.type
class VarNode():
    def __init__(self, token):
        self.value = token.value
        self.op = token.type
class BoolNode():
    def __init__(self, token):
        self.value = token.value
        self.op = token.type
class NotNode():
    def __init__(self, token):
        self.op = token.type
#For all the Aexpr operations
class BinopNode():
    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op
#For all the Bexpr operations
class BoolopNode():
    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op
class AssignNode():
    pass
class CompNode():
    pass
class WhileNode():
    #should be a while true and while false
    pass
class DoNode():
    pass
class IfNode():
    pass
class ThenNode():
    pass
class ElseNode():
    pass

#help with creating a dictionary for states
class helpers():
    def create_dict(self, var, value):
        return dict([tuple([var,value])])

#lexer tokenize everything with the proper token, each time object.tokenize is called, the next value gets tokenized
#Parser should parse out a AST.
class Parser():
    def __init__(self, lexer):
        self.lexer = lexer
        self.state = lexer.state
        self.current_token = lexer.tokenize()
    def error(self):
        raise error("Invalid Syntax for this language")   

    def factor(self):
        token = self.current_token
        #negative value
        if token.type == "MINUS":
            self.current_token = self.lexer.tokenize()
            token = self.current_token
            #print('first',token.value)
            token.value = -token.value
            #print(token.value)
            node = IntNode(token)
        elif token.type == "INT":
            node = IntNode(token)
            #print(node.value)
        elif token.type == "VAR":
            node = VarNode(token)
        elif token.type == "ARR":
            node = ArrNode(token)
        elif token.type == "NOT":
            node = NotNode(token)
        elif token.type == "BOOL":
            node = BoolNode(token)
        elif token.tpye == "LEFTPAR":
            self.current_token = self.lexer.tokenize()
            node = bexpr()
        elif token.type == "RIGHTPAR":
            pass
        else:
            self.error()      
        self.current_token = self.lexer.tokenize()      
        return node
    
    def aterm(self):
        node = self.factor()
        while self.current_token.type == 'MUL':
            print(self.current_token)
            ttype = self.current_token.type
            self.current_token = self.lexer.tokenize()
            node = BinopNode(left = node, right = self.factor(), op = ttype)
            #print("in term",node.left, node.right) 
        return node
        
    def aexpr(self):
        node = self.aterm()  
        #print("in expression", token.value)
        while self.current_token.type in ("PLUS", "MINUS"):
            print(self.current_token)
            ttype = self.current_token.type
            self.current_token = self.lexer.tokenize()
            node = BinopNode(left = node, right = self.aterm(), op = ttype)
            #print("in expr",node.left, node.right)
        return node
    #this returns a node that represent Aexpr for debugging
    def aparse(self):
        return self.aexpr()

    def bterm(self):
        node = self.aexpr()
        if self.current_token.type in ("EQUAL","LESSTHAN"):
            print(self.current_token)
            ttype = self.current_token.type
            self.current_token = self.lexer.tokenize()
            node = BoolopNode(left = node, right = self.aexpr(), op = ttype)
        return node
    
    def bexpr(self):
        node = self.bterm()
        if node.op == "NOT":
            print(self.current_token)
            node.ap = self.bexpr()
        while self.current_token.type in ("AND", "OR"):
            print(self.current_token)
            ttype = self.current_token.type
            self.current_token = self.lexer.tokenize()
            node = BinopNode(left = node, right = self.bterm(), op = ttype)
        return node

    def bparse(self):
        return self.bexpr()

    def cexpr():
        pass
    def statement(self):
        pass

class Interper():
    pass

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