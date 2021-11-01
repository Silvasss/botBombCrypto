import pyautogui
import execute, executeSuperRaroLegend
import clickScreen as click
from datetime import datetime, timedelta
import time


# Executar o script na tela do round.
def main(home, minutosBonecos, minutosCasaBonecos, timeSleep):

    def verifyTimeFuture():
        casa = home

        # Calculo da hora atual mais os minutos que a função recebe.
        # Tempo que o código vai esperar carregar a energia dos bonecos para chamar o próximo passo.
        timeFuture = datetime.now() + timedelta(minutes=minutosBonecos)
        # Formatando o hora futura
        future_time = timeFuture.strftime('%H:%M')

        # Calculo da hora atual mais os minutos que a função recebe.
        # Tempo que o código vai esperar os bonecos "SuperRaros" e "Legend" cansarem, para mandar eles para casa.
        timeFutureRaroLegend = datetime.now() + timedelta(minutes=minutosCasaBonecos)
        # Formatando o hora futura dos raros e lendas.
        futureRaroLegend_time = timeFuture.strftime('%H:%M')

        # While com loop eterno, com sleep de 3m.
        while True:
            # Recebe a hora atual.
            now = datetime.now()

            # Formatando hora.
            current_time = now.strftime('%H:%M')

            # Verifica se a hora atual e menor que o tempo para rodar o script.
            if current_time > future_time:
                execute.execMain()

                return True
            else:
                # Verifica se a hora atual e igual a hora futura e a função "Home" e true.
                if current_time >= futureRaroLegend_time and casa:
                    # Função que vai navegar até a tela "Character" e manipular os comandos necessários.
                    executeSuperRaroLegend.screenCharacterSuperRaroLegend()

                    casa = False
                try:
                    # Verifica se tem que mudar de mapa.
                    execute.screenRoundNewMap()

                    # Verifica se deu erro o "Unknown".
                    execute.screenErroUnknown()

                    # Verifica se deu erro o "Overloaded".
                    execute.screenErroOverloaded()
                finally:
                    pass

                print("Pausa de {} minuto: {}".format(int(timeSleep/60), datetime.now().strftime('%H:%M:%S')))

                time.sleep(timeSleep)

                # Move o mouse, não AFK.
                x, y = pyautogui.position()
                pyautogui.moveTo(x - 20, y, 2)
                click.mouseLeftClick()
                pyautogui.moveTo(x + 10, y, 2)

    while True:
        print("Ciclo completo: {}".format(verifyTimeFuture()))
