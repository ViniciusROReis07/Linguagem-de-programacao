from time import sleep

def relogio():
    while True:
        h = 23
        while h >= 00:
            m = 59
            while m >= 00:
                s = 59
                while s >= 00:
                    print(f'{h:02}:{m:02}:{s:02}')
                    sleep(1)
                    s -= 1
                m -= 1
            h -= 1


relogio()
