from typing import Union

# Define a função de soma
def soma(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Sum function

    :param a: Number A
    :param b: Number B

    :return: Result sum a+b
    """
    return a + b

# Define a função de subtração
def subtracao(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Sub function

    :param a: Number A
    :param b: Number B

    :return: Result sum a-b
    """
    return a - b

# Define a função de multiplicação
def multiplicacao(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Mult function

    :param a: Number A
    :param b: Number B

    :return: Result sum a*b
    """
    return a * b

# Define a função de divisão
def divisao(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Div function

    :param a: Number A
    :param b: Number B

    :return: Result sum a/b
    """
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

# Função principal da calculadora
def calculadora(operacao: str, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Main function

    :param operacao: Operation name
    :param a: Number A
    :param b: Number B

    :return: Calc result
    """
    if operacao == 'soma':
        return soma(a, b)
    elif operacao == 'subtracao':
        return subtracao(a, b)
    elif operacao == 'multiplicacao':
        return multiplicacao(a, b)
    elif operacao == 'divisao':
        return divisao(a, b)
    else:
        raise ValueError(f"Operação {operacao} não é suportada.")

# Exemplo de uso
if __name__ == "__main__":
    a = 10
    b = 5
    print("Soma:", calculadora('soma', a, b))
    print("Subtração:", calculadora('subtracao', a, b))
    print("Multiplicação:", calculadora('multiplicacao', a, b))
    print("Divisão:", calculadora('divisao', a, b))
