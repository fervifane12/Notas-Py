a=0
b=0
def suma (a=float(a), b=float(b)):
    try:
        r=a+b
    except TypeError:
        print ("Debe escribir un número")
    else:
        return r

def resta (a=float(a), b=float(b)):
    try:
        r=a-b
    except TypeError:
        print ("Debe escribir un número")
    else:
        return r

def producto(a=float(a), b=float(b)):
    try:
        r=a*b
    except TypeError:
        print ("Debe escribir un número")
    else:
        return r
        
def division(a=float(a), b=float(b)):
    try:
        r=a/b
    except ZeroDivisionError:
       print ("No es posible dividir entre cero")
    except TypeError:
        print ("Debe escribir un número")
    else:
        return r