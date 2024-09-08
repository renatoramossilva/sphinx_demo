from typing import Union

# Define a função de sum
def sum(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Sum function

    :param a: Number A
    :param b: Number B

    :return: Result sum a+b
    """
    return a + b

# Define a função de subtração
def sub(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Sub function

    :param a: Number A
    :param b: Number B

    :return: Result sum a-b
    """
    return a - b

# Define a função de multiplicação
def mult(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Mult function

    :param a: Number A
    :param b: Number B

    :return: Result sum a*b
    """
    return a * b

# Define a função de divisão
def div(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Div function

    :param a: Number A
    :param b: Number B

    :return: Result sum a/b
    """
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

# Função principal da calculator
def calculator(operacao: str, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Main function

    :param operacao: Operation name
    :param a: Number A
    :param b: Number B

    :return: Calc result
    """
    if operacao == 'sum':
        return sum(a, b)
    elif operacao == 'sub':
        return sub(a, b)
    elif operacao == 'mult':
        return mult(a, b)
    elif operacao == 'div':
        return div(a, b)
    else:
        raise ValueError(f"Operação {operacao} não é suportada.")

# Exemplo de uso
if __name__ == "__main__":
    a = 10
    b = 5
    print("sum:", calculator('sum', a, b))
    print("Subtração:", calculator('sub', a, b))
    print("Multiplicação:", calculator('mult', a, b))
    print("Divisão:", calculator('div', a, b))
