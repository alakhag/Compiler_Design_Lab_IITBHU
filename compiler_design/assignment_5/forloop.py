def valid_id(id):
    if not id[0].isalpha() and id[0]!='_':
        return False
    for i in id:
        if not i.isalnum() and i!='_':
            return False
    return True

def T(expr):
	if expr == 'int' or expr == 'float' or expr == 'double' or expr == 'char':
		return True
	return False

def A(expr):
	if '*' in expr:
		return False
	expr_temp = expr.replace(' ','*').replace(',','*').split('*')
	res = T(expr_temp[0])
	if res == False:
		si = 0
	else:
		si = 1
	res = True
	for st in expr_temp[si:]:
		tres = st.split('=')
		if len(tres) != 2:
			return False
		tres = valid_id(tres[0]) and (valid_id(tres[1]) or tres[1].isnumeric())
		res = res and tres
		if not res:
			break
	return res

def C(expr):
	expr = expr.replace('&&','*').replace('||','*').split('*')
	res = True
	for e in expr:
		if '==' in e:
			e = e.split('==')
			res = res and (len(e)==2) and (valid_id(e[0]) or e[0].isnumeric()) and (valid_id(e[1]) or e[1].isnumeric())
		elif '<=' in e:
			e = e.split('<=')
			res = res and (len(e)==2) and (valid_id(e[0]) or e[0].isnumeric()) and (valid_id(e[1]) or e[1].isnumeric())
		elif '>=' in e:
			e = e.split('>=')
			res = res and (len(e)==2) and (valid_id(e[0]) or e[0].isnumeric()) and (valid_id(e[1]) or e[1].isnumeric())
		elif '<' in e:
			e = e.split('<')
			res = res and (len(e)==2) and (valid_id(e[0]) or e[0].isnumeric()) and (valid_id(e[1]) or e[1].isnumeric())
		elif '>' in e:
			e = e.split('>')
			res = res and (len(e)==2) and (valid_id(e[0]) or e[0].isnumeric()) and (valid_id(e[1]) or e[1].isnumeric())
		else:
			res = False
			break
	return res

def U(expr):
	if expr[-2:] == '--' or expr[-2:] == '++' and valid_id(expr[:-2]):
		return True
	return False

def D(expr):
	if len(expr) == 1 and expr[0]=='stmt':
		return True
	elif len(expr) ==0:
		return True
	else:
		for i in range(len(expr)+1):
			res = S(expr[:i]) and D(expr[i:])
			if res:
				return res
	return False
def S(expr):
	if len(expr) > 9 and expr[0]=='for' and expr[1] == '(' and A(expr[2]) and expr[3] == ';' and C(expr[4]) and expr[5] == ';' and U(expr[6]) and expr[7] == ')' and expr[8] == '{' and expr[-1] =='}': 
		return D(expr[9:-1])
	return False

def spliter(expr):
	expr = expr.replace(' ','').replace('for','#for#').replace(';','#;#').replace('(','#(#').replace(')','#)#').replace('{','#{#').replace('}','#}#').split('#')
	return [i for i in expr if i!='']

def Parser(expr):
    expr = spliter(expr)
    print "-------------------------------------------"
    print 'Expression in Tokens : '
    print '',expr
    print "-------------------------------------------"
    return S(expr)

try:
    while True:
        print "-------------------------------------------"
        expr = raw_input('   Enter Expression : ')
        print "   Expression is    : ",Parser(expr)
        print ""
except Exception as ex:
    print ex
