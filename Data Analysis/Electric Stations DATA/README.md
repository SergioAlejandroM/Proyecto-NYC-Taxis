# Análisis Preliminar de la Base de Datos "Electric and Alternative Fuel Charging Stations"

## 1. Descripción General
La base de datos contiene 70,406 registros sobre estaciones de carga para vehículos eléctricos y de combustible alternativo en diversas ubicaciones. Cada registro incluye información detallada sobre la estación como la ubicación, el tipo de combustible, las características de los cargadores y más.

## 2. Columnas Principales
- **Fuel Type Code:** Código del tipo de combustible.
- **Station Name:** Nombre de la estación.
- **Street Address:** Dirección de la estación.
- **Intersection Directions:** Indicaciones para llegar a la estación.
- **City:** Ciudad donde se encuentra la estación.
- **State:** Estado donde se encuentra la estación.
- **ZIP:** Código postal de la estación.
- **Plus4:** Extensión del código postal.
- **Station Phone:** Número de teléfono de la estación.
- **Status Code:** Código de estado de la estación (operativa, en construcción, etc.).
- **Expected Date:** Fecha esperada de operación.
- **Groups With Access Code:** Código de acceso para grupos.
- **Access Days Time:** Días y horas de acceso.
- **Cards Accepted:** Tarjetas aceptadas para el pago.
- **BD Blends:** Tipos de mezclas de biodiésel disponibles.
- **NG Fill Type Code:** Código de tipo de llenado de gas natural.
- **NG PSI:** Presión del gas natural.
- **EV Level1 EVSE Num:** Número de cargadores de nivel 1.
- **EV Level2 EVSE Num:** Número de cargadores de nivel 2.
- **EV DC Fast Count:** Número de cargadores de carga rápida DC.
- **EV Other Info:** Otra información relevante sobre la estación de carga.
- **EV Network:** Red de carga a la que pertenece la estación.
- **EV Network Web:** Sitio web de la red de carga.
- **Geocode Status:** Estado del geocódigo.
- **Latitude:** Latitud de la estación.
- **Longitude:** Longitud de la estación.
- **Date Last Confirmed:** Fecha de última confirmación de operación.
- **ID:** Identificador único de la estación.
- **Updated At:** Fecha de la última actualización de los datos.
- **Owner Type Code:** Código del tipo de propietario.
- **Federal Agency ID:** Identificador de la agencia federal si aplica.
- **Federal Agency Name:** Nombre de la agencia federal si aplica.
- **Open Date:** Fecha de apertura de la estación.
- **Hydrogen Status Link:** Enlace al estado del hidrógeno.
- **NG Vehicle Class:** Clase de vehículo de gas natural soportado.
- **LPG Primary:** Información primaria sobre LPG.
- **E85 Blender Pump:** Información sobre bombas de mezcla E85.
- **EV Connector Types:** Tipos de conectores EV disponibles.
- **Country:** País donde se encuentra la estación.
- **Intersection Directions (French):** Indicaciones para llegar a la estación en francés.
- **Access Days Time (French):** Días y horas de acceso en francés.
- **BD Blends (French):** Tipos de mezclas de biodiésel disponibles en francés.
- **Groups With Access Code (French):** Código de acceso para grupos en francés.
- **Hydrogen Is Retail:** Indicador si el hidrógeno está disponible para venta al por menor.
- **Access Code:** Código de acceso.
- **Access Detail Code:** Código de detalles de acceso.
- **Federal Agency Code:** Código de la agencia federal.
- **Facility Type:** Tipo de instalación.
- **CNG Dispenser Num:** Número de dispensadores de CNG.
- **CNG On-Site Renewable Source:** Fuente renovable de CNG en el sitio.
- **CNG Total Compression Capacity:** Capacidad total de compresión de CNG.
- **CNG Storage Capacity:** Capacidad de almacenamiento de CNG.
- **LNG On-Site Renewable Source:** Fuente renovable de LNG en el sitio.
- **E85 Other Ethanol Blends:** Otras mezclas de etanol E85 disponibles.
- **EV Pricing:** Precios de carga EV.
- **EV Pricing (French):** Precios de carga EV en francés.
- **LPG Nozzle Types:** Tipos de boquillas de LPG.
- **Hydrogen Pressures:** Presiones del hidrógeno.
- **Hydrogen Standards:** Estándares del hidrógeno.
- **CNG Fill Type Code:** Código de tipo de llenado de CNG.
- **CNG PSI:** Presión del CNG.
- **CNG Vehicle Class:** Clase de vehículo de CNG soportado.
- **LNG Vehicle Class:** Clase de vehículo de LNG soportado.
- **EV On-Site Renewable Source:** Fuente renovable de EV en el sitio.
- **Restricted Access:** Indicador de acceso restringido.

## 3. Análisis Descriptivo

### Distribución Geográfica
Las estaciones están distribuidas en varias ciudades y estados con detalles específicos de latitud y longitud.

### Tipos de Combustible y Cargadores
Varias estaciones soportan múltiples tipos de combustibles alternativos y niveles de carga eléctrica.

### Acceso y Operación
Información detallada sobre los horarios de operación y los métodos de pago aceptados en cada estación.

## 4. Uso Específico de las Columnas

### Ubicación y Densidad de Estaciones
- **Street Address**, **City**, **State**, **ZIP**, **Latitude**, **Longitude**: Evaluar la densidad y accesibilidad de las estaciones de carga en Nueva York.

### Capacidad y Tipo de Cargadores
- **EV Level1 EVSE Num**, **EV Level2 EVSE Num**, **EV DC Fast Count**, **EV Connector Types**: Analizar la capacidad de carga y tipos de conectores disponibles para asegurar la compatibilidad con la flota de taxis eléctricos.

### Disponibilidad y Acceso
- **Access Days Time**, **Restricted Access**: Evaluar los horarios de operación y restricciones de acceso para planificar la disponibilidad de carga para la flota de taxis.

### Costos Operativos
- **EV Pricing**: Analizar los costos de carga en diferentes estaciones para calcular los costos operativos de la flota de taxis eléctricos.

### Actualidad y Operatividad
- **Status Code**, **Date Last Confirmed**, **Open Date**: Asegurar que las estaciones de carga están operativas y los datos son actuales.

## 5. Análisis Propuesto

### Mapeo Geoespacial
Utilizar las columnas de ubicación para mapear las estaciones de carga en Nueva York y evaluar su distribución.

### Evaluación de Capacidad
Analizar la capacidad de carga de las estaciones para determinar si pueden soportar la demanda de una flota de taxis eléctricos.

### Análisis de Costos
Comparar los costos de carga en diferentes estaciones para calcular los costos operativos y evaluar la viabilidad económica.

### Análisis de Disponibilidad
Evaluar los horarios de operación y accesibilidad de las estaciones para planificar la carga eficiente de la flota.
