# Conversor-de-IP-a-Binario-y-Calculadora-de-Subredes-en-Python
Este proyecto es un programa en Python que permite trabajar de forma manual con direcciones IP y conceptos básicos de redes. Su objetivo principal es convertir una dirección IP decimal a su equivalente binario y realizar cálculos de subredes utilizando operaciones matemáticas simples, sin depender de librerías externas.

# 🧠 Conversor de IP a Binario y Calculadora de Subredes en Python

## 📌 Descripción
Este proyecto es un programa interactivo en **Python** que permite trabajar manualmente con direcciones IP y conceptos básicos de redes.  
Convierte direcciones IP a su representación binaria y realiza cálculos de subred sin depender de librerías externas.  
Fue desarrollado como ejercicio educativo para reforzar conocimientos de **redes y lógica de programación**.

---

## 🧭 Características principales

- ✅ Conversión manual de cada octeto de la IP a binario (bit a bit).  
- 🧮 Determinación de clase de IP (A, B o C) según el valor CIDR ingresado.  
- 🌐 Cálculo de:
  - Número de subredes  
  - Número de hosts por subred  
  - Rango de hosts disponibles  
  - Rangos para loopback, broadcast y APIPA  
- 💻 Totalmente interactivo: el programa solicita datos por consola y muestra los resultados en tiempo real.

---

## 🧰 Tecnologías utilizadas

- Lenguaje: **Python 3**  
- Librerías: No utiliza librerías externas, solo funciones básicas de Python.  
- Ejecución: Línea de comandos / terminal.

---

## 🚀 Ejemplo de uso

```bash
Introduzca el primer octeto de la IP: 192
Introduzca el segundo octeto de la IP: 168
Introduzca el tercer octeto de la IP: 1
Introduzca el cuarto octeto de la IP: 5

El número en binario es: 1 1 0 0 0 0 0 0
...
Tu direccion IP en Binario es: 11000000.10101000.00000001.00000101

Introdusca tu CIDR: 26
la ip es tipo C
Ingrese el tipo de IP (A, B, C): C
El numero de subredes es:  4
El numero de Hosts por Subred es:  62
El Rango de Hosts es:  64
...
