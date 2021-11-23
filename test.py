import pyautogui
import time

import positionsObjectsScreen
import positionsObjectsScreen as objectsScreen
import clickScreen as click
from printScreen import printScreem
from playsound import playsound
playsound("sound/ClockSound.mp3")


def mouseDragCharacter():
    time.sleep(5)

    # Recebe a posição do cursor do mouse.
    x, y = pyautogui.position()

    pyautogui.click()

    # Movimento do scroll para baixo.
    pyautogui.scroll(-15000)

    # Tempo para terminar a animação
    time.sleep(2)

    # Move o mouse novamente para a posição inicial e clica no último personagem.
    pyautogui.click(x, y - 100, duration=2)

    time.sleep(2)

    # Posiciona o mouse em "Work".
    pyautogui.moveTo(x + 230, y, 2)

    return True


time.sleep(2)

# print(mouseDragCharacter())
"""

x, y = pyautogui.position()

pyautogui.moveTo(x - 50, y, 2)

pyautogui.move(x, y - 80, 2)

pyautogui.dragRel(0, +800, 2)

"""

# pyautogui.moveTo(891, 723)

# time.sleep(2)
"""
printScreem()

# Posição da palavra "Work".
workX, workY = objectsScreen.positionButtonWork()

# Move o mouse para o último boneco da primeira parte da lista.
click.moveMouse(workX - 240, workY + 10)

# Movimento de segurar e arrastar e posicionar o cursos em "work".
click.mouseDragCharacter()
# --------------------Último boneco-------------
time.sleep(2)

printScreem()

# Posição da palavra "SuperRaro" ou "Legend".
#tipoX, tipoY = objectsScreen.positionTipoBonecoSuperRaroLegend()
tipoX, tipoY = objectsScreen.positionButtonWork()

# Move o mouse para o nome do tipo do boneco.
click.moveMouse(tipoX, tipoY)

# Posiciona o cursos em "work".
click.moveMouse(tipoX + 230, tipoY)

# Clica no botão "work".
click.mouseLeftClick()

time.sleep(2)

tipoX, tipoY = pyautogui.position()

# Posiciona o cursos em "work".
click.moveMouse(tipoX + 230, tipoY)

# Clica no botão "work".
click.mouseLeftClick()

x, y = 847, 437

n = 0
while n < 2:
    # Posiciona o mouse no primeiro.
    click.moveMouse(x, y)

    # Clica para libera o movimento.
    click.mouseLeftClick()

    # Movimento de puxar para baixo.
    pyautogui.dragRel(0, 350, 2)

    n += 1

# Posiciona o mouse no primeiro.
click.moveMouse(x, y)

# Posiciona o mouse em "House".
pyautogui.moveTo(x + 160, y, 2)

# Clica em "House".
click.mouseLeftClick()
"""
"""
#time.sleep(3)

#x, y = pyautogui.position()
#click.moveMouse(x - 240, y + 15)

printScreem()

listaBonecosEspeciais = []

#listaBonecosEspeciais.append(objectsScreen.positionTipoBonecoSuperRaroLegend())

n = 0

#listaBonecosEspeciais = listaBonecosEspeciais[0]
 
#listaBonecosEspeciais.pop(2)
"""
"""
# Que percorre a lista que contém as posições dos bonecos.
for i in listaBonecosEspeciais:
    for k in i:
        print("Valor de K: {}".format(k))
        if k:
            print("primeiro: {} {}".format(k[0], k[1]))

            # Posição da palavra "SuperRaro" ou "Legend".
            tipoX, tipoY = k[0], k[1]

            # Move o mouse para o nome do tipo do boneco.
            click.moveMouse(tipoX, tipoY)

            pyautogui.moveTo(tipoX + 230, tipoY)

            # Clica no botão "work".
            click.mouseLeftClick()

            time.sleep(2)

            n += 1

        if n > 2:

            printScreem()

            listaBonecosEspeciais = []

            listaBonecosEspeciais.append(objectsScreen.positionTipoBonecoSuperRaroLegend())

            #print(listaBonecosEspeciais[-1][-1])

            # Posição da palavra "SuperRaro" ou "Legend".
            tipoX, tipoY = listaBonecosEspeciais[-1][-1]

            # Move o mouse para o nome do tipo do boneco.
            click.moveMouse(tipoX, tipoY)

            pyautogui.moveTo(tipoX + 230, tipoY)

            # Clica no botão "work".
            click.mouseLeftClick()

            time.sleep(2)

            n += 1
"""
"""
# Que percorre a lista que contém as posições dos bonecos.
for i in listaBonecosEspeciais:
    if i:
        print("primeiro: {} {}".format(i[0], i[1]))

        # Posição da palavra "SuperRaro" ou "Legend".
        tipoX, tipoY = i[0], i[1]

        # Move o mouse para o nome do tipo do boneco.
        click.moveMouse(tipoX, tipoY)

        pyautogui.moveTo(tipoX + 230, tipoY)

        # Clica no botão "work".
        click.mouseLeftClick()

        time.sleep(2)

        n += 1

    if n > 1:

        #printScreem()

        listaBonecosEspeciais = [(659, 506)]

        #listaBonecosEspeciais.append(objectsScreen.positionTipoBonecoSuperRaroLegend())

        #print(listaBonecosEspeciais[-1][-1])

        # Posição da palavra "SuperRaro" ou "Legend".
        tipoX, tipoY = listaBonecosEspeciais[0]

        # Move o mouse para o nome do tipo do boneco.
        click.moveMouse(tipoX, tipoY)

        pyautogui.moveTo(tipoX + 230, tipoY)

        # Clica no botão "work".
        click.mouseLeftClick()

        time.sleep(2)

        n += 1
"""
"""
# Que percorre a lista que contém as posições dos bonecos.
for i in listaBonecosEspeciais:
    if i:
        print("primeiro: {} {}".format(i[0], i[1]))

        # Posição da palavra "SuperRaro" ou "Legend".
        tipoX, tipoY = i[0], i[1]

        # Move o mouse para o nome do tipo do boneco.
        click.moveMouse(tipoX, tipoY)

        pyautogui.moveTo(tipoX + 230, tipoY)

        # Clica no botão "work".
        click.mouseLeftClick()

        time.sleep(2)

        n += 1

    if n > 1:
        printScreem()

        listaBonecosEspeciais = []

        listaBonecosEspeciais.append(objectsScreen.positionTipoBonecoSuperRaroLegend())

        # Posição da palavra "SuperRaro" ou "Legend".
        tipoX, tipoY = listaBonecosEspeciais[0]

        # Move o mouse para o nome do tipo do boneco.
        click.moveMouse(tipoX, tipoY)

        pyautogui.moveTo(tipoX + 230, tipoY)

        # Clica no botão "work".
        click.mouseLeftClick()

        time.sleep(2)

        n += 1

        x, y = pyautogui.position()

        click.moveMouse(x - 100, y)

        pyautogui.dragRel(0, -y, 1)

        printScreem()

        listaBonecosEspeciais = []

        listaBonecosEspeciais.append(objectsScreen.positionTipoBonecoSuperRaroLegend())

        # Posição da palavra "SuperRaro" ou "Legend".
        tipoX, tipoY = listaBonecosEspeciais[0]

        # Move o mouse para o nome do tipo do boneco.
        click.moveMouse(tipoX, tipoY)

        pyautogui.moveTo(tipoX + 230, tipoY)

        # Clica no botão "work".
        click.mouseLeftClick()
"""
"""
printScreem()

listaBonecosEspeciais = []

listaBonecosEspeciais.append(objectsScreen.positionTipoBonecoSuperRaroLegend())

# Posição da palavra "SuperRaro" ou "Legend".
tipoX, tipoY = listaBonecosEspeciais[0]

# Move o mouse para o nome do tipo do boneco.
click.moveMouse(tipoX, tipoY)

pyautogui.moveTo(tipoX + 230, tipoY)

# Clica no botão "work".
click.mouseLeftClick()
"""
'''
# Função Base
def posicaoEspeciais(qtd1, qtd2):
    # Quantidade de bonecos na primeira parte da tela.
    QtdPriPart = qtd1

    # Quantidade de bonecos na segunda parte da tela.
    QtdSecPart = qtd2

    num = 0

    # Percorre a quantidade de bonecos que tem na primeira parte.
    while num < QtdPriPart:
        print(num)

        num += 1

    num = 0

    # Percorre a quantidade de bonecos que tem na segunda parte.
    while num < QtdSecPart:
        print(num)

        num += 1


#posicaoEspeciais(3, 1)
# ---------------------------------------------!#@¨%T#!@*#¨$¨&$)!@$¨)!@$&¨$&#$¨#@)-----------------------------
'''

listaBonecosEspeciais = [[(675, 434), (675, 722), (659, 506)]]

num = 0

# print(listaBonecosEspeciais[0][num][0])

while num < 4:
    num += 1
    pass


def posicaoEspeciais(qtd1, qtd2):
    exit()
    # Quantidade de bonecos na primeira parte da tela.
    QtdPriPart = qtd1

    # Quantidade de bonecos na segunda parte da tela.
    QtdSecPart = qtd2

    num = 0

    # Percorre a quantidade de bonecos que tem na primeira parte.
    while num < QtdPriPart:
        time.sleep(2)

        printScreem()

        # Lista que armazena a posição dos bonecos "SuperRaro" e "Legend".
        listaBonecosEspeciais = []

        try:
            # Posição das palavras "SuperRaro" ou "Legend".
            x2, x3 = objectsScreen.positionTipoBonecoSuperRaroLegend()

            try:
                print(x2[num])
                print("Encontrou ------------ SuperRaro ou Legend")
            except:
                print(x3[0])
                print("Encontrou ------------ SuperRaro ou Legend")
        except:
            print("Não encontrou ------------ SuperRaro ou Legend")
            return False
        '''
        if listaBonecosEspeciais[num]:
            # Posição da palavra "SuperRaro" ou "Legend".
            tipoX, tipoY = listaBonecosEspeciais[0][num][0], listaBonecosEspeciais[0][num][1]

            # Move o mouse para o nome do tipo do boneco.
            click.moveMouse(tipoX, tipoY)

            pyautogui.moveTo(tipoX + 230, tipoY)

            # Clica no botão "work".
            click.mouseLeftClick()

            time.sleep(2)
            '''

        num += 1

    """
    num = 0

    # Percorre a quantidade de bonecos que tem na segunda parte.
    while num < QtdSecPart:
        print(num)

        num += 1
    """


# posicaoEspeciais(3, 1)


def screenCharacterVersion2():
    # Utilizado no for.
    n = 0

    time.sleep(2)

    printScreem()

    # Lista que armazena a posição dos bonecos "SuperRaro" e "Legend".
    listaBonecosEspeciais = []

    if objectsScreen.positionTipoBonecoSuperRaroLegend():
        # Posição das palavras "SuperRaro" ou "Legend".
        listaBonecosEspeciais.append(objectsScreen.positionTipoBonecoSuperRaroLegend())

        # Pegando só a primeira lista
        listaBonecosEspeciais = listaBonecosEspeciais[0]

        # Retirando o terceiro item.
        listaBonecosEspeciais.pop(2)

        print("Encontrou ------------ SuperRaro ou Legend")
    else:
        print("Não encontrou ------------ SuperRaro ou Legend")
        return False

    # Que percorre a lista que contém as posições dos bonecos.
    for i in listaBonecosEspeciais:
        if i:
            # Posição da palavra "SuperRaro" ou "Legend".
            tipoX, tipoY = i[0], i[1]

            # Move o mouse para o nome do tipo do boneco.
            click.moveMouse(tipoX, tipoY)

            pyautogui.moveTo(tipoX + 230, tipoY)

            # Clica no botão "work".
            click.mouseLeftClick()

            time.sleep(2)

            n += 1

        if n > 1:
            printScreem()

            # Zera as posições da lista.
            listaBonecosEspeciais = []

            # Adicionado as posições dos bonecos.
            listaBonecosEspeciais.append(objectsScreen.positionTipoBonecoSuperRaroLegend())

            # Posição da palavra "SuperRaro" ou "Legend".
            tipoX, tipoY = listaBonecosEspeciais[0][-1]

            # Move o mouse para o nome do tipo do boneco.
            click.moveMouse(tipoX, tipoY)

            # Move o mouse para o botão "Work".
            pyautogui.moveTo(tipoX + 230, tipoY)

            # Clica no botão "work".
            click.mouseLeftClick()

            time.sleep(2)

            n += 1

            # Recebe a posição do cursor do mouse.
            x, y = pyautogui.position()

            # Move o curso para o lado do botão "Work".
            click.moveMouse(x - 100, y)

            # Movimento de arrastar para baixo.
            pyautogui.dragRel(0, -y, 1)

            time.sleep(2)

            printScreem()

            # Adicionado as posições dos bonecos.
            listaBonecosEspeciais = objectsScreen.positionTipoBonecoSuperRaroLegend()

            # Posição da palavra "SuperRaro" ou "Legend".
            tipoX, tipoY = listaBonecosEspeciais

            # Move o mouse para o nome do tipo do boneco.
            click.moveMouse(tipoX, tipoY)

            # Move o curso.
            pyautogui.moveTo(tipoX + 230, tipoY)

            # Clica no botão "work".
            click.mouseLeftClick()



