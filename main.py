import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["açucena",	"advogado",	"afta", "alambique", "alcachofra", "algarismo", "almanaque", "almofariz", "almoxarife", "alquimia",	"altivez",	"alvíssaras",
"amendoim",	"amnésia",	"amplificar","ampulheta",	"ansioso",	"aplaudir","ascensão",	"asterisco",	"atlas",
"balacobaco",	"bandolim",	"barulhento","basquetebol",	"batráquio",	"beneficente","berimbau",	"bicarbonato",	"brusquidão",
"bugiganga",	"bumerangue",	"burocracia","caatinga",	"caboclo",	"cacareco","cacto",	"cadarço",	"cãibra","calibrado",	"camuflagem",	"candelabro",
"cassetete",	"catalisador",	"catequizar","cérebro",	"chamariz",	"cicatriz",
"cleptomaníaco",	"coincidência",	"companhia","condescender",	"consciente",	"crepúsculo",
"cronologia",	"deglutir",	"depredar","destruído",	"diapasão",	"digladiar",
"diretriz",	"dobradiça",	"ecossistema","embaixador",	"empecilho",	"entretido",
"entrevista",	"envernizar",	"enxaqueca","enxerido",	"escangalhado",	"escaravelho",
"escombro",	"esculacho",	"esfirra","espinafre",	"esplendor",	"estapafúrdio",
"estetoscópio",	"exceção",	"excêntrico","excepcional",	"faniquito",	"fascículo",
"flexível",	"frustrado",	"gargantilha","glândula",	"glicerina",	"glorioso",
"gnomo",	"grampeador",	"hamster","helicóptero",	"hemisfério",	"herdeiro",
"hermético",	"hierárquico",	"hieróglifo","hipocrisia",	"humanizar",	"idolatrada","imbróglio	inexorável",	"inflamado",
"influência	insignificância",	"interruptor","invertebrado	iogurte",	"irascível","lantejoula	licenciado",	"losango",
"madrasta",	"magnético",	"manteigueira","marimbondo",	"mesclar",	"meteorologia",
"mexerico",	"micróbio",	"microfone","microscópio",	"milionário",	"mordaz",
"nebulizador",	"oscilação",	"paralisado","pedágio",	"pernóstico",	"perturbar",
"piripaque",	"plissado",	"pneumático","pneumonia",	"poliomielite",	"potiguar","prescindir",	"presságio",	"privilégio",
"prodígio",	"prostração",	"prurido","psicanálise",	"psicólogo",	"quadriciclo",
"quádruplo",	"quinquilharia",	"reciclar","reflorescer",	"reivindicar",	"rescindir",
"retrógrado",	"retrovisor",	"ritmo","seborreia",	"sensatez", "serelepe",
"serpentina",	"simplório",	"simulacro","sincrônico",	"sobrevivente",	"subsídio","supérfluo",	"suscetível",	"termômetro",
"torácico",	"travesseiro",	"trilogia","universidade",	"vangloriar", "vaporizador",
"ventilador",	"xilindró",	"ziguezague","ziquizira",	"zodíaco",	"zumbido"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False     
lives = 6

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("escolha uma letra: ").lower()

    if guess in display:
        print(f"você já escolheu {guess}")

    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    
    if guess not in chosen_word:
        print(f"Você escolheu: {guess}, esta não está na palavra. você perdeu uma vida.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Você Perdeu.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("Você Ganhou.")

    print(stages[lives])