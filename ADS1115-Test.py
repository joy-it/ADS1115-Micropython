import machine
import ADS1115
import sys
from time import sleep

chan = 0

if __name__ == '__main__':
    try:
        ADS1115.init(0x48, 1, 4, False)
        print("start")
        while True:
            print(ADS1115.read(chan))
            print(str(ADS1115.raw_to_v(ADS1115.read(chan))) + " V")
            sleep(1)

    except KeyboardInterrupt:
        sys.exit()
