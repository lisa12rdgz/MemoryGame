from random import *
from turtle import *
from freegames import path

car = path('car.gif')
#tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
tiles = ["\U0001f947","\U0001f384","\U0001f250","\u264e",
"\U0001f936","\U0001f197","\U0001f17e\ufe0f","\U0001f17f\ufe0f",
"\U0001f17f\ufe0f","\U0001f198","\U0001f385","\U0001f3f4\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f",
"\U0001f5fd","\U0001f996","\U0001f5fc","\U0001f199",
"\U0001f19a","\u264d","\U0001f9ee","\U0001fa79",
"\U0001f39f\ufe0f","\U0001f39f","\U0001f6a1","\u2708\ufe0f",
"\u23f0","\u2697\ufe0f","\U0001f47d","\U0001f47e",
"\U0001f691","\U0001f3c8","\U0001f3fa","\U0001f69b"] * 2

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

#Contadoress
contador = 0 
contador2=0

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    global contador
    global contador2

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        contador2+= 1 #Contador de parejas encontradas
    
    contador = contador+1 # Contador de taps
    print('Tap:', contador)

    if contador2==32: #Contador que determina cuando se encontraron todas las parejas // juego terminado
        print('JUEGO TERMINADO')

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 26, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'),align=("center"))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()