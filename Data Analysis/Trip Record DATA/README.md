# Análisis de los Datasets de Taxis Amarillos y Verdes en Nueva York (Junio 2023)

Se presenta un análisis detallado de los datasets de viajes de taxis amarillos y verdes en la ciudad de Nueva York durante el mes de junio de 2023. Los objetivos de este análisis son entender los patrones de viaje, las distancias recorridas, los métodos de pago utilizados, las tarifas y propinas, así como otros aspectos relevantes de los viajes en taxi en la ciudad.

## 1. Descripción de los Datasets

### Taxis Amarillos
- **Nombre del archivo:** yellow_tripdata_2023-06.parquet
- **Número de registros:** 3,307,234
- **Número de columnas:** 19

### Taxis Verdes
- **Nombre del archivo:** green_tripdata_2023-06.parquet
- **Número de registros:** 65,550
- **Número de columnas:** 20

## 2. Análisis Descriptivo

### Taxis Amarillos
| Métrica                  | Valor          |
|--------------------------|----------------|
| Media de duración        | 18:09 (hh:mm)  |
| Media de distancia       | 4.37 millas    |
| Media de tarifa          | $19.99         |
| Media de propina         | $3.59          |
| Método de pago más usado | Tarjeta de crédito |

### Taxis Verdes
| Métrica                  | Valor          |
|--------------------------|----------------|
| Media de duración        | 20:02 (hh:mm)  |
| Media de distancia       | 22.43 millas   |
| Media de tarifa          | $18.89         |
| Media de propina         | $2.41          |
| Método de pago más usado | Tarjeta de crédito |

## 3. Análisis de Duración y Distancia de Viajes

### Taxis Amarillos
- **Duración del Viaje:** La mayoría de los viajes tienen una duración entre 10 y 30 minutos.
- **Distancia del Viaje:** La distancia media es de 4.37 millas, con algunas distancias extremadamente altas que podrían ser errores.

### Taxis Verdes
- **Duración del Viaje:** La mayoría de los viajes tienen una duración entre 15 y 30 minutos.
- **Distancia del Viaje:** La distancia media es de 22.43 millas, con algunas distancias extremadamente altas que podrían ser errores.

## 4. Análisis de Tarifas y Propinas

### Taxis Amarillos
- **Tarifa Media:** $19.99
- **Propina Media:** $3.59
- **Total Amount:** La tarifa total incluye tarifas adicionales y recargos, con una media de $29.07.

### Taxis Verdes
- **Tarifa Media:** $18.89
- **Propina Media:** $2.41
- **Total Amount:** La tarifa total incluye tarifas adicionales y recargos, con una media de $24.53.

## 5. Métodos de Pago

### Taxis Amarillos
- **Método de Pago Más Común:** Tarjeta de crédito

### Taxis Verdes
- **Método de Pago Más Común:** Tarjeta de crédito

## 6. Visualizaciones

### Taxis Amarillos
- Histograma de Duración de Viajes
- Histograma de Distancia de Viajes
- Boxplot de Tarifas Totales
- Distribución de Métodos de Pago
- Boxplot de Propinas

### Taxis Verdes
- Histograma de Duración de Viajes
- Histograma de Distancia de Viajes
- Boxplot de Tarifas Totales
- Distribución de Métodos de Pago
- Boxplot de Propinas

## 7. Conclusiones

**Patrones de Duración y Distancia:**
   - Los taxis amarillos suelen tener viajes más cortos en distancia pero con una mayor cantidad de viajes en comparación con los taxis verdes.
   - Los taxis verdes presentan una mayor variabilidad en las distancias recorridas.

**Tarifas y Propinas:**
   - Las tarifas y propinas medias son comparables entre los taxis amarillos y verdes, aunque los taxis amarillos tienden a tener tarifas ligeramente más altas y propinas mayores.

**Métodos de Pago:**
   - El uso de tarjetas de crédito es el método de pago predominante para ambos tipos de taxis.

**Calidad de los Datos:**
   - Existen algunos valores atípicos y errores de datos que deben ser considerados en análisis futuros, especialmente en las distancias extremadamente altas registradas.

