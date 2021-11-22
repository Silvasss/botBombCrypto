import mss


def printScreem(screen):

    with mss.mss() as mss_instance:
        mss_instance.shot(mon=screen, output='screenShot.jpg')

    return True