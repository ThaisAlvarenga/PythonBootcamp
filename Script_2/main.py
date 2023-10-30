"""
Name: Thais Alvarenga
Course: 100 Days of Python
Description:  Your Life Comic/Movie Name Generator
Date: 29/10/2023
"""
lang_mode = int(input("Press 1 for English. Presiona 2 para Español: "))

if lang_mode == 1:
    # English version
    user_name = input("Hey buddy! What is your name? ")
    print(f'Nice to meet you {user_name.capitalize()}')
    print('Life can be pretty tough sometimes.')
    print('And that can put us down.')
    print('However, without conflict, the plot of our lives would be pretty boring.')
    print('No character development; no interesting duels or moments of heroism...')
    print("")
    print('I surely hope you are not struggling too much right now.')
    print('But if you are, please tell someone.')
    print('Protagonists must learn to seek help when challenges are too big.')
    print('You can practice with me!')
    print('What is a current struggle you are going through?')
    challenge = input('Your struggle is: ')

    print("")
    print(f"Well, {user_name.capitalize()}, if your life was a movie or a comic book,")
    print("we could call it:")
    print("")
    print(f"{user_name.capitalize()} vs {challenge.capitalize()}")
    print("")
    print("Sounds like a pretty good story doesn't it?")
    print('Now go out there and be the protagonist of that story!')

elif lang_mode == 2:
    # Spanish version
    user_name = input("¡Hola! ¿Cuál es tu nombre? ")
    print(f'¡Encantado de conocerte, {user_name.capitalize()}!')
    print('La vida a veces puede ser bastante difícil.')
    print('Y eso puede desanimarnos.')
    print('Sin embargo, sin conflictos, la trama de nuestras vidas sería bastante aburrida.')
    print('Sin desarrollo de personaje, sin duelos interesantes ni momentos heroicos...')
    print("")
    print('Espero sinceramente que no estés teniendo demasiados problemas en este momento.')
    print('Pero si lo estás, por favor, cuéntaselo a alguien.')
    print('Los protagonistas deben aprender a buscar ayuda cuando los desafíos son demasiado grandes.')
    print('¡Puedes practicar conmigo!')
    print('¿Cuál es un desafío que estás enfrentando?')
    challenge = input('Tu desafío es: ')

    print("")
    print(f"Bien, {user_name.capitalize()}, si tu vida fuera una película o un cómic, podríamos llamarla:")
    print("")
    print(f"{user_name.capitalize()} vs {challenge.capitalize()}")
    print("")
    print("¡Suena como una buena historia! ¿verdad?")
    print('¡Ahora ve y conviértete en protagonist@ de esa historia!')

else:
    print("Invalid selection. Selección invalida.")
    print("Please start again. Por favor vuelva a empezar.")