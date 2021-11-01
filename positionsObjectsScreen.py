from positionOnScreen import findClickPositions


# Tela do round
def positionButtonBack():
    # Retorna a posição do button "volta", que fica na tela do mapa.
    positionBack = findClickPositions('images/volta.jpg', 'screenShot.jpg', threshold=0.8, debug_mode='points')

    return positionBack[0]


# Tela do round
def sleepingQuantity():
    qtdSleeping = len(findClickPositions('images/sono2.jpg', 'screenShot.jpg', debug_mode='points'))

    return qtdSleeping


# Tela round
def positionTextNewMap():
    positionNewMap = findClickPositions('images/newMap.jpg', 'screenShot.jpg', debug_mode='points')

    return positionNewMap[0]


# Tela home
def positionButtonHeroes():
    # Retorna a posição do button "Heroes" da tela inicial.
    positionHeroes = findClickPositions('images/boneco.jpg', 'screenShot.jpg', debug_mode='points')

    return positionHeroes[0]


# Tela home
def positionButtonHunt():
    # Retorna a posição do button "Treasure Hunt" da tela inicial.
    positionHunt = findClickPositions('images/bauOuro.jpg', 'screenShot.jpg', debug_mode='points')

    return positionHunt[0]


# ---------------------------------------Função desativada-------------------------------------
"""
# Tela personagens
def positionTipoBoneco():
    # Retorna a última posição onde está escrito "common".
    positionTextCommon = findClickPositions('images/tipoboneco.jpg', 'screenShot.jpg', debug_mode='points')
    return positionTextCommon[-1] 
"""
# ----------------------------------------------------------------------------------------------

# Tela personagens
def positionButtonClose():
    # Retorna a posição do botão "close".
    positionClose = findClickPositions('images/close.jpg', 'screenShot.jpg', debug_mode='points')

    return positionClose[0]


# Tela round
def positionErroUnknown():
    # Retorna a posição da palavra "Unknown".
    positionErro = findClickPositions('images/okErro.jpg', 'screenShot.jpg', debug_mode='points')

    return positionErro[0]


# Tela round
def positionOkErro():
    # Retorna a posição do botão "Ok".
    positionErro = findClickPositions('images/unknown.jpg', 'screenShot.jpg', debug_mode='points')

    return positionErro[0]


# Tela de login
def positionConnectWallet():
    positionConnect = findClickPositions('images/loginConnect.jpg', 'screenShot.jpg', debug_mode='points')

    return positionConnect[0]


# Tela de login
def positionSelectWallet():
    positionWallet = findClickPositions('images/metaMask.jpg', 'screenShot.jpg', debug_mode='points')

    return positionWallet[0]


# Tela de login
def positionConfirmSign():
    positionSign = findClickPositions('images/signLogin.jpg', 'screenShot.jpg', debug_mode='points')

    return positionSign[0]


# Tela personagens
def positionButtonWork():
    # Retorna a última posição onde está escrito "Work".
    positionWork = findClickPositions('images/work.jpg', 'screenShot.jpg', threshold=0.8, debug_mode='points')

    return positionWork[-1]


# Tela personagens
def positionTipoBonecoSuperRaroLegend():
    try:
        positionSuperRaro = findClickPositions('images/superaro.jpg', 'screenShot.jpg', threshold=0.8,
                                               debug_mode='points')

        positionLegend = findClickPositions('images/legend.jpg', 'screenShot.jpg', threshold=0.8, debug_mode='points')

        positionSuperRaro.append(positionLegend[-1])

        return positionSuperRaro
    except IndexError:
        try:
            positionLegend = findClickPositions('images/legend.jpg', 'screenShot.jpg', threshold=0.8, debug_mode='points')

            return positionLegend[-1]
        except IndexError:
            positionSuperRaro = findClickPositions('images/superaro.jpg', 'screenShot.jpg', threshold=0.8, debug_mode='points')

            return positionSuperRaro[-1]


# Qualquer tela.
def positionErroOverloaded():
    # Retorna a posição da palavra "Unknown".
    positionErro = findClickPositions('images/overloaded.jpg', 'screenShot.jpg', debug_mode='points')

    return positionErro[0]
