
# Ejercicio: Beneficios para Nuevos Empleados

Una empresa de tecnología ofrece distintos beneficios económicos a sus nuevos empleados en función de su rendimiento en el proceso de selección y la ciudad desde la cual provienen.

El rendimiento se evalúa con una nota de 1.0 a 7.0, y las ciudades están agrupadas en tres zonas: Zona Norte, Zona Centro y Zona Sur. El beneficio consiste en un descuento aplicado sobre un bono anual de $2.500.000, según las siguientes condiciones:

## Descuentos:

| Evaluación de ingreso | Zona de origen | Descuento sobre bono |
|------------------------|----------------|------------------------|
| Nota mayor a 6.0       | Zona Sur       | 25%                   |
| Nota mayor a 6.0       | Zona Centro    | 20%                   |
| Nota entre 5.0 y 6.0   | Zona Sur       | 15%                   |
| Nota entre 4.0 y 5.0   | Zona Centro    | 10%                   |

Además:
- Todos los empleados de **Zona Norte** obtienen automáticamente un **12% de descuento**.
- Si son de **Zona Norte** y tienen nota **mayor o igual a 5.5**, obtienen un **5% adicional**.

## El programa debe:

1. Solicitar al usuario su **nota de ingreso** y **zona de origen**.
2. Calcular el **descuento total**.
3. Mostrar el **valor del bono final**, el **descuento aplicado**, y un **mensaje con los beneficios obtenidos**.

---

## Código en Python

```python
nota = float(input("Ingrese su nota de ingreso (1.0 a 7.0): "))
zona = input("Ingrese su zona de origen (Norte, Centro o Sur): ").lower()

bono_base = 2500000
descuento = 0

if zona == "norte":
    descuento = 12
    if nota >= 5.5:
        descuento += 5
elif zona == "centro":
    if nota > 6.0:
        descuento = 20
    elif 4.0 <= nota <= 5.0:
        descuento = 10
elif zona == "sur":
    if nota > 6.0:
        descuento = 25
    elif 5.0 <= nota <= 6.0:
        descuento = 15

monto_descuento = bono_base * (descuento / 100)
bono_final = bono_base - monto_descuento

print("Descuento aplicado:", descuento, "%")
print("Monto final del bono: ${:,.0f}".format(bono_final))
print("¡Beneficio procesado con éxito!")
```

---

¡Recuerda verificar los rangos de nota y escribir correctamente la zona!
