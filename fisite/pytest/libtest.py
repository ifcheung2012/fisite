def lib_func(a):
    return a + 10

def lib_func_another(b):
    """docstring for lib_func_another"""
    return b + 20

print __name__
if __name__ == '__main__':
    test = 101
    print(lib_func(120))
