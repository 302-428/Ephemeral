from pycparser import c_parser, c_ast

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

def proper_type(ast):
    return type(ast) in [ # are these right? how does sequence work?
        c_ast.Constant, #const
        c_ast.ID,       #var
        c_ast.Decl,     #let x e

        c_ast.Assignment, # e = e
        c_ast.If,         # if e e e
        c_ast.While,      # while e e
        c_ast.Compound,   # {e ; ... ; e}

        c_ast.BinaryOp,   # e b_op e
        c_ast.UnaryOp,    # e u_op e

        c_ast.EmptyStatement, #( )
        #c_ast.NamedInitializer, # ???       
    ]

def report_to_server(ast) :
    # 1. re-name variables 'in unique way'
    # 2. record the 'variable semantic' in the database
    
    #pass #TODO ################I dont like '#' I prefer /**/
    return report(ast)


def report_children(ast_children_tuple):
    flag = True
    for ast_child in ast_children_tuple : 
        flag = flag and report(ast_child)    
    return flag

def report(ast) :
    if(proper_type(ast) and report_children(ast.children())) : #ast.children right?
        report_to_server(ast)
        return True
    else:
        return False
    
