import array

def Sum(ls):
    res = 0
    for i in range(len(ls)):
        res = res + ls[i] 
    return res

def Sub(ls):
    res = 0
    for i in range(len(ls)):
        res = res - ls[i]
    return res

def Mul(ls):
    res = 1
    for i in range(len(ls)):
        res = res * ls[i]
    return res

def Div(ls):
    res = 1
    for i in range(len(ls)):
        res = res / ls[i]
    return res

def Expt(ls):
    res = ls[1]
    for i in range(len(ls)):
        res = res ** ls[i]
    return res


def calculate(operator, *args): 
    def make_array(*args):
        return array.array('f', args)
        
    match operator: # python's switch equivalent (introduced with python 3.10), epico
        case '+':  return Sum(make_array(*args)) 
        case '-':  return Sub(make_array(*args)) 
        case '*':  return Mul(make_array(*args)) 
        case '/':  return Div(make_array(*args)) 
        case '**': return Expt(make_array(*args))
        case default: return "Invalid operator, Mahmood Soldi"
    
