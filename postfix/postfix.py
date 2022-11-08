def postfix_eval(chaine):
    OPERATION = {
        '+' : lambda x, y: x+y,
        '-' :  lambda x, y: x-y,
        '*' :  lambda x, y: x*y,
        '/' : lambda x, y: x//y,
                }

    L=chaine.split()
    stack=[]
    res = 0
    for token in L:
        if token in OPERATION:
            try:
                a = stack.pop()
                b = stack.pop()
            except:
                return 'error-empty-stack'
            res = OPERATION[token](b,a)
            stack.append(res)
            
        else:
            try:
                token == int(token)
            except:
                return 'error-syntax'
            stack.append(int(token))
        
    if len(stack) > 1:
        return 'error-unfinished'
        
            
        
        
    return stack[0]
            
