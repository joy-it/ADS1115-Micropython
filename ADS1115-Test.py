# Import all required libraries
import machine
import ADS1115
import sys
from time import sleep

# Declaration of the required variables for the channels
chan = 0
chan1 = 4

if __name__ == '__main__':
    try:
        # Initialization of the ADC
        ADS1115.init(0x48, 1, 4, False)
        print("start")
        while True:
            # Main loop with all 3 functions of the library
            print(ADS1115.read(chan))
            print(str(ADS1115.raw_to_v(ADS1115.read(chan))) + " V")
            print(ADS1115.readMulti(chan, chan1))
            sleep(1)

    except KeyboardInterrupt:
        sys.exit()