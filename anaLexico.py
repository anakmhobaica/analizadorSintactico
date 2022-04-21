def tryNumber(n): #Comprobamos si el valor es un número
    try:
        value = int(n) 
        return "int"
    except ValueError:
        try:
            value = float(n)
            return "float"
        except ValueError:
            return "none"

def lexAnalyzer(code):
    print("\n\n--------------Analizador Léxico-------------- \n\n")
        
    tokens = [[",", "SEPARADOR"], [";", "FIN_LINEA"], ["(", "PARENTESIS_ABIERTO"], [")", "PARENTESIS_CERRADO"], 
    ["[", "CORCHETE_ABIERTO"], ["]", "CORCHETE_CERRADO"], ["print", "IMPRIMIR"], ['"', "COMILLA_DOBLE"], 
    ["'", "COMILLA_SIMPLE"], ["{", "LLAVE_ABIERTA"], ["}", "LLAVE_CERRADA"], ["=", "IGUAL_ASIG"], ["==", "IGUAL_COMP"], 
    ["!=", "DIFERENTE"], ["<", "MENOR_QUE"], [">", "MAYOR_QUE"], ["<=", "MENOR_IGUAL_A"], [">=", "MAYOR_IGUAL_A"], ["+", "SUMAR"], ["-", "RESTAR"], 
    ["*", "MULTIPLICAR"], ["/", "DIVIDIR"], ["int", "ENTERO"], ["string", "CADENA"], ["bool", "BOOLEANO"], ["float", "FLOTANTE"], 
    ["true", "BOOL_VERDADERO"], ["false", "BOOL_FALSO"], ["0", "CERO"], [".", "PUNTO"]] #Asignacion de Tokens
    
    espaciosArr= []

    saltosDeLineaArr = code.split('\n') #Separar el parametro que recibe la funncion en saltos de linea

    for idx, i in enumerate(saltosDeLineaArr):
        splitInChar = list(i)
        new_line = ""
        
        print("\nLINEA "+str(idx+1)+":\n")
        for x in splitInChar:
            if ord(x)<128:
                print(x+" ==> # ASCII: "+str(ord(x)))
                if (ord(x)>= 33 and ord(x)<= 47) or (ord(x)>= 58 and ord(x)<= 64) or (ord(x)>= 91 and ord(x)<= 96) or ord(x)>= 123 and ord(x)<= 126:
                    if ord(x) == 59:
                        new_line = new_line + " " + x
                    elif ord(x) == 46:
                        new_line = new_line + x
                    else:
                        new_line = new_line + " " + x + " "
                else:
                    new_line = new_line + x
            else:
                print("Error: "+x+" ==> elemento inválido en la línea "+ str(idx+1))
                exit()

        espaciosArr.append(new_line)

        final_list = []

        for i in espaciosArr:
            temp_line = []
            checkTokens = i.split()
            for x in checkTokens:
                for token in tokens:
                    tempchecker = False
                    if token[0]==x:
                        temp_line.append([x,token[1]])
                        tempchecker = True
                        break
                    else:
                        tempchecker = False

                if tempchecker == False:
                    checkx = tryNumber(x)
                    if checkx == "int":
                        temp_line.append([x, "ENTERO_VAL"])
                    elif checkx == "float":
                        temp_line.append([x, "FLOTANTE_VAL"])
                    else:
                        temp_line.append([x, "NOMBRE_VARIABLE"])
           
            final_list.append(temp_line)
    
    print("\n\nTokens en cada línea: \n")

    for count, line in enumerate(final_list):
        print('\n')
        print("LINEA "+str(count+1)+":")
        for token in line:
            print(token)
    return final_list

# with open('codigo.txt', 'r') as file:
#     codigo = file.read()

# lexAnalyzer(codigo)

# file.close()