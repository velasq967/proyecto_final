import json
import os
TXT_PATH = "letter_soup_example.txt"

def main():
    """
    Primera funcion en ejecutarse y ejecuta las demás
    Parametros: 
    Ninguno
    """
    try:
        matrix_soup, words = comprehend_letter_soup(TXT_PATH)

        check_word(matrix_soup, words)

        give_report_path(generate_report(matrix_soup, words))

    except FileNotFoundError:
        print("No se ha encontrado el archivo de la sopa de letras")
    
    except IndexError:
        print("El formato del archivo de texto no es legible (incorrecto)")

def comprehend_letter_soup(txt_input):
    """
    Esta funcion separará la sopa de letras de las posibles palabras
    a buscar
    
    Parametros:
    txt_input = el archivo de texto dado por el usuario
    donde se encuentra la sopa de letras

    Retorna:
    la sopa de letras
    la lista de palabras a buscar
    """
    with open(txt_input) as txt_file:
        txt_content = txt_file.read().strip().split('---')
        
        # Procesar la sopa de letras
        txt_lines = txt_content[0].strip().split('\n')
        matrix_soup = [list(line.strip().split()) for line in txt_lines]
        
        # Procesar las palabras
        words = txt_content[1].strip().split('\n')
        
    return matrix_soup, words

def check_word(letter_soup, word):
    """
    Esta funcion va a buscar las palabras en la sopa de letras
    Parametros:
    letter_soup = la matriz de la sopa de letras
    word = la palabra que va a buscar en la sopa de letras
    """
    rows, columns = len(letter_soup), len(letter_soup[0])
    word_len = len(word)
    word_checked = False
    DIRECTIONS = [ #posibles direcciones a 
                    #las que puede dirigirse una palabra, donde:
                    #el primer objeto de la tupla es la cordenada X y el segundo Y
                  (1, 0), 
                  (-1, 0), 
                  (0, 1), 
                  (0, -1),
                  (1, 1),
                  (1, -1),
                  (-1, -1),
                  (-1, 1),
                  ]

    def find_word_direction(x, y, direction_x, direction_y):
        """
        Esta funcion es para verificar que una palabra este hacia una direccion dada
        Parametros:
        x: la fila en la que se inicia a verificar
        y: la columna en la que se inicia a verificar
        direction_x: la direccion en el eje x (filas) que va a tomar, diagonal o horizontal 
        direction_y: la direccion en el eje y (columnas) que va a tomar, diagonal o vertical
        """
        letter_is_present = True
        for i in range(word_len):
            new_x = x + i * direction_x
            new_y = y + i * direction_y
            if not (0 <= new_x < rows and 0 <= new_y < columns) or letter_soup[new_x][new_y] != word[i]:
                letter_is_present = False
                #not (0 <= new_x < rows and 0 <= new_y < columns) es para verificar que los valores nuevos no esten fuera de rango
        return letter_is_present

    for x in range(rows):
        for y in range(columns):
            for direction_x, direction_y in DIRECTIONS:
                if find_word_direction(x, y, direction_x, direction_y):
                    word_checked = True
    
    return word_checked

def check_word_list(letter_soup, words_list):
    """
    Funcion que verifica que una lista de palabras esté en la sopa de letras
    Parametros:
    letter_soup: la matriz de la sopa de letras
    words_list: la lista de palabras que va a evaluar
    """
    words_checked = 0
    for word in words_list:
        if check_word(letter_soup, word):
            words_checked += 1
    if words_checked == len(words_list):
        print("Todas las palabras están en la sopa de letras")
        all_words_in_list = True
    else:
        print("Una o más palabras no están en la sopa de letras")
        all_words_in_list = False
    return all_words_in_list



def generate_report(letter_soup, words):
    """
    Esta funcion genera el archivo reporte JSON de las palabras encontradas y
    no encontradas que se entregará al usuario
    Parametros:
    letter_soup: matriz de la sopa de letras, para ejecutar la funcion check_word
    words: lista de palabras para agregarlas al archivo reporte
    """ 
    result = {}
    for word in words:
        result[word] = check_word(letter_soup, word)
    json_path = "words_report.json"
    with open(json_path, "w") as json_file:
        json.dump(result, json_file, indent = 4)

    
    return json_path

def give_report_path(json_path):
    """
    Esta funcion define el directorio absoluto en el cual se encuentra el archivo reporte 
    para entregarlo al usuario
    Parametros:
    json_path: directorio base en el cual se encuentra el archivo reporte
    """
    json_abspath = os.path.abspath(json_path)
    print("El archivo con el reporte de las palabras se encuentra en:", json_abspath)

if __name__ == "__main__":
    main()