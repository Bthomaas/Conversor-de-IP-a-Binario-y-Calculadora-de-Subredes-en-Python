#   ENTRADA
octeto1 = int(input("Introduzca el primer octeto de la IP: "))
#   PROCESO - Conversion manual a binario
bit1 = octeto1 % 2
bit2 = (octeto1 // 2) % 2
bit3 = (octeto1 // 4) % 2
bit4 = (octeto1 // 8) % 2
bit5 = (octeto1 // 16) % 2
bit6 = (octeto1 // 32) % 2
bit7 = (octeto1 // 64) % 2
bit8 = (octeto1 // 128) % 2
#   Guardar en una variable como string
binario1 = (str(bit8) + str(bit7) + str(bit6) + str(bit5) + str(bit4) + str(bit3) + str(bit2) + str(bit1))
#   SALIDA - Los bits deben ir de mayor a menor peso (bit8 ... bit1) porque sino queda dada vuelta la operacion
print("El número en binario es:", bit8, bit7, bit6, bit5, bit4, bit3, bit2, bit1)

octeto2 = int(input("Introduzca el segundo octeto de la IP: "))
# PROCESO - Conversion manual a binario
bit1 = octeto2 % 2
bit2 = (octeto2 // 2) % 2
bit3 = (octeto2 // 4) % 2
bit4 = (octeto2 // 8) % 2
bit5 = (octeto2 // 16) % 2
bit6 = (octeto2 // 32) % 2
bit7 = (octeto2 // 64) % 2
bit8 = (octeto2 // 128) % 2
#   Guardar en una variable como string
binario2 = (str(bit8) + str(bit7) + str(bit6) + str(bit5) + str(bit4) + str(bit3) + str(bit2) + str(bit1))
#   SALIDA - Los bits deben ir de mayor a menor peso (bit8 ... bit1) porque sino queda dada vuelta la operacion
print("El número en binario es:", bit8, bit7, bit6, bit5, bit4, bit3, bit2, bit1)

octeto3 = int(input("Introduzca el tercer octeto de la IP: "))
#   PROCESO - Conversion manual a binario
bit1 = octeto3 % 2
bit2 = (octeto3 // 2) % 2
bit3 = (octeto3 // 4) % 2
bit4 = (octeto3 // 8) % 2
bit5 = (octeto3 // 16) % 2
bit6 = (octeto3 // 32) % 2
bit7 = (octeto3 // 64) % 2
bit8 = (octeto3 // 128) % 2
#   Guardar en una variable como string
binario3 = (str(bit8) + str(bit7) + str(bit6) + str(bit5) + str(bit4) + str(bit3) + str(bit2) + str(bit1))
#   SALIDA - Los bits deben ir de mayor a menor peso (bit8 ... bit1) porque sino queda dada vuelta la operacion
print("El número en binario es:", bit8, bit7, bit6, bit5, bit4, bit3, bit2, bit1)

octeto4 = int(input("Introduzca el cuarto octeto de la IP: "))
#   PROCESO - Conversion manual a binario
bit1 = octeto4 % 2
bit2 = (octeto4 // 2) % 2
bit3 = (octeto4 // 4) % 2
bit4 = (octeto4 // 8) % 2
bit5 = (octeto4 // 16) % 2
bit6 = (octeto4 // 32) % 2
bit7 = (octeto4 // 64) % 2
bit8 = (octeto4 // 128) % 2
#   Guardar en una variable como string
binario4 = (str(bit8) + str(bit7) + str(bit6) + str(bit5) + str(bit4) + str(bit3) + str(bit2) + str(bit1))
#   SALIDA - Los bits deben ir de mayor a menor peso (bit8 ... bit1) porque sino queda dada vuelta la operacion
print("El número en binario es:", bit8, bit7, bit6, bit5, bit4, bit3, bit2, bit1)

#CON .
print("Tu direccion IP es: ",octeto1,".",octeto2,".",octeto3,".",octeto4)
print("Tu direccion IP en Binario es: ",binario1,".",binario2,".",binario3,".",binario4)

#   Ahora con CIDR
cidr = int(input("Introdusca tu CIDR: "))
if cidr > 24:
    print("la ip es tipo C")
elif cidr < 24 and cidr > 16:
    print("La ip es de tipo B")
elif cidr < 16 and cidr >= 8:
    print("La ip es de tipo A")

#   Cuantas Subredes
TipoSubRed = input("Ingrese el tipo de IP (A, B, C): ")
if TipoSubRed == "C":
    diferencia = cidr - 24
    NumSubRed = 2 ** diferencia
elif TipoSubRed == "B":
    diferencia = cidr - 16
    NumSubRed = 2 ** diferencia
elif TipoSubRed == "A":
    diferencia = cidr - 8
    NumSubRed = 2 ** diferencia
print("El numero de subredes es: ", NumSubRed)

#    Hosts por Subred
if TipoSubRed == "C":
    diferencia = 32 - cidr
    NumHost = (2 ** diferencia) - 2
elif TipoSubRed == "B":
    diferencia = 32 - cidr
    NumHost = (2 ** diferencia) - 2
elif TipoSubRed == "A":
    diferencia = 32 - cidr
    NumHost = (2 ** diferencia) - 2
print("El numero de Hosts por Subred es: ", NumHost)

#    Rango de Hosts
if TipoSubRed == "C":
    diferencia = 32 - cidr
    RangoHost = 2 ** diferencia
elif TipoSubRed == "B":
    diferencia = 32 - cidr
    RangoHost = 2 ** diferencia
elif TipoSubRed == "A":
    diferencia = 32 - cidr
    RangoHost = 2 ** diferencia
print("El Rango de Hosts es: ", RangoHost)
print("El Rango de Hosts disponible es: 0 -", RangoHost - 1)

#    Rango loopback
if TipoSubRed == "C":
    diferencia = 32 - cidr
    RangoLoopback = 2 ** diferencia
elif TipoSubRed == "B":
    diferencia = 32 - cidr
    RangoLoopback = 2 ** diferencia
elif TipoSubRed == "A":
    diferencia = 32 - cidr
    RangoLoopback = 2 ** diferencia
print("El Rango de Loopback es: ", RangoLoopback)
print("El Rango de Loopback disponible es: 128 -", RangoLoopback + 127)

#    Rango broadcast
if TipoSubRed == "C":
    diferencia = 32 - cidr
    RangoBroadcast = 2 ** diferencia
elif TipoSubRed == "B":
    diferencia = 32 - cidr
    RangoBroadcast = 2 ** diferencia
elif TipoSubRed == "A":
    diferencia = 32 - cidr
    RangoBroadcast = 2 ** diferencia
print("El Rango de Broadcast es: ", RangoBroadcast)
print("El Rango de Broadcast disponible es: ", RangoBroadcast - 1)

#    Rango APIPA
if TipoSubRed == "C":
    diferencia = 32 - cidr
    RangoAPIPA = 2 ** diferencia
elif TipoSubRed == "B":
    diferencia = 32 - cidr
    RangoAPIPA = 2 ** diferencia
elif TipoSubRed == "A":
    diferencia = 32 - cidr
    RangoAPIPA = 2 ** diferencia
print("El Rango de APIPA es: ", RangoAPIPA)
print("El Rango de APIPA disponible es: ", RangoAPIPA + 169)
print("El Rango de APIPA disponible es: ", RangoAPIPA + 254)
print("El Rango de APIPA disponible es: 254 -", RangoAPIPA + 255)