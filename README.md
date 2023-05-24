# Micropython Package for the ADS1115

This library provides a Micropython package for the ADS1115.
See **https://joy-it.net/en/products/COM-KY053ADC** for more details.

## Behaviour considered to be a pass
As long as the raw value and voltages still change depending on what is/will be connected. This is considered a pass, even the small jitter of up to +/- 10 in the raw value is an indicator of a pass.

## Behaviour considered to be a fail
As soon as the output values no longer change. This is considered a failure, since the functionality is basically no longer given and no "real" value can be read.

## ADS1115 possible addresses

| Pin         | Address        |
| ----------- | -------------- |
| ADDR to GND | 0x48 (default) |
| ADDR to VCC | 0x49           |
| ADDR to SDA | 0x4A           |
| ADDR to SCL | 0x4B           |

## init
You can use the function `init(...)` to initialize the ADS with the given parameters.
```python
# The init function takes 4 parameters
# init(adr, gain, rate, mode)
# The parameter adr allows to change the I2C address to the address of the physical device.
# The parameter gain allows to change the value used in measurements and calculations
# The parameter rate allows to change the number of measurements that the ADS1115 should perform in one second.
# The mode parameter allows you to change how the ADS performs its measurements.
# default initialization with address 0x48, gain 2, rate 4 and mode False
ADS1115.init(0x48, 1, 4, False)
```

## setGain
You can use the `setGain(...)` function to change the value used in measurements and calculations.
```python
# The function "setGain" takes 1 parameter
# setGain(gain)
# The parameter gain allows to change the value (0 to 5) used in measurements and calculations
# gain = 0 -> + /-6.144V range = Gain 2/3
# gain = 1 -> + /-4.096V range = Gain 1
# gain = 2 -> + /-2.048V range = gain 2 (default)
# Gain = 3 -> + /-1.024V range = Gain 4
# Gain = 4 -> + /-0.512V range = Gain 8
# Gain = 5 -> + /-0.256V range = Gain 16
# default call of function with value 2
ADS1115.setGain(2)
```

## setRate
You can use the `setRate(...)` function to change the number of measurements the ADS1115 should make in one second.
```python
# The setRate function takes 1 parameter
# setRate(rate)
# The parameter rate allows to change the number of measurements the ADS1115 should make in one second, based on the given value (0 to 7)
# rate = 0 -> _DR_128SPS 8 samples per second
# rate = 1 -> _DR_250SPS 16 samples per second
# rate = 2 -> _DR_490SPS 32 samples per second
# rate = 3 -> _DR_920SPS 64 samples per second
# Rate = 4 -> _DR_1600SPS 128 samples per second (default)
# Rate = 5 -> _DR_2400SPS 250 samples per second
# rate = 6 -> _DR_3300SPS 475 samples per second
# rate = 7 -> _DR_860SPS 860 samples per second
# default call of the function with value 4
ADS1115.setRate(4)
```

## setMode
You can use the function `setMode(...)` to change how the ADS performs its measurements.
```python
# The function "setMode" takes 1 parameter
# setMode(mode)
# The mode parameter allows to change how the ADS performs its measurements
# mode = True -> single measurement
# mode = False -> continuous measurements
# default call of the function with the value False
ADS1115.setMode(False)
```

## Read raw values from channels
To read the raw values from each channel, you can use the `read(...)` function, which returns the raw value of the specified channel.
```python
# The read function takes 1 parameter
# read(chan)
# chan = 0 -> Single - ended AIN0 (default)
# chan = 1 -> Single - ended AIN1
# chan = 2 -> Single - ended AIN2
# chan = 3 -> Single - ended AIN3
# chan = 4 -> Differential P = AIN0, N = AIN1
# chan = 5 -> Differential P = AIN0, N = AIN3
# chan = 6 -> Differential P = AIN1, N = AIN3
# chan = 7 -> Differential P = AIN2, N = AIN3
# Reads the specified channel (chan) based on the specified parameter (0 to 7)
# standard call of the function without value
ADS1115.read()
```

## Converting raw values to voltages
To calculate the voltages of each channel, you can use the function `raw_to_v(...)`, which returns the voltages based on the given 'raw' variables.
```python
# The raw_to_v function takes 1 parameter
# raw_to_v(raw)
# Reads an arbitrary raw value (raw) either from the previously specified channel or from any other variable and converts it to voltages.
# Standard call of the function without value
ADS1115.raw_to_v()
```

## License

MIT
