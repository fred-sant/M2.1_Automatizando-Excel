#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 10:54:45 2024

@author: fredy.santander
"""

# Este programa lee un archivo Excel con calificaciones de alumnos, agrega una columna
# llamada 'Mat_Fisica' con valores aleatorios entre 0 y 100 con un decimal, y guarda
# el archivo modificado.

import pandas as pd
import numpy as np

# Leer el archivo Excel y cargar los datos en un DataFrame
archivo_excel = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo_excel)

# Generar valores aleatorios para la nueva columna 'Mat_Fisica'
np.random.seed(42)  # Fijar la semilla para reproducibilidad
df['Mat_Fisica'] = np.random.uniform(0, 100, size=len(df)).round(1)

# Guardar el DataFrame modificado en un nuevo archivo Excel
df.to_excel('calificaciones_alumnos_con_fisica.xlsx', index=False)

# Mostrar los primeros registros para verificar
print(df.head())
