import mss


def printScreem():

    with mss.mss() as mss_instance:
        mss_instance.shot(mon=0, output='screenShot.jpg')

    return True
