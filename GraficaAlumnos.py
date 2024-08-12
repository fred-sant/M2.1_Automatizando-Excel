#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 10:39:56 2024

@author: fredy.santander
"""

# Este programa lee un archivo Excel con calificaciones de alumnos y genera un gráfico
# de barras para cada alumno mostrando sus calificaciones en las materias: Cálculo Integral,
# Programación Orientada a Objetos y Estructura de Datos. Las etiquetas en el eje X se rotan
# para evitar que se encimen.

import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo Excel y cargar los datos en un DataFrame
archivo_excel = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo_excel)

# Configurar el tamaño del gráfico
plt.figure(figsize=(10, 6))

# Generar el gráfico de barras
for i, row in df.iterrows():
    # Obtener el nombre del alumno y sus calificaciones
    nombre = row['Nombre']
    calificaciones = row[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']]
    
    # Crear una posición en el eje X para cada alumno
    x = [i * 3, i * 3 + 1, i * 3 + 2]
    
    # Graficar las calificaciones del alumno
    plt.bar(x, calificaciones, label=nombre)

# Etiquetas para el eje X
nombres_materias = ['Cálculo Integral', 'Programación OOP', 'Estructura de Datos']
xticks = [i * 3 + 1 for i in range(len(df))]

# Configurar el eje X
plt.xticks(xticks, df['Nombre'], rotation=45, ha='right')

# Añadir leyenda, título y etiquetas
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.title('Calificaciones de los Alumnos')
plt.xlabel('Alumnos')
plt.ylabel('Calificaciones')

# Mostrar el gráfico
plt.tight_layout()
plt.show()
