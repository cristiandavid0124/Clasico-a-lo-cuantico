#CRISTIAN DAVID NARANJO ORJUELA CNYT 2
import scipy
import math
import numpy as np
import matplotlib.pyplot as plt

def sumcplx(a, b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    return (real, img)

def multicplx(a, b):
    real = (a[0] * b[0]) - (a[1] * b[1])
    img = (a[0] * b[1]) + (a[1] * b[0])
    return real, img

def modulo(c):
    raiz = math.sqrt(c[0] ** 2 + c[1] ** 2)
    return raiz


def actionbool(vect, vect1):
    row, col = len(vect), len(vect[0])
    if col == len(vect1):
        answer = [False for k in range(row)]
        for i in range(row):
            flag = True
            for j in range(col):
                flag = vect1[i][j] and vect1[j]
                answer[i] = answer[i] or flag
        return answer
    else:
        return "Size Error"


def action(matrix, vect1):
    m, n = len(matrix), len(matrix[0])
    prob1 = len(vect1)
    answer = []
    if len(vect1) == n:
        matinicial = (0, 0)
        for i in range(m):
            for j in range(len(matrix[i])):
                operation = multicplx(matrix[i][j], vect1[j])
                matinicial = sumcplx(operation, matinicial)
            answer += [matinicial]
            matinicial = (0, 0)
        return answer
    else:
        return "Size Error"


def actionComplex(matrix, vect1):
    if len(matrix[0]) == len(vect1):
        vector = [(0, 0) for i in range(len(vect1))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                vector[i] = sumcplx(vector[i], multicplx(matrix[i][j], vect1[j]))
        return vector
    else:
        return "Size Error"


def matrixComplex(matrix, vect1, clicks):
    answer = [(0, 0) for x in range(len(vect1))]
    for j in range(clicks):
        new_vect = actionComplex(matrix, vect1)
        vect1 = new_vect
    if vect1 != "Length error":
        for i in range(len(vect1)):
            num = modulo(vect1[i]) ** 2
            answer[i] = num
    else:
        answer = "Size Error"
    return answer

def marbleExperiment(matrix,vect1,n):
    click = 0
    if len(matrix) == len(vect1):
        answer = vect1
        while click != n:
            answer = action(matrix,answer)
            click += 1
        return answer
    else:
        return "Size Error"
def experiments(matrix, vect1, n):
    power = np.linalg.matrix_power(matrix, n)
    answer = action(power,vect1)
    return(answer)

def grafica(matrix, vect1, clicks):
    posiciones = [n for n in range(len(vect1))]
    probability = matrixComplex(matrix, vect1, clicks)
    fig, ax = plt.subplots()
    ax.set_ylabel('Probability')
    ax.set_xlabel('Position')
    ax.set_title('Quantum system probability')
    plt.bar(posiciones, probability)
    plt.savefig('Quantum_system_probability.png')
    plt.show()

def main():
    matrix = [(8, 0), (3, 2)], [(3, 5), (6, 6)]
    vect1 = [(5, 6), (4, 2)]
    print(action(matrix, vect1))
    print(actionbool(vect1, vect1))
    print(actionComplex(matrix, vect1))
    print(matrixComplex(matrix, vect1, 2))
    print(marbleExperiment(matrix,vect1,2))
    print(experiments(matrix, vect1, 2))
main()