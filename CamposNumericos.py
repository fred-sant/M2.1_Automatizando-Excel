#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:03:34 2024

@author: fredy.santander
"""

# Este programa lee un archivo Excel con calificaciones de alumnos, agrega una columna
# llamada 'Mat_Fisica' con valores aleatorios entre 0 y 100 con un decimal, ordena la
# tabla por el campo 'Nombre', cuenta el número de registros y campos, identifica los
# campos numéricos, y guarda el archivo modificado.

import pandas as pd
import numpy as np

# Leer el archivo Excel y cargar los datos en un DataFrame
archivo_excel = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo_excel)

# Contar el número de registros y campos
num_registros = df.shape[0]
num_campos = df.shape[1]

# Imprimir el número de registros y campos
print(f'Número de registros: {num_registros}')
print(f'Número de campos: {num_campos}')

# Generar valores aleatorios para la nueva columna 'Mat_Fisica'
np.random.seed(42)  # Fijar la semilla para reproducibilidad
df['Mat_Fisica'] = np.random.uniform(0, 100, size=len(df)).round(1)

# Ordenar el DataFrame por la columna 'Nombre'
df = df.sort_values(by='Nombre')

# Identificar los campos numéricos
campos_numericos = df.select_dtypes(include=[np.number]).columns.tolist()

# Imprimir los campos numéricos
print(f'Campos numéricos: {campos_numericos}')

# Guardar el DataFrame modificado en un nuevo archivo Excel
df.to_excel('calificaciones_alumnos_con_fisica_ordenado.xlsx', index=False)

# Mostrar los primeros registros para verificar
print(df.head())
