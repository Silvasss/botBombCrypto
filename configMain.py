import main


# Ativar função "Home", True ou Falso.
home = False

# Tempo para carregar a energia dos bonecos. Só número
minutosBonecos = 60

# Tempo para a função "Home" ativar.
# Tempo que o código vai esperar os bonecos "SuperRaros" e "Legend" cansarem, para mandar eles para casa.
minutosCasaBonecos = 20

# Tempo de pausa, entre cada verificação da hora.
# Valor em SEGUNDOS.
timeSleep = 180

# Função segunda tela.
secondScreen = True


if __name__ == '__main__':
    main.main(home, minutosBonecos, minutosCasaBonecos, timeSleep, secondScreen)
