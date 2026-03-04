import pandas as pd
import numpy as np
import math

df = pd.read_csv("diabetes.csv")
print("Dimensión de la tabla:", df.shape)

# Función que retorna el menor de tres valores
def menor(A, B, C):
    return min(A, B, C)

#funcion que saca el maximo de los valores
def maximo(A, B, C):
    return max(A, B, C)

#funcion que saca el promedio de los valores
def mean(A, B, C):
    return mean(A, B, C)