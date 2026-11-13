# Dashboard de Control de Ventas

## Microtaller 6 – Gestión y análisis de información

**Responsable:** Nelson Julián Martínez Bedoya  
**Proyecto:** Control de ventas  
**Periodo de análisis:** 1 al 10 de noviembre de 2026

## Enlaces del proyecto

- **Dashboard publicado:** [Ver dashboard de control de ventas](https://mrtnzjuliancho-svg.github.io/control-ventas-nelson/ )
- **Repositorio en GitHub:** [Ver repositorio del proyecto](https://github.com/mrtnzjuliancho-svg/control-ventas-nelson )

## Descripción del proyecto

Este proyecto presenta una solución web para registrar y analizar las ventas diarias de un negocio. El dashboard permite consultar las ventas totales, las unidades comercializadas, los productos con mayor movimiento y el comportamiento de las ventas durante el periodo analizado.

La información utilizada está compuesta por 20 registros ficticios creados únicamente con fines académicos. Cada registro contiene la fecha, el producto, la categoría, la ciudad, el vendedor, las unidades y el precio unitario.

## Identificación del problema

Cuando las ventas se registran de manera dispersa, resulta difícil conocer cuánto se ha vendido, cuáles productos generan más ingresos y qué días presentan mejores resultados. También puede ser complicado comparar la información si los datos no se encuentran organizados.

Para solucionar esta situación se desarrolló un dashboard interactivo que reúne la información de las ventas y la presenta mediante indicadores y gráficos. De esta manera, los resultados pueden consultarse de forma rápida y ordenada.

## Construcción de datos

La base de datos contiene 20 registros ficticios de ventas realizadas entre el 1 y el 10 de noviembre de 2026.

Los campos utilizados son:

- Fecha de la venta.
- Producto.
- Categoría.
- Ciudad.
- Vendedor.
- Unidades vendidas.
- Precio unitario.
- Total de la venta.

El total de cada venta se obtiene multiplicando las unidades vendidas por el precio unitario.

## Indicadores KPI

El dashboard presenta los siguientes indicadores:

- Ventas totales.
- Unidades vendidas.
- Registros de venta.
- Ticket promedio.

Los resultados generales obtenidos fueron:

- **Ventas totales:** $34.100.000.
- **Unidades vendidas:** 106.
- **Registros de venta:** 20.
- **Ticket promedio:** $1.705.000.
- **Producto con mayor aporte:** Portátil.
- **Categoría con mayores ventas:** Tecnología.

## Visualizaciones del dashboard

El dashboard incluye tres gráficos principales:

1. Ventas por día.
2. Ventas por producto.
3. Ventas por categoría.

También cuenta con filtros por categoría y ciudad. Cuando se cambia un filtro, los indicadores, los gráficos y la tabla de registros se actualizan automáticamente.

## Desarrollo técnico

La versión web fue construida utilizando HTML, CSS y JavaScript. Los gráficos se desarrollaron mediante la API Canvas, por lo que no es necesario instalar librerías externas.

La página puede abrirse directamente desde un navegador y también puede publicarse en GitHub Pages. Además, se preparó una versión de escritorio en Python para ejecutar el dashboard como programa independiente en Windows.

## Tecnologías utilizadas

- HTML5.
- CSS3.
- JavaScript.
- Canvas API.
- Python.
- Tkinter.
- GitHub Pages.

## Archivos principales

```text
index.html
README.md
