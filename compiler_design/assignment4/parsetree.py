def XY(f1,f2,expr,epsilon):
    res = False
    if not expr and epsilon:
        res=True
    for i in range(len(expr)+1):
        res = res or (f1(expr[:i]) and f2(expr[i:]))
        if res:
            #print f1, f2, expr, i
            break
    return res

def F(expr):
    if len(expr)==1 and expr[0]=="id":
        return True
    elif len(expr) > 2 and expr[0]=="(" and expr[-1]==")":
        return E(expr[1:-1])
    return False

def T_(expr):
    if len(expr)==0:
        return True
    elif expr[0] != '*' or len(expr)==1:
        return False
    return XY(F,T_,expr[1:],True)

def T(expr):
    return XY(F,T_,expr,False)

def E_(expr):
    if len(expr)==0:
        return True
    elif expr[0] != '+' or len(expr)==1:
        return False
    return XY(T,E_,expr[1:],True)

def E(expr):
    return XY(T,E_,expr,False)

def spliter(expr):
    expr=expr.replace(" ","").replace("\t","").replace("\n","").replace("*","#*#").replace("+","#+#").replace("(","#(#").replace(")","#)#").split('#')
    return [i for i in expr if i != '#' and i != '']

def Parser(expr):
    expr = spliter(expr)
    return E(expr)

while True:
	print("-------------------------------------------")
	expr = raw_input("    Expression    : ")
	if expr == "no":
		break
	res = Parser(expr)
	print "   Expression is    : ",res
