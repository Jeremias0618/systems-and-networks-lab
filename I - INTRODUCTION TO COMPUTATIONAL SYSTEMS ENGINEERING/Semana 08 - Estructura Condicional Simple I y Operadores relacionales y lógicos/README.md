# Semana 08 - Estructura Condicional Simple I y Operadores Relacionales y Lógicos

## Descripción General

Esta semana se introdujo el concepto fundamental de las **estructuras condicionales** en programación, específicamente las estructuras `if`, `elif` y `else` en Python. Se aprendieron los **operadores relacionales y lógicos** necesarios para crear condiciones efectivas que permitan al programa tomar decisiones basadas en diferentes escenarios.

## Objetivos de Aprendizaje

Al finalizar esta semana, el estudiante será capaz de:

1. **Comprender el concepto de programación condicional**
2. **Utilizar la estructura `if-else` básica**
3. **Implementar estructuras `if-elif-else` para múltiples condiciones**
4. **Aplicar operadores relacionales y lógicos correctamente**
5. **Resolver problemas prácticos usando estructuras condicionales**

## Conceptos Teóricos

### 1. Estructuras Condicionales

Las estructuras condicionales permiten que un programa ejecute diferentes bloques de código dependiendo de si una condición es verdadera o falsa.

#### Sintaxis Básica

```python
if condición:
    # Código a ejecutar si la condición es verdadera
    pass
else:
    # Código a ejecutar si la condición es falsa
    pass
```

#### Sintaxis con Múltiples Condiciones

```python
if condición1:
    # Código para condición1
    pass
elif condición2:
    # Código para condición2
    pass
elif condición3:
    # Código para condición3
    pass
else:
    # Código por defecto
    pass
```

### 2. Operadores Relacionales

Los operadores relacionales comparan dos valores y devuelven un valor booleano (`True` o `False`):

| Operador | Descripción | Ejemplo |
|----------|-------------|---------|
| `==` | Igual a | `5 == 5` → `True` |
| `!=` | Diferente de | `5 != 3` → `True` |
| `<` | Menor que | `3 < 5` → `True` |
| `>` | Mayor que | `5 > 3` → `True` |
| `<=` | Menor o igual que | `5 <= 5` → `True` |
| `>=` | Mayor o igual que | `5 >= 3` → `True` |

### 3. Operadores Lógicos

Los operadores lógicos combinan o modifican expresiones booleanas:

| Operador | Descripción | Ejemplo |
|----------|-------------|---------|
| `and` | Y lógico | `True and True` → `True` |
| `or` | O lógico | `True or False` → `True` |
| `not` | Negación lógica | `not True` → `False` |

### 4. Indentación en Python

Python utiliza la **indentación** (espacios o tabs) para definir bloques de código. Es fundamental mantener la consistencia en la indentación:

```python
if condición:
    print("Esta línea está indentada")
    print("Esta también")
else:
    print("Bloque else también indentado")
```

## Ejercicios Prácticos

### Ejercicio 1: Número Positivo o Negativo (`01_condicionales.py`)

**Objetivo:** Determinar si un número ingresado por el usuario es positivo o negativo.

**Conceptos aplicados:**
- Estructura `if-else` básica
- Operador relacional `>=`
- Entrada de datos con `input()`
- Conversión de tipos con `float()`

**Código:**
```python
number = float(input("Ingrese un numero: "))

if number >= 0:
    print(f"{number} es positivo")
else:
    print(f"{number} es negativo")
```

### Ejercicio 2: Sistema de Descuentos (`02_condicionales.py`)

**Objetivo:** Aplicar un descuento del 10% si el cliente gasta más de 100 soles.

**Conceptos aplicados:**
- Operador relacional `>`
- Cálculos matemáticos
- Formateo de números decimales
- Variables para almacenar resultados

**Problema detectado:** El código original tiene un error de indentación que impide el cálculo correcto del precio final.

### Ejercicio 3: Comparación de Números (`03_condicionales.py`)

**Objetivo:** Determinar cuál de dos números es mayor o si son iguales.

**Conceptos aplicados:**
- Estructura `if-elif-else`
- Múltiples condiciones
- Operadores relacionales `>` y comparación de igualdad

### Ejercicio 4: Clasificación por Edades (`04_condicionales.py`)

**Objetivo:** Clasificar a una persona según su edad en diferentes categorías.

**Conceptos aplicados:**
- Múltiples condiciones con `elif`
- Operadores relacionales combinados (`<=`)
- Ranges de valores

**Categorías:**
- Niño: 0-12 años
- Adolescente: 13-17 años
- Adulto: 18-59 años
- Adulto mayor: 60+ años

### Ejercicio 5: Tarifas de Consumo Eléctrico (`05_condicionales.py`)

**Objetivo:** Calcular el monto a pagar por consumo eléctrico según tarifas escalonadas.

**Conceptos aplicados:**
- Estructura `if-elif-else` completa
- Múltiples condiciones anidadas
- Cálculos complejos
- Salida formateada

**Tarifas:**
- < 100 kWh: S/ 0.80 por kWh
- 100-200 kWh: S/ 1.00 por kWh
- > 200 kWh: S/ 1.20 por kWh

## Versiones Alternativas

Se incluyen versiones alternativas (`_v2.py`) que muestran diferentes enfoques para resolver los mismos problemas:

- **02_condicionales_v2.py:** Corrige el error de indentación del ejercicio original
- **03_condicionales_v2.py:** Mejora los mensajes de salida
- **04_condicionales_V2.py:** Utiliza operadores lógicos (`and`) para las condiciones

## Errores Comunes y Mejores Prácticas

### Errores Frecuentes:

1. **Indentación incorrecta:** Python es sensible a la indentación
2. **Usar `=` en lugar de `==` para comparaciones**
3. **No considerar todos los casos posibles en las condiciones**
4. **Olvidar el `:` después de las declaraciones `if`, `elif`, `else`**

### Mejores Prácticas:

1. **Usar nombres de variables descriptivos**
2. **Comentar el código para explicar la lógica**
3. **Probar con diferentes valores de entrada**
4. **Validar datos de entrada cuando sea necesario**
5. **Mantener la consistencia en la indentación**

## Ejercicios de Práctica Adicional

Para reforzar los conceptos aprendidos, se recomienda practicar con:

1. **Calculadora de notas:** Determinar si un estudiante aprobó o reprobó
2. **Sistema de descuentos por categoría:** Aplicar diferentes descuentos según el tipo de cliente
3. **Clasificador de temperaturas:** Determinar si hace frío, calor o temperatura normal
4. **Validador de contraseñas:** Verificar si una contraseña cumple ciertos criterios
5. **Calculadora de IMC:** Clasificar el estado nutricional según el índice de masa corporal

## Recursos Adicionales

- [Documentación oficial de Python - Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Python Operators](https://www.w3schools.com/python/python_operators.asp)
- [Python If...Else](https://www.w3schools.com/python/python_conditions.asp)

## Conclusión

Las estructuras condicionales son fundamentales en la programación, ya que permiten crear programas que pueden tomar decisiones y adaptarse a diferentes situaciones. El dominio de estos conceptos es esencial para el desarrollo de algoritmos más complejos en las siguientes semanas del curso.

---

*Nota: Este material forma parte del curso de "Introducción a la Ingeniería de Sistemas Computacionales" y está diseñado para proporcionar una base sólida en programación estructurada.*
