# -*- coding: utf-8 -*-
"""AluraStoreLatamcarlosmario.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xaMNfHo2kbgSHuUZaTNV3pMVA7-OBkV2

### Importación de datos
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#estas serían las URLs de los archivos csv que debo analizar
url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

#aquí se cargarían los archivos. Por lo que tengo 4 tiendas
tienda = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

tienda.head()
"""
Ahora examinaré cuidadosamente los datos CSV LS de mi negocio, que se verán así:
Este encabezado me permite ver los títulos del encabezado
"""

"""#1. Análisis de facturación


"""

tienda["Tienda"] = "Tienda 1"
tienda2["Tienda"] = "Tienda 2"
tienda3["Tienda"] = "Tienda 3"
tienda4["Tienda"] = "Tienda 4"

df_total = pd.concat([tienda, tienda2, tienda3, tienda4], ignore_index=True)
#se unen las cuatro tiendas en una sola
df_total.head()

# Calcular ingreso total por venta (suma del precio y costo de envío)
df_total["Ingreso Total"] = df_total["Precio"] + df_total["Costo de envío"]

# Agrupar por tienda y calcular el ingreso total por tienda
ingresos_por_tienda = (
    df_total.groupby("Tienda")["Ingreso Total"]
    .sum()
    .sort_values(ascending=False)  # Ordenar de mayor a menor ingreso
)

# Mostrar ingresos sin formato (útil para análisis)
print("Ingresos totales por tienda (sin formato):")
print(ingresos_por_tienda)

# Formatear los ingresos para visualización (con símbolo de dólar y separadores de miles)
ingresos_formateados = ingresos_por_tienda.apply(lambda x: f"${x:,.0f}")

# Mostrar ingresos formateados
print("\nIngresos totales por tienda (formateados):")
print(ingresos_formateados)

# Opcional: convertir ingresos a millones (por ejemplo, para gráficos)
ingresos_en_millones = ingresos_por_tienda / 1e6

import matplotlib.pyplot as plt

# Crear gráfico de barras de ingresos por tienda (en millones)
plt.figure(figsize=(8, 5))  # Tamaño de la figura
bars = plt.bar(ingresos_en_millones.index, ingresos_en_millones.values, color='gray')

# Agregar valores encima de cada barra (formato con una decimal y M de millones)
for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # posición horizontal centrada en la barra
        yval + 0.1,                         # posición vertical un poco encima de la barra
        f"{yval:.1f}M",                     # texto: valor en millones con un decimal
        ha='center',
        va='bottom',
        fontsize=8
    )

# Títulos y etiquetas del gráfico
plt.title("Ingresos Totales por Tienda", fontsize=20)
plt.xlabel("Tienda", fontsize=14)
plt.ylabel("Millones de pesos", fontsize=12)

# Mejorar la presentación del gráfico
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)  # línea de guía horizontal

# Mostrar gráfico
plt.show()

"""# 2. Ventas por categoría"""

# Agrupar ingresos totales por categoría del producto y ordenarlos de mayor a menor
ventas_por_categoria = (
    df_total.groupby("Categoría del Producto")["Ingreso Total"]
    .sum()
    .sort_values(ascending=False)
)

# Mostrar resultados sin formato (útiles para análisis)
print("Ingresos totales por categoría de producto (sin formato):")
print(ventas_por_categoria)

# Formatear los ingresos con separador de miles y símbolo de pesos
ventas_formateadas = ventas_por_categoria.apply(lambda x: f"${x:,.0f}")

# Mostrar resultados formateados (útiles para presentación final)
print("\nIngresos totales por categoría de producto (formateados):")
print(ventas_formateadas)

# Convertir ingresos por categoría de producto a millones de pesos
ventas_categoria_millones = ventas_por_categoria / 1e6

# Mostrar como tabla (útil en notebooks)
print("Ingresos por categoría de producto (en millones de pesos):")
display(ventas_categoria_millones)

import matplotlib.pyplot as plt

# Crear gráfico de barras horizontal para mostrar ingresos por categoría de producto (en millones)
plt.figure(figsize=(9, 6))  # Definir tamaño del gráfico

bars = plt.barh(
    ventas_categoria_millones.index,
    ventas_categoria_millones.values,
    color='darkseagreen'
)

# Añadir etiquetas numéricas al final de cada barra
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 0.1,                              # Desplazar el texto un poco a la derecha de la barra
        bar.get_y() + bar.get_height() / 2,       # Centrar verticalmente
        f"{width:.1f}M",                          # Formato: millones con 1 decimal
        va='center',
        fontsize=8
    )

# Añadir título y etiquetas de los ejes
plt.title("Ventas Totales por Categoría", fontsize=20)
plt.xlabel("Millones de pesos", fontsize=14)
plt.ylabel("Categoría del Producto", fontsize=14)

# Mejorar presentación del gráfico
plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.5)  # Líneas guía horizontales

# Mostrar gráfico
plt.show()

"""# 3. Calificación promedio de la tienda

"""

# Calcular la calificación promedio por tienda y ordenarla de mayor a menor
calificacion_promedio_por_tienda = (
    df_total.groupby("Tienda")["Calificación"]
    .mean()
    .sort_values(ascending=False)
)

# Mostrar resultados en forma tabular (útil en notebooks como Jupyter o Colab)
print("Calificación promedio de los clientes por tienda:")
display(calificacion_promedio_por_tienda)

import matplotlib.pyplot as plt

# Definir paleta de colores personalizada (opcional)
colores = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3']  # Un color para cada tienda

# Crear gráfico de barras horizontal de calificación promedio por tienda
plt.figure(figsize=(8, 5))

bars = plt.barh(
    calificacion_promedio_por_tienda.index,
    calificacion_promedio_por_tienda.values,
    color=colores
)

# Agregar etiquetas numéricas al final de cada barra
for bar in bars:
    xval = bar.get_width()
    plt.text(
        xval + 0.02,
        bar.get_y() + bar.get_height() / 2,
        f"{xval:.2f}",
        va='center',
        fontsize=9
    )

# Título y etiquetas
plt.title("Calificación Promedio por Tienda", fontsize=20)
plt.xlabel("Calificación (de 1 a 5)", fontsize=14)

# Ajustar los límites del eje x para que no empiece en cero (resalta diferencias)
plt.xlim(
    calificacion_promedio_por_tienda.min() - 0.1,
    calificacion_promedio_por_tienda.max() + 0.1
)

# Líneas guía horizontales para facilitar lectura
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Ajuste de márgenes y visualización
plt.tight_layout()
plt.show()

"""# 4. Productos más y menos vendidos"""

# Contar la cantidad de veces que cada producto aparece en el dataset (más vendidos)
productos_mas_vendidos = df_total["Producto"].value_counts().head(10)

# Mostrar los 10 productos más vendidos
print("Top 10 productos más vendidos:")
display(productos_mas_vendidos)

# Opcional: Formatear los nombres de productos si son muy largos (para mejorar la visualización)
productos_mas_vendidos.index = productos_mas_vendidos.index.str.wrap(20)  # Limitar a 20 caracteres por línea

# Mostrar nuevamente con los nombres de productos ajustados
display(productos_mas_vendidos)

import matplotlib.pyplot as plt
import seaborn as sns

# Obtener los 10 productos más vendidos (ordenados)
productos_mas_vendidos = df_total["Producto"].value_counts().head(10)

# Obtener los valores y los productos ordenados
productos = productos_mas_vendidos[::-1]
valores = productos.values

# Crear una paleta de colores única para los diferentes valores
# Usar "husl" para una paleta de colores distintos para cada barra
valores_unicos = list(dict.fromkeys(valores))  # Lista de valores únicos para asignar colores
palette = sns.color_palette("husl", len(valores_unicos))  # Paleta colorida
color_map = {val: palette[i] for i, val in enumerate(valores_unicos)}

# Asignar un color por cada valor
colores = [color_map[val] for val in valores]

# Crear gráfico de barras horizontal
plt.figure(figsize=(12, 7))  # Aumentar tamaño de la figura para mayor claridad
bars = plt.barh(productos.index, valores, color=colores, edgecolor='black')  # Añadir bordes negros a las barras

# Agregar etiquetas a las barras
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 2,  # Separación de las etiquetas con respecto a las barras
        bar.get_y() + bar.get_height() / 2,  # Centrado vertical de las etiquetas
        f"{width}",  # Mostrar cantidad de ventas
        va='center',  # Alineación vertical
        fontsize=12,  # Tamaño de la fuente
        fontweight='bold',  # Negrita para destacar la etiqueta
        color='black'  # Color de la etiqueta para buen contraste
    )

# Títulos y etiquetas
plt.title("Top 10 Productos Más Vendidos", fontsize=24, fontweight='bold')  # Título con mayor tamaño y negrita
plt.xlabel("Cantidad de Ventas", fontsize=18)
plt.ylabel("Producto", fontsize=18)

# Ajustar márgenes y mejorar el layout
plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.4)

# Mostrar gráfico
plt.show()
d

"""# 5. Envío promedio por tienda"""

# Contar la cantidad de ventas por producto y ordenar de menor a mayor para obtener los productos con menos ventas
productos_menos_vendidos = (
    df_total["Producto"]
    .value_counts()
    .sort_values(ascending=True)  # Ordenar de menor a mayor
    .head(10)  # Obtener los 10 productos con menos ventas
)

# Mostrar los 10 productos con menos ventas
print("Top 10 productos con menos ventas:")
display(productos_menos_vendidos)

# Opcional: Si los nombres de los productos son largos, podemos formatearlos para mejorar la visualización
productos_menos_vendidos.index = productos_menos_vendidos.index.str.wrap(20)  # Limitar a 20 caracteres por línea

# Mostrar nuevamente con los nombres de productos ajustados
display(productos_menos_vendidos)

import matplotlib.pyplot as plt
import seaborn as sns

# Contar la cantidad de ventas por producto y ordenar de menor a mayor para obtener los productos con menos ventas
productos_menos_vendidos = (
    df_total["Producto"]
    .value_counts()
    .sort_values(ascending=True)  # Ordenar de menor a mayor
    .head(10)  # Obtener los 10 productos con menos ventas
)

# Mostrar los 10 productos con menos ventas
print("Top 10 productos con menos ventas:")
display(productos_menos_vendidos)

# Crear una paleta de colores personalizada
colores = sns.color_palette("coolwarm", len(productos_menos_vendidos))  # Usando la paleta coolwarm

# Gráfico de barras horizontal para productos con menos ventas
plt.figure(figsize=(10, 6))
bars = plt.barh(productos_menos_vendidos.index, productos_menos_vendidos.values, color=colores)

# Etiquetas en las barras
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 0.05,  # Desplazar el texto un poco a la derecha de la barra
        bar.get_y() + bar.get_height() / 2,  # Centrar verticalmente
        f"{width}",  # Mostrar la cantidad de ventas
        va='center',
        fontsize=10,
        fontweight='bold',
        color='black'  # Contrastar el texto con el color de la barra
    )

# Títulos y etiquetas
plt.title("Top 10 Productos con Menos Ventas", fontsize=20, fontweight='bold')
plt.xlabel("Cantidad de Ventas", fontsize=16)
plt.ylabel("Producto", fontsize=16)

# Mejorar el layout
plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.4)

# Mostrar el gráfico
plt.show()