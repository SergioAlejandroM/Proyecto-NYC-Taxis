Diccionario de datos:

1) ElectricCarData_Clean y ElectricCarData_Norm

Los datasets ElectricCarData_Clean y ElectricCarData_Norm contienen información sobre vehículos eléctricos, incluyendo detalles técnicos y económicos, y se centran en especificaciones clave de los autos eléctricos y su rendimiento. Aunque representan los mismos datos, uno está limpio y el otro no, por lo que debemos ajustarlos según nuestro interés.

Columnas a tener en cuenta: 

	* Brand: Texto (Marca del vehículo)
    * Model: Texto (Modelo del vehículo)
	* TopSpeed: Texto (Velocidad máxima en km/h)
	* Range: Texto (Autonomía en km)
	* Efficiency: Texto (Consumo de energía en Wh/km)
	* FastCharge: Texto (Velocidad de carga rápida en km/h)
	* RapidCharge: Texto (Posibilidad de carga rápida: Sí/No)
    * Seats: Número (Número de asientos)
	* PriceEuro: Número (Precio en euros)

Posibles columnas a descartar:

    * Accel: Texto (Aceleración en segundos)
    * PlugType: Texto (Tipo de enchufe)
    * BodyStyle: Texto (Estilo de carrocería)
    * Segment: Texto (Segmento del vehículo)

Como insights a tener en cuenta se pudo observar que en nuestro dataset los registro consta en su mayoria de vehiculos electricos que aceleran en poco tiempo siendo siendo 7.5 el valor de los vehiculos que mas hay.

que en su mayoria el registro que mas se repite es de vehiculos que alcanzan una velocidad de 150Km y que la velocidad maxima de los vehiculos disponible es de 400km

que el rendimiento de la cantidad de vehiculos que mas se repite suele estar entre los 400km que este puede recorrer con una carga completa

se observa que la gran mayoria de los registro de los vehiculos electricos tienen un consumo eficiente de energia y tambien que los vehiculos en promedio son de 5 puestos.

el promedio de los precios de los vehiculos electricos suele rondar aproximadamente entre los 40.000 Euros



2) Light Duty Vehicles

Este dataset proporciona información detallada sobre vehículos, incluyendo su identificación, fabricante, modelo, año y tipo de combustible. Además, ofrece datos sobre la autonomía en modo eléctrico, que permitira un análisis completo del rendimiento y características de diversos vehículos.

Columnas a tener en cuenta: 

    * Vehicle ID: Identificación única del vehículo
    * Manufacturer ID: Identificación del fabricante.
    * Category ID: Identificación de la categoría del vehículo.
    * Model: Modelo del vehículo.
    * Model Year: Año del modelo del vehículo.
    * Manufacturer: Nombre del fabricante del vehículo
    * Category: Categoría del vehículo (e.g., Sedán, SUV).
    * Fuel: Tipo de combustible (e.g., gasolina, electricidad).
    * Electric-Only Range: Autonomía en modo eléctrico solamente


Posibles columnas a descartar:

    * Fuel ID: Identificación del tipo de combustible.
    * Fuel Configuration ID: Identificación de la configuración del combustible.
    * Alternative Fuel Economy City: Consumo de combustible en ciudad usando combustible alternativo (millas por galón, MPG).
    * Alternative Fuel Economy Highway: Consumo de combustible en carretera usando combustible alternativo (MPG).
    * Alternative Fuel Economy Combined: Consumo de combustible combinado (ciudad y carretera) usando combustible alternativo (MPG).
    * Conventional Fuel Economy City: Consumo de combustible en ciudad usando combustible convencional (MPG).
    * Conventional Fuel Economy Highway: Consumo de combustible en carretera usando combustible convencional (MPG).
    * Conventional Fuel Economy Combined: Consumo de combustible combinado (ciudad y carretera) usando combustible convencional (MPG).
    * Transmission Type: Tipo de transmisión del vehículo (e.g., automática, manual).
    * Engine Type: Tipo de motor (e.g., SI para inyección de gasolina).
    * Engine Size: Tamaño del motor en litros (litros).
    * Engine Cylinder Count: Número de cilindros del motor.
    * Engine Description: Descripción del motor.
    * Manufacturer URL: URL del sitio web del fabricante.
    * Fuel Code: Código del tipo de combustible.
    * Fuel Configuration Name: Nombre de la configuración del combustible.
    * PHEV Total Range: Autonomía total en modo híbrido enchufable.
    * PHEV Type: Tipo de híbrido enchufable (e.g., tipo de batería).
    * Notes: Notas adicionales sobre el vehículo.
    * Drivetrain: Tipo de tracción del vehículo (e.g., AWD, FWD).

Como insights a tener en cuenta se ve que la gran mayoria de datos de los modelos de vehiculos pertenecen al año del 2022, siendo este año donde predomina la cantidad de modelos mas recientes en este dataset.

Se puede observar el rendimiento del combustible de distintos modelos de vehiculos en distintas condiciones como podria ser una carretera, una ciudad o su desempeño en ambas

3) Vehicle_Fuel_Economy_Data

El dataset proporciona información sobre la economía de combustible y las emisiones de CO2 de los vehículos. Contiene detalles como el año del modelo, fabricante, modelo, tipo de combustible y su autonomía en diferentes modos, así como características del motor y de carga. La información está enfocada en el rendimiento del combustible y las emisiones, permitiendo analizar la eficiencia y el impacto ambiental de los vehículos.

Columnas a tener en cuenta: 

    * Year: Año del modelo del vehículo.
    * Manufacturer: Fabricante del vehículo.
    * Model: Modelo del vehículo.
    * charge240: Tiempo de carga en horas con un cargador de 240V.
    * cityE: Consumo de combustible en ciudad en modo eléctrico
    * co2: Emisiones de CO2 en gramos por milla.
    * co2A: Emisiones de CO2 en modo alternativo.
    * co2TailpipeAGpm: Emisiones de CO2 del tubo de escape en modo alternativo (gramos por milla).
    * co2TailpipeGpm: Emisiones de CO2 del tubo de escape (gramos por milla).
    * combE: Consumo de combustible combinado en modo eléctrico.
    * feScore: Puntaje de eficiencia de combustible.
    * fuelCost08: Costo estimado de combustible en un año
    * fuelType: Tipo de combustible.
    * fuelType1: Primer tipo de combustible.
    * ghgScore: Puntaje de gases de efecto invernadero
    * VClass: Clase del vehículo.
    * highwayCD: Consumo de combustible en carretera con carga directa.
    * highwayE: Consumo de combustible en carretera en modo eléctrico.
    * highwayUF: Consumo de combustible en carretera en modo UF.
    * hlv: Volumen del compartimiento de carga (high load volume).
    * hpv: Volumen del compartimiento de carga (high passenger volume).
    * id: Identificación del vehículo.
    * pv2: Volumen del compartimiento de pasajeros en configuración de dos pasajeros.
    * pv4: Volumen del compartimiento de pasajeros en configuración de cuatro pasajeros.
    * range: Autonomía del vehículo.
    * rangeCity: Autonomía en ciudad
    * youSaveSpend: Ahorro o gasto estimado comparado con el vehículo promedio.
    * guzzler: Si el vehículo es un gran consumidor de combustible.
    * sCharger: Si tiene supercargador.
    * evMotor: Tipo de motor eléctrico.
    * c240Dscr: Descripción del cargador de 240V.
    * charge240b: Tiempo de carga con un cargador de 240V de respaldo.
    * c240bDscr: Descripción del cargador de 240V de respaldo.
    * startStop: Si el vehículo tiene sistema de arranque y parada.


Posibles columnas a descartar:

    * barrels08: Consumo de barriles de combustible en un año para el ciclo de manejo en ciudad.
    * barrelsA08: Consumo de barriles de combustible en un año para el ciclo de manejo alternativo.
    * city08: Consumo de combustible en ciudad (millas por galón, MPG).
    * city08U: Consumo de combustible en ciudad en modo US.
    * cityA08: Consumo de combustible en ciudad en modo alternativo.
    * cityA08U: Consumo de combustible en ciudad en modo alternativo US.
    * cityCD: Consumo de combustible en ciudad con carga directa.
    * cityUF: Consumo de combustible en ciudad en modo UF.
    * comb08: Consumo de combustible combinado (ciudad y carretera, MPG).
    * comb08U: Consumo de combustible combinado en modo US.
    * combA08: Consumo de combustible combinado en modo alternativo.
    * combA08U: Consumo de combustible combinado en modo alternativo US.
    * combinedCD: Consumo de combustible combinado con carga directa.
    * combinedUF: Consumo de combustible combinado en modo UF.
    * cylinders: Número de cilindros del motor.
    * displ: Desplazamiento del motor en litros.
    * drive: Tipo de tracción (e.g., Tracción trasera, Tracción delantera).
    * engId: Identificación del motor.
    * eng_dscr: Descripción del motor.
    * fuelCostA08: Costo estimado de combustible en un año en modo alternativo.
    * ghgScoreA: Puntaje de gases de efecto invernadero en modo alternativo.
    * highway08: Consumo de combustible en carretera (MPG).
    * highway08U: Consumo de combustible en carretera en modo US.
    * highwayA08: Consumo de combustible en carretera en modo alternativo.
    * highwayA08U: Consumo de combustible en carretera en modo alternativo US.
    * highwayUF: Consumo de combustible en carretera en modo UF.
    * lv2: Volumen del compartimiento de carga en configuración baja.
    * lv4: Volumen del compartimiento de carga en configuración baja.
    * mpgData: Datos de millas por galón.
    * phevBlended: Si el vehículo es híbrido enchufable con modo combinado
    * rangeCityA: Autonomía en ciudad en modo alternativo.
    * rangeHwy: Autonomía en carretera.
    * rangeHwyA: Autonomía en carretera en modo alternativo.
    * trany: Tipo de transmisión.
    * UCity: Consumo de combustible en ciudad en modo US.
    * UCityA: Consumo de combustible en ciudad en modo alternativo US.
    * UHighway: Consumo de combustible en carretera en modo US.
    * UHighwayA: Consumo de combustible en carretera en modo alternativo US.
    * trans_dscr: Descripción de la transmisión.
    * tCharger: Si tiene turbocargador.
    * atvType: Tipo de vehículo todo terreno.
    * fuelType2: Segundo tipo de combustible.
    * rangeA: Autonomía en modo alternativo.
    * mfrCode: Código del fabricante.
    * createdOn: Fecha de creación del registro.
    * modifiedOn: Fecha de última modificación del registro
    * startStop: Si el vehículo tiene sistema de arranque y parada.

Como insights a tener en cuenta se observa que hay distintos tipos de vehiculos con una varidad que usan distintos tipos de combustibles e incluso puede llegar a ser combinados y tambien el tipo de carga que este usa

se puede observar tambien el desempeño que este tiene a nivel de rendimiento operativo en cierta condiciones