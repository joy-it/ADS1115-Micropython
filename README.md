# Micropython Package for the ADS1115

This library provides a Micropython package for the ADS1115.
See **https://joy-it.net/en/products/COM-KY053ADC** for more details.

## Behaviour considered to be a pass
As long as the raw value and voltages still change depending on what is/will be connected. This is considered a pass, even the small jitter of up to +/- 10 in the raw value is an indicator of a pass.

## Behaviour considered to be a fail
As soon as the output values no longer change. This is considered a failure, since the functionality is basically no longer given and no "real" value can be read.

## init
You can use the `init(...)` function to initialize the ADS with the given parameters.
```python
# The init function takes 4 parameters
# init(adr, gain, rate, mode)
# The parameter adr allows you change the I2C address to the address of your physical device
# The parameter gain allows you to change the value used in measurements and calculations
# The parameter rate allows you to change the number of measurements that the ADS1115 should perform in one second
# The parameter mode allows you to change how the ADS performs its measurments
# Standard initialization with address 0x48, gain 2, rate 4 and mode False
 ADS1115.init(0x48, 1, 4, False)
```

## setGain
You can use the `setGain(...)` function to change the value used in measurements and calculations.
```python
# The setGain function takes 1 parameter
# setGain(gain)
# The parameter gain allows you to change the value (0 to 5) used in measurements and calculations
# + /-6.144V range  =  Gain 2/3
# + /-4.096V range  =  Gain 1
# + /-2.048V range  =  Gain 2 (default)
# + /-1.024V range  =  Gain 4
# + /-0.512V range  =  Gain 8
# + /-0.256V range  =  Gain 16
# Standard call of function with value 2
# ADS1115.setGain(2)
```

## setRate
You can use the `setRate(...)` function to change the number of measurements that the ADS1115 should perform in one second.
```python
# The setRate function takes 1 parameter
# setRate(rate)
# The parameter rate allows you to change the number of measurements that the ADS1115 should perform in one second based on the given value (0 to 7)
# _DR_128SPS     8 samples per second
# _DR_250SPS     16 samples per second
# _DR_490SPS     32 samples per second
# _DR_920SPS     64 samples per second
# _DR_1600SPS    128 samples per second (default)
# _DR_2400SPS    250 samples per second
# _DR_3300SPS    475 samples per second
# _DR_860SPS     860 samples per Second
# Standard call of function with value 4
# ADS1115.setRate(4)
```

## setMode
You can use the `setMode(...)` function to change how the ADS performs its measurments.
```python
# The setMode function takes 1 parameter
# setMode(mode)
# The parameter mode allows you to change how the ADS performs its measurments
# mode = True -> Single measurment
# mode = False -> Continous measurments
# Standard call of function with value False
# ADS1115.setMode(False)
```

## Converting Raw Values to Voltages
To calculate the voltages of the individual channels, you can use the `raw_to_v(...)` function, which returns the voltages based on the entered 'raw' variables.
```python
# The raw_to_v function takes 1 parameter
# raw_to_v(raw)
# Reads any raw value (raw) either from the previously specified channel or from any other variable and converts it to voltages
# Standard call of function with no value
ADS1115.raw_to_v()
```

## License

MIT
