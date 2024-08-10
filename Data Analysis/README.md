Irene
# Análisis de Taxis en Nueva York

![Análisis de taxis][Data Analysis/Imagenes_eda/EDA.png]


# Dataset taxi_zone+_lookup.csv
## Conclusión

En este proyecto, se realizó un análisis exhaustivo de los datos de taxi en Nueva York. A continuación, se resumen los principales hallazgos y recomendaciones basados en el análisis de datos:

### **Resumen del Análisis:**
- Se analizaron datos de ubicación de taxis y zonas de servicio en Nueva York,ubicaciónID.
- Se llevo a cabo té análisis exploratorio y visualización para comprender la distribución y calidad de los datos.

### **Hallazgos Clave:**
1. **Distribución de Datos:**
   - La columna `service_zone` muestra una alta concentración en zonas como `Boro Zone`, mientras que `Yellow Zone` es menos representada.
   
2. **Valores Nulos y Duplicados:**
   - Se identificaron algunos valores nulos, pero la mayoría de los datos están completos y sin duplicados significativos.

3. **Frecuencia de Taxis:**
   - Las zonas con alta demanda se concentran en áreas como Manhattan. Zonas con baja demanda presentan oportunidades para mejorar el servicio.

4. **Outliers:**
   - No se encontraron valores extremos significativos en el análisis de outliers.

### **Recomendaciones:**
- **Optimización del Servicio:** Mejorar la asignación de recursos en áreas con alta demanda.
- **Investigación Adicional:** Analizar zonas con baja demanda para identificar oportunidades de mejora.

### **Limitaciones:**
- El análisis se basa en datos disponibles y puede no capturar todas las variaciones en la demanda de taxis. La precisión de la información de ubicación también puede ser una limitación.

### **Próximos Pasos:**
- **Análisis Temporal:** Examinar patrones de demanda a lo largo del tiempo.
- **Limpieza y/o imputación:** Reemplazar o eliminar  datos considerados nulos.
- **Investigación de Factores Externos:** Considerar el impacto de eventos especiales y cambios estacionales en la demanda.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Dataset Zone_taxis.dbf

## Dataset
El dataset contiene las siguientes columnas:

## OBJECTID: Identificador único de la zona.
## Shape_Leng: Longitud del perímetro de la zona en coordenadas geográficas.
## Shape_Area: Área de la zona en unidades cuadradas.
## zone: Nombre descriptivo de la zona.
## LocationID: Identificador de ubicación dentro del dataset.
## borough: Distrito administrativo al que pertenece la zona (por ejemplo,     Manhattan, Queens, Bronx, Staten Island).


# Análisis Realizado
## 1. Exploración de Datos
Número de Filas y Columnas: Se verificó que el dataset tiene un total de 265 filas y 4 columnas.

- Valores Nulos y Faltantes: Se identificaron y trataron valores nulos o faltantes para asegurar la integridad del análisis.
- Valores Duplicados: Se verificó la existencia de filas duplicadas,      encontrando que no hay duplicados en el dataset.
## 2. Análisis de Variables
-Variables Categóricas: Se identificaron las columnas categóricas (zone, borough) para segmentar y analizar la distribución y demanda de taxis en diferentes zonas y distritos.
-Variables Numéricas: Se analizaron las columnas numéricas (Shape_Leng, Shape_Area) para entender la cobertura y el tamaño de cada zona.
## 3. Detección de Outliers
-Método Intercuartílico: Se aplicó el método del rango intercuartílico (IQR) para identificar valores atípicos en las variables numéricas. Se visualizó mediante gráficos de cajas.
## 4. Correlación y Visualización
Matriz de Correlación: Se intentó calcular la matriz de correlación entre variables numéricas para identificar relaciones potenciales. Se encontró un error debido a la presencia de datos no numéricos en el dataset.

# Conclusiones
Cobertura Geográfica: Las columnas Shape_Leng y Shape_Area proporcionan información crucial para evaluar y mejorar la cobertura de los servicios de taxi. Las zonas más grandes o con perímetros más largos pueden requerir más taxis o rutas mejor planificadas.
Segmentación por Borough: El análisis por borough permite optimizar la asignación de recursos y mejorar el servicio en diferentes partes de la ciudad.
Visualización de Datos: Las columnas zone y borough son útiles para crear mapas y gráficos que faciliten la interpretación de los datos y la comunicación de los resultados.
=======

<<<<<<< HEAD
## OBSERVACIONES:
## Objetivo 2 comparación entre taxis eléctricos y de gasolina.
### - Vehicle_Fuel_Economy_Data.csv , columnas        (year-manufacturar-model-fuelCost08,fuelType1)
### - taxi_zones.dbf , columnas (shape-leng y shape-area)
### -taxi+_zone_lookup.csv,columnas (service_zone)
### Estos dataset muestran información de costos de combustibles,area recorrida y frecuencia de alta y baja demanda en donde se puede sacar los km recorridos y calcular el costo de mantenimientos de autos a combustible con los eléctricos en donde se observa gran ventaja a favor y por ende sería rentable para la empresa.

## Objetivo 3 zonas de alta emisión CO2 y ruido:
### zonas_distritos_emisiones.csv muestra de cantidad de emisiones de CO2 en diferentes distritos de Nueva York .







=======
**Exploración de Datos**

1. **Número de Filas y Columnas:**
   * ElectricCarData: 103 filas y 11 columnas.
   * Vehicle Fuel Economy Data: 46,186 filas y 82 columnas.
   * Light Duty Vehicles: 3,008 filas y 29 columnas.
2. **Valores Nulos y Faltantes:**
   * Se identificaron y trataron valores nulos en todos los datasets. Por ejemplo, Electric-Only Range en el dataset Light Duty Vehicles y varias columnas en Vehicle Fuel Economy Data.
3. **Valores Duplicados:**
   * Se verificó la existencia de filas duplicadas, y se encontraron y eliminaron duplicados donde fue necesario para asegurar la integridad del análisis.

**Análisis de Variables**

1. **Variables Categóricas:**
   * ElectricCarData: Brand, Model, RapidCharge, BodyStyle.
   * Vehicle Fuel Economy Data: Manufacturer, Model, fuelType, VClass.
   * Light Duty Vehicles: Manufacturer, Model, Category, Fuel.
2. **Variables Numéricas:**
   * ElectricCarData: TopSpeed, Range, Efficiency, FastCharge, Seats, PriceEuro, Accel.
   * Vehicle Fuel Economy Data: charge240, cityE, co2, combE, fuelCost08, ghgScore, highwayE, range, youSaveSpend.
   * Light Duty Vehicles: Model Year, Electric-Only Range, Alternative Fuel Economy City, Conventional Fuel Economy City.

**Detección de Outliers**

1. **Método Intercuartílico (IQR):**
   * Se aplicó el método del rango intercuartílico (IQR) para identificar valores atípicos en las variables numéricas de los datasets. Los valores atípicos se visualizaron mediante gráficos de cajas para cada dataset.

**Correlación y Visualización**

1. **Matriz de Correlación:**
   * Se calculó la matriz de correlación entre variables numéricas clave en cada dataset para identificar relaciones potenciales.
   * ElectricCarData: Correlación entre TopSpeed, Range, Efficiency, FastCharge, PriceEuro, Seats, Accel.
   * Vehicle Fuel Economy Data: Correlación entre cityE, co2, combE, fuelCost08, ghgScore, highwayE, range, youSaveSpend.
   * Light Duty Vehicles: Correlación entre Model Year, Electric-Only Range, Alternative Fuel Economy City, Conventional Fuel Economy City.


Los datasets **ElectricCarData\_Clean y ElectricCarData\_Norm** contienen información sobre vehículos eléctricos, incluyendo detalles técnicos y económicos, y se centran en especificaciones clave de los autos eléctricos y su rendimiento. Aunque representan los mismos datos, uno está limpio y el otro no, por lo que debemos ajustarlos según nuestro interés.

**Columnas Seleccionadas**

Las columnas seleccionadas aportan valor significativo al análisis del rendimiento y la viabilidad de una flota de taxis eléctricos. Incluyen información esencial sobre la eficiencia energética, capacidad operativa y costos, que son fundamentales para evaluar la rentabilidad y el impacto ambiental de los vehículos.

**Brand:** Texto (Marca del vehículo)

**Model:** Texto (Modelo del vehículo)

**Range:** Texto (Autonomía en km)

**Efficiency:** Texto (Consumo de energía en Wh/km)

**FastCharge:** Texto (Velocidad de carga rápida en km/h)

**RapidCharge:** Texto (Posibilidad de carga rápida: Sí/No)

**Seats:** Número (Número de asientos)

**PriceEuro:** Número (Precio en euros)

**BodyStyle:** Texto (Estilo de carrocería)

**Columnas Descartadas**

Las columnas descartadas no aportan valor crítico al análisis en el contexto de la evaluación operativa y económica de una flota de taxis eléctricos. Aunque proporcionan detalles adicionales sobre el vehículo, no son esenciales para el análisis de eficiencia, autonomía y costos operativos necesarios para tomar decisiones informadas sobre la implementación de taxis eléctricos.

**TopSpeed:** Texto (Velocidad máxima en km/h)

**PlugType: Texto** (Tipo de enchufe)

**Accel:** Texto (Aceleración en segundos)

**Segment:** Texto (Segmento del vehículo)

**Insights Clave del EDA**

1. **Distribución de Vehículos por Marca y Modelo**:
   * La mayoría de los vehículos eléctricos tienen una aceleración rápida, con un valor común de 7.5 segundos.
2. **Velocidad Máxima y Autonomía**:
   * Los vehículos más comunes alcanzan una velocidad máxima de 150 km/h, siendo la velocidad máxima disponible de 400 km/h.
   * La autonomía de la mayoría de los vehículos está en torno a los 400 km con una carga completa.
3. **Consumo de Energía y Número de Asientos**:
   * La mayoría de los vehículos tienen un consumo eficiente de energía.
   * En promedio, los vehículos eléctricos tienen 5 asientos.
4. **Precio de los Vehículos**:
   * El precio promedio de los vehículos eléctricos ronda los 40,000 euros.
5. **Correlación entre Variables Clave de Vehículos Eléctricos**
   * Muestra las relaciones entre velocidad máxima, autonomía, eficiencia energética, velocidad de carga rápida, precio, número de asientos y aceleración mediante un heatmap, ayudando a identificar patrones y asociaciones significativas entre estas características.

**Visualizaciones Clave**

1. **Histograma: Distribución de Vehículos por Marca y Modelo**
   * Muestra la cantidad de vehículos registrados para cada marca y modelo.
2. **Scatter Plot: Relación entre Velocidad Máxima y Autonomía**
   * Visualiza cómo se distribuyen los vehículos en función de su velocidad máxima y autonomía.
3. **Boxplot: Distribución del Consumo de Energía**
   * Presenta la distribución del consumo de energía en Wh/km.
4. **Histograma: Distribución de Precios de Vehículos Eléctricos**
   * Muestra la distribución de los precios de los vehículos eléctricos en euros.

**Conclusión**

* **Rendimiento y Eficiencia**: Los vehículos eléctricos muestran una tendencia hacia altas velocidades máximas y eficiencias energéticas.
* **Viabilidad Económica**: El precio promedio de 40,000 euros sugiere una accesibilidad razonable para el mercado de taxis eléctricos.
* **Eficiencia Operativa**: Vehículos con mayor autonomía y eficiencia energética son ideales para una flota de taxis eléctricos.

El dataset **Vehicle\_Fuel\_Economy\_Data** proporciona información sobre la economía de combustible y las emisiones de CO2 de los vehículos. Contiene detalles como el año del modelo, fabricante, modelo, tipo de combustible y su autonomía en diferentes modos, así como características del motor y de carga. La información está enfocada en el rendimiento del combustible y las emisiones, permitiendo analizar la eficiencia y el impacto ambiental de los vehículos.

**Columnas Seleccionadas**

Las columnas seleccionadas aportan valor significativo al análisis del rendimiento y la viabilidad de una flota de taxis eléctricos. Incluyen información esencial sobre la eficiencia energética, capacidad operativa y costos, que son fundamentales para evaluar la rentabilidad y el impacto ambiental de los vehículos.

**Year: Año del modelo del vehículo.**

**Manufacturer: Fabricante del vehículo.**

**Model: Modelo del vehículo.**

**charge240: Tiempo de carga en horas con un cargador de 240V.**

**cityE: Consumo de combustible en ciudad en modo eléctrico**

**city08: Consumo de combustible en ciudad (millas por galón, MPG).**

**co2: Emisiones de CO2 en gramos por milla.**

**co2A: Emisiones de CO2 en modo alternativo.**

**co2TailpipeAGpm: Emisiones de CO2 del tubo de escape en modo alternativo (gramos por milla).**

**co2TailpipeGpm: Emisiones de CO2 del tubo de escape (gramos por milla).**

**combE: Consumo de combustible combinado en modo eléctrico.**

**feScore: Puntaje de eficiencia de combustible.**

**fuelCost08: Costo estimado de combustible en un año**

**fuelType: Tipo de combustible.**

**fuelType1: Primer tipo de combustible.**

**ghgScore: Puntaje de gases de efecto invernadero**

**VClass: Clase del vehículo.**

**highwayCD: Consumo de combustible en carretera con carga directa.**

**highwayE: Consumo de combustible en carretera en modo eléctrico.**

**highwayUF: Consumo de combustible en carretera en modo UF.**

**hlv: Volumen del compartimiento de carga (high load volume).**

**hpv: Volumen del compartimiento de carga (high passenger volume).**

**id: Identificación del vehículo.**

**pv2: Volumen del compartimiento de pasajeros en configuración de dos pasajeros.**

**pv4: Volumen del compartimiento de pasajeros en configuración de cuatro pasajeros.**

**range: Autonomía del vehículo.**

**rangeCity: Autonomía en ciudad**

**youSaveSpend: Ahorro o gasto estimado comparado con el vehículo promedio.**

**guzzler: Si el vehículo es un gran consumidor de combustible.**

**sCharger: Si tiene supercargador.**

**evMotor: Tipo de motor eléctrico.**

**c240Dscr: Descripción del cargador de 240V.**

**charge240b: Tiempo de carga con un cargador de 240V de respaldo.**

**c240bDscr: Descripción del cargador de 240V de respaldo.**

**startStop: Si el vehículo tiene sistema de arranque y parada.**

**Columnas Descartadas**

Las columnas descartadas no aportan valor crítico al análisis en el contexto de la evaluación operativa y económica de una flota de taxis eléctricos. Aunque proporcionan detalles adicionales sobre el vehículo, no son esenciales para el análisis de eficiencia, autonomía y costos operativos necesarios para tomar decisiones informadas sobre la implementación de taxis eléctricos.

**barrels08**: Consumo de barriles de combustible en un año para el ciclo de manejo en ciudad.

**barrelsA08**: Consumo de barriles de combustible en un año para el ciclo de manejo alternativo.

**city08U**: Consumo de combustible en ciudad en modo US.

**cityA08**: Consumo de combustible en ciudad en modo alternativo.

**cityA08U**: Consumo de combustible en ciudad en modo alternativo US.

**cityCD**: Consumo de combustible en ciudad con carga directa.

**cityUF**: Consumo de combustible en ciudad en modo UF.

**comb08**: Consumo de combustible combinado (ciudad y carretera, MPG).

**comb08U**: Consumo de combustible combinado en modo US.

**combA08**: Consumo de combustible combinado en modo alternativo.

**combA08U**: Consumo de combustible combinado en modo alternativo US.

**combinedCD**: Consumo de combustible combinado con carga directa.

**combinedUF**: Consumo de combustible combinado en modo UF.

**cylinders**: Número de cilindros del motor.

**displ**: Desplazamiento del motor en litros.

**drive**: Tipo de tracción (e.g., Tracción trasera, Tracción delantera).

**engId**: Identificación del motor.

**eng\_dscr**: Descripción del motor.

**fuelCostA08**: Costo estimado de combustible en un año en modo alternativo.

**ghgScoreA**: Puntaje de gases de efecto invernadero en modo alternativo.

**highway08**: Consumo de combustible en carretera (MPG).

**highway08U**: Consumo de combustible en carretera en modo US.

**highwayA08**: Consumo de combustible en carretera en modo alternativo.

**highwayA08U**: Consumo de combustible en carretera en modo alternativo US.

**highwayUF**: Consumo de combustible en carretera en modo UF.

**lv2**: Volumen del compartimiento de carga en configuración baja.

**lv4**: Volumen del compartimiento de carga en configuración baja.

**mpgData**: Datos de millas por galón.

**phevBlended**: Si el vehículo es híbrido enchufable con modo combinado

**rangeCityA**: Autonomía en ciudad en modo alternativo.

**rangeHwy**: Autonomía en carretera.

**rangeHwyA**: Autonomía en carretera en modo alternativo.

**trany**: Tipo de transmisión.

**UCity**: Consumo de combustible en ciudad en modo US.

**UCityA**: Consumo de combustible en ciudad en modo alternativo US.

**UHighway**: Consumo de combustible en carretera en modo US.

**UHighwayA**: Consumo de combustible en carretera en modo alternativo US.

**trans\_dscr**: Descripción de la transmisión.

**tCharger**: Si tiene turbocargador.

**atvType**: Tipo de vehículo todo terreno.

**fuelType2**: Segundo tipo de combustible.

**rangeA**: Autonomía en modo alternativo.

**mfrCode**: Código del fabricante.

**createdOn**: Fecha de creación del registro.

**modifiedOn**: Fecha de última modificación del registro

**startStop**: Si el vehículo tiene sistema de arranque y parada.

**Insights Clave del EDA**

1. **Distribución de Vehículos por Año**:
   * La mayoría de los vehículos eléctricos tienen una aceleración rápida, con un valor común de 7.5 segundos.
2. **Velocidad Máxima y Autonomía**:
   * Los vehículos más comunes alcanzan una velocidad máxima de 150 km/h, siendo la velocidad máxima disponible de 400 km/h.
   * La autonomía de la mayoría de los vehículos está en torno a los 400 km con una carga completa.
3. **Consumo de Energía y Número de Asientos**:
   * La mayoría de los vehículos tienen un consumo eficiente de energía.
   * En promedio, los vehículos eléctricos tienen 5 asientos.
4. **Precio de los Vehículos**:
   * El precio promedio de los vehículos eléctricos ronda los 40,000 euros.
5. **Heatmap: Correlación entre Variables Clave de Vehículos Eléctricos**:
   * Muestra las relaciones entre velocidad máxima, autonomía, eficiencia energética, velocidad de carga rápida, precio, número de asientos y aceleración, ayudando a identificar patrones y asociaciones significativas entre estas características.

**Conclusión**

* **Rendimiento y Eficiencia**: Los vehículos eléctricos muestran una tendencia hacia altas velocidades máximas y eficiencias energéticas.
* **Viabilidad Económica**: El precio promedio de 40,000 euros sugiere una accesibilidad razonable para el mercado de taxis eléctricos.
* **Eficiencia Operativa**: Vehículos con mayor autonomía y eficiencia energética son ideales para una flota de taxis eléctricos.

El dataset **Light\_Duty\_Vehicles** proporciona información detallada sobre vehículos, incluyendo su identificación, fabricante, modelo, año y tipo de combustible. Además, ofrece datos sobre la autonomía en modo eléctrico, que permite un análisis completo del rendimiento y características de diversos vehículos.

**Columnas Seleccionadas**

Las columnas seleccionadas aportan valor significativo al análisis del rendimiento y la viabilidad de los vehículos en términos de eficiencia y características operativas. Estas incluyen información esencial sobre la identificación del vehículo, fabricante, modelo, año, tipo de combustible y autonomía en modo eléctrico, que son fundamentales para evaluar el rendimiento y el impacto ambiental de los vehículos.

**Vehicle ID**: Identificación única del vehículo

**Model**: Modelo del vehículo.

**Model Year**: Año del modelo del vehículo.

**Manufacturer**: Nombre del fabricante del vehículo

**Category**: Categoría del vehículo (e.g., Sedán, SUV).

**Fuel**: Tipo de combustible (e.g., gasolina, electricidad).

**Electric-Only Range**: Autonomía en modo eléctrico solamente

**Columnas Descartadas**

Las columnas descartadas no aportan valor crítico al análisis en el contexto de la evaluación operativa y ambiental de los vehículos. Aunque proporcionan detalles adicionales sobre el motor y la configuración del combustible, no son esenciales para el análisis de eficiencia, autonomía y características operativas necesarias para tomar decisiones informadas sobre el rendimiento de los vehículos.


**Category ID**: Identificación de la categoría del vehículo.

**Manufacturer ID**: Identificación del fabricante.

**Fuel ID**: Identificación del tipo de combustible.

**Fuel Configuration ID**: Identificación de la configuración del combustible.

**Alternative Fuel Economy City**: Consumo de combustible en ciudad usando combustible alternativo (millas por galón, MPG).

**Alternative Fuel Economy Highway**: Consumo de combustible en carretera usando combustible alternativo (MPG).

**Alternative Fuel Economy Combined**: Consumo de combustible combinado (ciudad y carretera) usando combustible alternativo (MPG).

**Conventional Fuel Economy City**: Consumo de combustible en ciudad usando combustible convencional (MPG).

**Conventional Fuel Economy Highway**: Consumo de combustible en carretera usando combustible convencional (MPG).

**Conventional Fuel Economy Combined**: Consumo de combustible combinado (ciudad y carretera) usando combustible convencional (MPG).

**Transmission Type**: Tipo de transmisión del vehículo (e.g., automática, manual).

**Engine Type**: Tipo de motor (e.g., SI para inyección de gasolina).

**Engine Size**: Tamaño del motor en litros (litros).

**Engine Cylinder Count**: Número de cilindros del motor.

**Engine Description**: Descripción del motor.

**Manufacturer URL**: URL del sitio web del fabricante.

**Fuel Code**: Código del tipo de combustible.

**Fuel Configuration Name**: Nombre de la configuración del combustible.

**PHEV Total Range**: Autonomía total en modo híbrido enchufable.

**PHEV Type**: Tipo de híbrido enchufable (e.g., tipo de batería).

**Notes**: Notas adicionales sobre el vehículo.

**Drivetrain**: Tipo de tracción del vehículo (e.g., AWD, FWD).

**Insights Clave del EDA**

1. **Distribución de Vehículos por Año y Fabricante**:
   * La mayoría de los vehículos en el dataset son modelos recientes, especialmente a partir de 2020.
2. **Categorías de Vehículos**:
   * Los vehículos están categorizados principalmente como Sedan/Wagon y SUV.
3. **Tipos de Combustible**:
   * Predomina el uso de Hybrid Electric, indicando una transición hacia vehículos más eficientes en consumo de combustible.
4. **Autonomía en Modo Eléctrico**:
   * La mayoría de los vehículos no tienen una autonomía en modo eléctrico registrada, lo que sugiere que el enfoque principal aún está en los híbridos y no completamente eléctricos.

**Conclusiones**

* **Rendimiento y Eficiencia**: Los vehículos eléctricos y los híbridos muestran una tendencia hacia una mejor eficiencia en comparación con los vehículos de combustible convencional. La mayoría de los vehículos en el dataset son modelos recientes, lo que refleja una evolución hacia tecnologías más eficientes.

* **Viabilidad Operativa**: La autonomía en modo eléctrico es una característica clave para evaluar la viabilidad de los vehículos eléctricos en términos de operación diaria. Aunque muchos vehículos en el dataset no tienen una autonomía eléctrica registrada, los que sí la tienen muestran una variabilidad significativa, lo que puede influir en la elección de vehículos para diferentes usos.

* **Preferencia por Tipos de Combustible**: La preferencia por tipos de combustible híbrido y eléctrico indica una transición hacia vehículos más sostenibles y eficientes. Esto es crucial para reducir las emisiones y mejorar la eficiencia energética en el sector de transporte.

* **Categorías de Vehículos**: La predominancia de categorías como Sedan/Wagon y SUV sugiere que estos tipos de vehículos son los más comunes en el dataset, lo que puede influir en las tendencias de mercado y la planificación de flotas de vehículos.
>>>>>>> ee3981016ed281f100f7c620c46fd595a68c0cce

