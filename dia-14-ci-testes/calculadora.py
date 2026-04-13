def somar(a, b):
    """
    Realiza a soma de dois números.
    
    Args:
        a: Primeiro número a ser somado (int ou float).
        b: Segundo número a ser somado (int ou float).
    
    Returns:
        int ou float: O resultado da soma entre a e b.
    """
    return a + b

def subtrair(a, b):
    """
    Realiza a subtração entre dois números.
    
    Args:
        a: O minuendo (primeiro número).
        b: O subtraendo (segundo número).
    
    Returns:
        O resultado da subtração de b de a.
    """
    return a - b

def multiplicar(a, b):
    """
    Realiza a multiplicação de dois números.
    
    Args:
        a: Primeiro número a ser multiplicado (int ou float).
        b: Segundo número a ser multiplicado (int ou float).
    
    Returns:
        int ou float: O produto da multiplicação entre a e b.
    """
    return a * b

def dividir(a, b):
    """
    Realiza a divisão de dois números.
    
    Divide o numerador pelo denominador e retorna o resultado da operação.
    Lança uma exceção caso o denominador seja zero.
    
    Args:
        a (float): O numerador da divisão.
        b (float): O denominador da divisão.
    
    Returns:
        float: O resultado da divisão entre a e b.
    
    Raises:
        ValueError: Se b for igual a zero.
    """
    if b == 0:
        raise ValueError("Nao e possivel dividir por zero")
    return a / b