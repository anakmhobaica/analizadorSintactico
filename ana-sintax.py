from anaLexico import lexAnalyzer

def syntaxdebug(code):
    print("\n\n--Analizador Sintáctico--\n\nSimplificar Arreglo de Tokens:\n")

    arreglo_simplicartokens = {"COMPARERS": ["MAYOR_QUE", "MENOR_QUE", "MAYOR_IGUAL_A", "MENOR_IGUAL_A", "IGUAL_COMP", 
    "DIFERENTE"], "VALUE":["ENTERO_VAL", "FLOTANTE_VAL", "BOOL_VERDADERO", "BOOL_FALSO", "CADENA_VAL", "CERO"], "TIPO_VAR": ["ENTERO", 
    "FLOTANTE", "CADENA", "BOOLEANO"], "MATH_SIMB": ["SUMAR", "RESTAR", "MULTIPLICAR", "DIVIDIR", "IGUAL_ASIG"]}

    arreglo_simplificado = []

    for idx, i in enumerate(code):
        temp_text=""
        checknumcommit = 0
        for j in i:
            if j[1] == 'COMILLA_DOBLE':
                checknumcommit+=1
        
        if checknumcommit>0:
            if checknumcommit % 2 ==0:
                for jdx, j in enumerate(i):
                    if j[1] == 'COMILLA_DOBLE': 
                        l=jdx+1
                        while(True):
                            if l < len(i):
                                if i[l+1][1] == 'COMILLA_DOBLE': 
                                    j[1] = "CADENA_VAL"
                                    j[0] = '"' + temp_text + i[l][0]+'"'
                                    i[l:l+2] = []
                                    # print(j)
                                    break
                                else:
                                    temp_text = temp_text + i[l][0] + " "
                                    i[l:l+1] = []
                                    l -= 1
                                l += 1
            else:
                print ("--Analizador Sintáctico--\n\nError Sintáctico en la línea "+str(idx+1)+": String mal declarado. Revisar comillas.")
                return False
    
    for i in code:
        arreglo_simplificado_temp = []
        for j in i:
            varchecker = False
            tempinfo = ""

            for key in arreglo_simplicartokens.keys():
                for x in arreglo_simplicartokens[key]:
                    if j[1] == x:
                        varchecker = True
                        tempinfo = key
                        break
            
            if varchecker == False:
                arreglo_simplificado_temp.append([j[0], j[1]])
            else:
                arreglo_simplificado_temp.append([j[0], tempinfo])
        
        arreglo_simplificado.append(arreglo_simplificado_temp)

    for idx, i in enumerate(arreglo_simplificado):
        temp_code = ""
        for jdx, j in enumerate(i):
            # print(j)
            temp_code = temp_code + j[0] + " "

            if jdx == 0:
                if not (j[1] == "TIPO_VAR" or j[1] == "NOMBRE_VARIABLE" or j[1] == "IMPRIMIR"):
                    print("Error en la linea: "+str(idx+1)+": Se esperaba un TIPO_VAR, NOMBRE_VARIABLE o IMPRIMIR al inicio")
                    return False
            else:
                if j[1] == "TIPO_VAR":
                    print(i[jdx-1][1])
                    if i[jdx-1][1] != "FIN_LINEA":
                        print ("Error en línea "+str(idx+1)+": Se esperaba un FIN_LINEA (;) antes de " + j[0])
                        return False
                elif j[1] == "NOMBRE_VARIABLE":
                    if not (i[jdx-1][1] == "TIPO_VAR" or i[jdx-1][1] == "SEPARADOR" or i[jdx-1][1] == "COMPARERS" or i[jdx-1][1] == "MATH_SIMB" or i[jdx-1][1] == "IMPRIMIR"):
                        print ("Error en línea "+str(idx+1)+": Se esperaba un TIPO_VAR (tipo de variable), o un SEPARADOR (,) o un operador matemático antes de "+j[1]+ " ("+ j[0]+")")
                        return False
                elif j[1] == "MATH_SIMB":
                    if not (i[jdx-1][1] == "NOMBRE_VARIABLE" or i[jdx-1][1] == "VALUE"):
                        print("Error en la linea "+str(idx+1)+": Se esperana un Nombre de Variable o un Valor antes de "+j[1]+ " (" + j[0]+")")
                        return False
                elif j[1] == "VALUE":
                    if not (i[jdx-1][1] == "MATH_SIMB" or i[jdx-1][1] == "COMPARERS" or i[jdx-1][1] == "IMPRIMIR"):
                        print ("Error en línea "+str(idx+1)+": Se esperaba un Operador Matemático antes de "+j[1]+ " ("+ j[0]+")")
                        return False
                elif j[1] == "FIN_LINEA":
                    if not (i[jdx-1][1] == "NOMBRE_VARIABLE" or i[jdx-1][1] == "VALUE"):
                        print ("Error en línea "+str(idx+1)+": Se esperaba un Nombre de Variable o un Valor antes de "+j[1]+ " ("+ j[0]+")")
                        return False
                elif j[1] == "SEPARATE":
                    if not (i[jdx-1][1] == "NOMBRE_VARIABLE" or i[jdx-1][1] == "VALUE"):
                        print ("Error en línea "+str(idx+1)+": Se esperaba un Nombre de Variable o un Valor antes de "+j[1]+ " ("+ j[0]+")")
                        return False
                elif j[1] == "COMPARERS":
                    if not (i[jdx-1][1] == "NOMBRE_VARIABLE" or i[jdx-1][1] == "VALUE"):
                        print ("Error en línea "+str(idx+1)+": Se esperaba un Nombre de Variable o un Valor antes de "+j[1]+ " ("+ j[0]+")")
                        return False

        print("\nLinea "+ str(idx+1)+ " ( "+temp_code+"): OK.")
        temp_text = ""

        for jdx,j in enumerate(i):
            print("\n     "+j[1])

    print("\nAnalisis Lexico Terminado")

with open('codigo.txt', 'r') as file:
    codigo = file.read()

syntaxdebug(lexAnalyzer(codigo))

file.close()



# syntaxdebug([[['string', 'CADENA'], ['a', 'NOMBRE_VARIABLE'], ['=', 'IGUAL_ASIG'], ['"', 'COMILLA_DOBLE'], ['hola', 'NOMBRE_VARIABLE'], ['mundo', 'NOMBRE_VARIABLE'], ['"', 'COMILLA_DOBLE'], [';', 'FIN_LINEA']], [['int', 'ENTERO'], ['a', 'NOMBRE_VARIABLE'], ['=', 'IGUAL_ASIG'], ['0', 'CERO'], [';', 'FIN_LINEA']], [['float', 'FLOTANTE'], ['b', 'NOMBRE_VARIABLE'], ['=', 'IGUAL_ASIG'], ['5.6', 'FLOTANTE_VAL'], [';', 'FIN_LINEA']], [['float', 'FLOTANTE'], ['c', 'NOMBRE_VARIABLE'], ['=', 'IGUAL_ASIG'], ['a', 'NOMBRE_VARIABLE'], ['+', 'SUMAR'], ['b', 'NOMBRE_VARIABLE'], [';', 'FIN_LINEA']], [['int', 'ENTERO'], ['d', 'NOMBRE_VARIABLE'], ['=', 'IGUAL_ASIG'], ['a', 'NOMBRE_VARIABLE'], ['*', 'MULTIPLICAR'], ['3', 'ENTERO_VAL'], [';', 'FIN_LINEA']], [['bool', 'BOOLEANO'], ['e', 'NOMBRE_VARIABLE'], ['=', 'IGUAL_ASIG'], ['true', 'BOOL_VERDADERO'], [';', 'FIN_LINEA']], [['bool', 'BOOLEANO'], ['f', 'NOMBRE_VARIABLE'], ['=', 'IGUAL_ASIG'], ['b', 'NOMBRE_VARIABLE'], ['<', 'MENOR_QUE'], ['a', 'NOMBRE_VARIABLE'], [';', 'FIN_LINEA']], [['float', 'FLOTANTE'], ['g', 'NOMBRE_VARIABLE'], ['=', 'IGUAL_ASIG'], ['b', 'NOMBRE_VARIABLE'], ['/', 'DIVIDIR'], ['c', 'NOMBRE_VARIABLE'], [';', 'FIN_LINEA']]])