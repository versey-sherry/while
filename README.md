# WHILE
Course Homework for Programming Languages. Implementing WHILE in Python

As per the homework requirement, this script will do the following things:
1. The script gets inputs via stdin and output via stdout
2. The script parses the input into an Abstract Syntax Tree (AST)
3. The AST is evaulated in the interpreter and the script outputs the results.
4. The program should print out small step semantics.

While supports arithmetic expressions, boolean expressions and commands.

### Requirements:
python3 >=3.6

pyinstaller ==3.6

### Implementation
The program reads in a string and parse the string into tokens. Then tokens are placed in the correct position of the AST with DFS. The tree is then evaluated recursively bottom up.

Structual Hierarchy

Factors (Int, Var, Bool, (Bexp), {Cexp} and negation) < Aterm (*) < Aexp(+,-) < Bterm(=, <) < Bexp(&, |) < Cterm(skip, :=) < Cexp(;, if b then c1 else c2, while b do c)
