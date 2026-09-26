import string


print("""
=================================
        TEXT ANALYZER
=================================
""")

# 0. ----------------------------------------------------------------------------------

#ingresa el texto del ususario
text = input("Enter your text: \n")

#evita que el usuario ingrese un texto completamente vacio ""
if text == "":
    text = " "

text_with_words = False

#Elimina los cracteres especiales del texto, tambien los numeros 
text_without_characters =  text
for c in range(len(text)):
    if text[c] in string.punctuation or text[c].isalpha() == False:
        if c != len(text) - 1:
            text_without_characters = text_without_characters[:c] + " " + text_without_characters[c+1:] 
        else:
            text_without_characters = text_without_characters[:c] 
    else:
        # verifica que alla letras en el texto, no solamente espacion
        text_with_words = True

    word_list = text_without_characters.lower().split()

#permite que se analize el texto si es True es porque anteriormente se probo que si habian letras
#si es false no hay letras, por ende no se ejecuta el analisis

if text_with_words:

#1. ----------------------------------------------------------------------------------

    #como queremos saber cuantas palabras hay ponemos cada palabra en una lista y contamos los
    #elementos de la lista
    words = len(word_list)

    #contamos cuantas palabras aparecen solo una vez en todo el texto
    words_appearing_once = 0
    
    word_counts = {}
    for c in word_list:
        word_counts[c] = word_counts.get(c, 0) + 1

    for j in word_counts:
        if word_counts[j] == 1:
            words_appearing_once += 1

#2. ----------------------------------------------------------------------------------

    # esta funcion cuenta cuanto de algo hay en el text
    # amount = cantidad que quiere que se sume  #group = de que grupo quiere que se busque
    def count_characters(amount, group):
        result = sum( amount for c in text if c in group)
        return result

    # se utilizo la funcion para contar los characteres especiales
    special_characters = count_characters(1, string.punctuation)

    #aqui se uso para la cantidad de oraciones, el codigo esta pensado para texto en ingles
    #por eso se obvian signos de apertura que existen en el español 
    sentences = count_characters(1, "?!.")

#3. ----------------------------------------------------------------------------------

    # aqui nos aseguramos que las palabras del texto que envio el usuario no se repitan
    #esto evita que si hay 2 veces tipeadas la palabra "excelente" se coloquen en la lista juntas
    # pues solo puede haber una. Utíl para que las palabras en el ranking no se repitan
    list_longest_words = list(set(word_list))

    # Aquí se ordenan las palabras de la más larga a la más corta
    list_longest_words = sorted(list_longest_words, key=len, reverse=True)



# 4. ----------------------------------------------------------------------------------
  
    #Aqui se saca del diccionario word_counter la frecuencia de las palabras (revisar seccion 1.) 
    #y se las ordena de mayor a menor
    list_most_frequent_words = sorted(word_counts.keys(), key=lambda c: word_counts[c], reverse=True)


# 5. ----------------------------------------------------------------------------------

    #Con todos los datos obtenidos se imprimen los resultados en la consola

    print(f"""

    Text analized: {words} words

    ESTADISTICS
    -----------------------

    Total words: {words}
    Words appearing once: {words_appearing_once}
    Special Characters: {special_characters}
    Sentences: {sentences}
    Average words per sentence: {float(words/sentences) if sentences >= 1 else  print("Invalid division") if None else ""}


    WORDS
    -----------------------

    Most frequent word: {list_most_frequent_words[0]}
    Appeareances: {word_counts[list_most_frequent_words[0]]}

    Longest word: {list_longest_words[0]}
    length: {len(list_longest_words[0])}

    Shortest word: {list_longest_words[-1]}
    length: {len(list_longest_words[-1])}

    TOP 5 LONGEST WORDS
    -----------------------
    1. {list_longest_words[0]}
    2. {list_longest_words[1] if len(list_longest_words) > 1 else "There are not enough words"}
    3. {list_longest_words[2] if len(list_longest_words) > 2 else "There are not enough words"}
    4. {list_longest_words[3] if len(list_longest_words) > 3 else "There are not enough words"}
    5. {list_longest_words[4] if len(list_longest_words) > 4 else "There are not enough words"}

    TOP 5 MOST COMMON WORDS
    -----------------------
    1. {list_most_frequent_words[0]}
    2. {list_most_frequent_words[1] if len(list_most_frequent_words) > 1 else "There are not enough words"}
    3. {list_most_frequent_words[2] if len(list_most_frequent_words) > 2 else "There are not enough words"}
    4. {list_most_frequent_words[3] if len(list_most_frequent_words) > 3 else "There are not enough words"}
    5. {list_most_frequent_words[4] if len(list_most_frequent_words) > 4 else "There are not enough words"}
    """)

else:
    print("The text lacks words")

