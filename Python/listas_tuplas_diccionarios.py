'''
# 1. CARGA DE DATOS
'''
ventas = [
    {"fecha": "18-04-2026", "producto": "Laptop", "cantidad": 2, "precio": 800000},
    {"fecha": "18-04-2026", "producto": "Mouse", "cantidad": 5, "precio": 15500},
    {"fecha": "19-04-2026", "producto": "Teclado", "cantidad": 3, "precio": 45000},
    {"fecha": "19-04-2026", "producto": "Laptop", "cantidad": 1, "precio": 800000},
    {"fecha": "20-04-2026", "producto": "Mouse", "cantidad": 4, "precio": 15500},
    {"fecha": "20-04-2026", "producto": "Monitor", "cantidad": 2, "precio": 250000},
    {"fecha": "20-04-2026", "producto": "Teclado", "cantidad": 2, "precio": 45000},
]

'''
# 2. CÁLCULO DE INGRESOS TOTALES
'''
ingresos_totales = 0
for venta in ventas:
    cantidad = venta["cantidad"]
    precio = venta["precio"]
    ingreso_venta = cantidad * precio
    ingresos_totales = ingresos_totales + ingreso_venta

print("INGRESOS TOTALES: $", ingresos_totales, " CLP")
print("")

'''
# 3. ANÁLISIS DEL PRODUCTO MÁS VENDIDO
'''
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    
    # Con esto, respondemos a la pregunta: ¿el producto ya existe en el diccionario?
    if producto in ventas_por_producto:
        ventas_por_producto[producto] = ventas_por_producto[producto] + cantidad
    else:
        ventas_por_producto[producto] = cantidad

# Identificación del producto más vendido
producto_mas_vendido = ""
cantidad_maxima = 0

for producto in ventas_por_producto:
    cantidad = ventas_por_producto[producto]
    if cantidad > cantidad_maxima:
        cantidad_maxima = cantidad
        producto_mas_vendido = producto

print("PRODUCTO MAS VENDIDO:", producto_mas_vendido, "(cantidad:", cantidad_maxima, ")")
print("")

'''
# 4. PROMEDIO DE PRECIO POR PRODUCTO
'''
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]
    
    # Cálculo el ingreso total de esta venta para el producto
    ingreso_producto = cantidad * precio
    
    if producto in precios_por_producto:
        '''Extracción  de la suma de precios y cantidad total actuales para este producto'''  
        suma_precios_actual = precios_por_producto[producto][0]
        cantidad_total_actual = precios_por_producto[producto][1]
        
        # Actualizaamos valores
        nueva_suma_precios = suma_precios_actual + ingreso_producto
        nueva_cantidad_total = cantidad_total_actual + cantidad
        
        # Volcamos el dato actualizado a una tupla (datos no modificables) dentro del diccionario
        precios_por_producto[producto] = (nueva_suma_precios, nueva_cantidad_total)
    else:
        precios_por_producto[producto] = (ingreso_producto, cantidad)

print("PRECIO PROMEDIO POR PRODUCTO:")
for producto in precios_por_producto:
    suma_precios = precios_por_producto[producto][0]
    cantidad_total = precios_por_producto[producto][1]
    precio_promedio = suma_precios / cantidad_total
    print(" ", producto, ": $", precio_promedio, " CLP")
print("")

'''
# 5.  VENTAS POR DÍA ( ingresos por día) 
'''
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]
    ingreso_dia = cantidad * precio
    
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] = ingresos_por_dia[fecha] + ingreso_dia
    else:
        ingresos_por_dia[fecha] =  ingreso_dia

print("INGRESOS POR DIA:")
for  fecha in ingresos_por_dia:
    ingreso = ingresos_por_dia[fecha]
    print(" " , fecha,  ": $", ingreso, " CLP")
print("")

'''
# 6. REPRESENTACIÓN DE DATOS (resumen_ventas)
'''
resumen_ventas = {}

# Recorrer cada producto único
for producto in ventas_por_producto:
    ingresos_totales_producto = 0
    cantidad_total_producto = 0
    
    #  Obtendremos contepto de ingresos y  cantidad total para este producto
    for venta in ventas:
        if venta["producto"] == producto:
            cantidad = venta["cantidad"]
            precio = venta["precio"]
            ingresos_totales_producto  = ingresos_totales_producto +  (cantidad * precio)
            cantidad_total_producto = cantidad_total_producto + cantidad
    
    # Precio promedio
    if cantidad_total_producto > 0:
        precio_promedio = ingresos_totales_producto / cantidad_total_producto
    else:
        precio_promedio = 0
    
    # Diccionario anidado (almacenamos los datos del producto en un diccionario dentro del diccionario resumen_ventas)
    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total_producto,
        "ingresos_totales": ingresos_totales_producto,
        "precio_promedio": precio_promedio
    }

print("RESUMEN DE VENTAS POR PRODUCTO:")
for producto in resumen_ventas:
    datos = resumen_ventas[producto]
    print(" ", producto, ":")
    print("    Cantidad total:", datos["cantidad_total"])
    print("    Ingresos totales: $", datos["ingresos_totales"], " CLP")
    print("    Precio promedio: $", datos["precio_promedio"], " CLP")
    print("")

'''
#7.  GUARDAR RESULTADOS  EN ARCHIVO DE  TEXTO 
'''
archivo = open("resumen_ventas.txt", "w", encoding="utf-8")
archivo.write("="  * 60 + "\n")
archivo.write("ANALISIS DE VENTAS\n" )
archivo.write( "=" * 60 + "\n\n")

# Lista de ventas original
archivo.write("1. LISTA DE VENTAS ORIGINAL:\n")
for i in range(len(ventas)):
    venta = ventas[i]
    archivo.write("   Venta " + str(i+1) + ": " + str(venta) + "\n")
archivo.write("\n")

# Ingresos totales
archivo.write("2. INGRESOS TOTALES: $" + str(ingresos_totales) + " CLP\n\n")

# Producto más vendido
archivo.write("3. PRODUCTO MAS VENDIDO: " + producto_mas_vendido + " (cantidad: " + str(cantidad_maxima) + ")\n\n")

# Precio promedio por producto
archivo.write("4. PRECIO PROMEDIO POR PRODUCTO:\n")
for producto in precios_por_producto:
    suma_precios = precios_por_producto[producto][0]
    cantidad_total = precios_por_producto[producto][1]
    precio_promedio = suma_precios / cantidad_total
    archivo.write("   " + producto + ": $" + str(precio_promedio) + " CLP\n")
archivo.write("\n")

# Ingresos por día
archivo.write("5. INGRESOS POR DIA:\n")
for fecha in ingresos_por_dia:
    ingreso = ingresos_por_dia[fecha]
    archivo.write("   " + fecha + ": $" + str(ingreso) + " CLP\n")
archivo.write("\n")

# Resumen de ventas
archivo.write("6. RESUMEN DE VENTAS POR PRODUCTO:\n")
for producto in resumen_ventas:
    datos = resumen_ventas[producto]
    archivo.write("   " + producto + ":\n")
    archivo.write("      Cantidad total: " + str(datos["cantidad_total"]) + "\n")
    archivo.write("      Ingresos totales: $" + str(datos["ingresos_totales"]) + " CLP\n")
    archivo.write("      Precio promedio: $" + str(datos["precio_promedio"]) + " CLP\n")
archivo.write("\n" + "=" * 60 + "\n")

archivo.close()

print("RESULTADOS GUARDADOS EN 'resumen_ventas.txt'")