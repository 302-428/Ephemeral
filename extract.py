#-----------------------------------------------------------------
# pycparser: explore_ast.py
#
# This example demonstrates how to "explore" the AST created by
# pycparser to understand its structure. The AST is a n-nary tree
# of nodes, each node having several children, each with a name.
# Just read the code, and let the comments guide you. The lines
# beginning with #~ can be uncommented to print out useful
# information from the AST.
# It helps to have the pycparser/_c_ast.cfg file in front of you.
#
# Eli Bendersky [http://eli.thegreenplace.net]
# License: BSD
#-----------------------------------------------------------------
from __future__ import print_function
import sys

# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
#
sys.path.extend(['.', '..'])

import pycparser
from pycparser import c_parser, c_ast

text = r"""
struct data {
	int a;
	int b;
};

typedef int Node, Hash;
void foo(int a, int b) {
	a = (a*25)+360 / 15;
	a = a + b;
	b = a+b;
	b = a+b;
}
"""
# Create the parser and ask to parse the text. parse() will throw
# a ParseError if there's an error in the code
#
parser = c_parser.CParser()
ast = parser.parse(text, filename='<none>')

print("===========================Original AST============================")
ast.show(showcoord=True)
print("===================================================================")

#########################################################

# toy language is as below
# e = const | var | let x e
#   | e = e (assignment)
#   | if e e e
#   | while e e
#   | e ; e (sequence)
#   | e b_op e  | u_op e
#   | empty ( )
# b_op = +, - , * , / , &&, ||
# u_op = !

astlist = []
def proper_type(ast):
	T = type(ast)
	if(T is pycparser.c_ast.Constant):
		return True
	if(T is pycparser.c_ast.ID):
		return True
#	if(T is pycparser.c_ast.Decl):
#		return True
	if(T is pycparser.c_ast.Assignment):
		return True
	if(T is pycparser.c_ast.If):
		return True
	if(T is pycparser.c_ast.While):
		return True
	if(T is pycparser.c_ast.Compound):
		return True
	if(T is pycparser.c_ast.BinaryOp):
		return True
	if(T is pycparser.c_ast.UnaryOp):
		return True
	if(T is pycparser.c_ast.BinaryOp):
		return True
	return False

def report_to_server(ast) :
# 1. re-name variables 'in unique way'
# 2. record the 'variable semantic' in the database

#pass #TODO ################I dont like '#' I prefer /**/
	return report(ast)

def report(ast) :
	flag = True
	if(not proper_type(ast)):
		flag = False

	ast_children = ast.children()
	for ast_child in ast_children:
		if(not report(ast_child[1])):
			flag = False

	if(flag):
		astlist.append(ast)
		return flag

report(ast)
for i in xrange(0, len(astlist)):
	print("Printing AST")
	astlist[i].show(showcoord=True)

