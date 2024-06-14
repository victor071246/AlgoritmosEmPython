import numpy as np

def invert_matrix(matrix):
    """
    Inverte uma matriz quadrada.
    
    :param matrix: Lista de listas representando a matriz a ser invertida.
    :return: Matriz invertida como uma lista de listas ou uma mensagem de erro se a matriz não for invertível.
    """
    try:
        # Converte a matriz de lista de listas para um array NumPy
        np_matrix = np.array(matrix)
        
        # Verifica se a matriz é quadrada
        if np_matrix.shape[0] != np_matrix.shape[1]:
            return "A matriz deve ser quadrada para ser invertida."
        
        # Calcula a matriz inversa
        inv_matrix = np.linalg.inv(np_matrix)
        
        # Converte a matriz invertida de volta para lista de listas
        return inv_matrix.tolist()
    except np.linalg.LinAlgError:
        return "A matriz fornecida não é invertível."

# Exemplo de uso
if __name__ == "__main__":
    matriz = [
        [1, 2, 3],
        [0, 1, 4],
        [5, 6, 0]
    ]

    inversa = invert_matrix(matriz)
    if isinstance(inversa, list):
        print("Matriz invertida:")
        for linha in inversa:
            print(linha)
    else:
        print(inversa)
