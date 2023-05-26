# Import of Librarys
from machine import I2C, Pin
import utime

# Register variables
_REGISTER_MASK = 0x03
_REGISTER_CONVERT = 0x00
_REGISTER_CONFIG = 0x01
_REGISTER_LOWTHRESH = 0x02
_REGISTER_HITHRESH = 0x03

_OS_MASK = 0x8000
_OS_SINGLE = 0x8000     # Write: Set to start a single - conversion
_OS_BUSY = 0x0000       # Read: Bit = 0 when conversion is in progress
_OS_NOTBUSY = 0x8000    # Read: Bit = 1 when no conversion is in progress

# Channel variables
_MUX_MASK = 0x7000
_MUX_DIFF_0_1 = 0x0000  # Differential P = AIN0, N = AIN1 (default)
_MUX_DIFF_0_3 = 0x1000  # Differential P = AIN0, N = AIN3
_MUX_DIFF_1_3 = 0x2000  # Differential P = AIN1, N = AIN3
_MUX_DIFF_2_3 = 0x3000  # Differential P = AIN2, N = AIN3
_MUX_SINGLE_0 = 0x4000  # Single - ended AIN0
_MUX_SINGLE_1 = 0x5000  # Single - ended AIN1
_MUX_SINGLE_2 = 0x6000  # Single - ended AIN2
_MUX_SINGLE_3 = 0x7000  # Single - ended AIN3

# Gain variables
_PGA_MASK = 0x0E00
_PGA_6_144V = 0x0000    # + /-6.144V range  =  Gain 2/3
_PGA_4_096V = 0x0200    # + /-4.096V range  =  Gain 1
_PGA_2_048V = 0x0400    # + /-2.048V range  =  Gain 2 (default)
_PGA_1_024V = 0x0600    # + /-1.024V range  =  Gain 4
_PGA_0_512V = 0x0800    # + /-0.512V range  =  Gain 8
_PGA_0_256V = 0x0A00    # + /-0.256V range  =  Gain 16

# Mode variables
_MODE_MASK = 0x0100
_MODE_CONTIN = 0x0000   # Continuous conversion mode
_MODE_SINGLE = 0x0100   # Power - down single - shot mode (default)

# Samplerate variables
_DR_MASK = 0x00E0       # ADS1115
_DR_128SPS = 0x0000     # 8 samples per second
_DR_250SPS = 0x0020     # 16 samples per second
_DR_490SPS = 0x0040     # 32 samples per second
_DR_920SPS = 0x0060     # 64 samples per second
_DR_1600SPS = 0x0080    # 128 samples per second (default)
_DR_2400SPS = 0x00A0    # 250 samples per second
_DR_3300SPS = 0x00C0    # 475 samples per second
_DR_860SPS = 0x00E0     # 860 samples per Second

_CMODE_MASK = 0x0010
_CMODE_TRAD = 0x0000    # Traditional comparator with hysteresis (default)
_CMODE_WINDOW = 0x0010  # Window comparator

_CPOL_MASK = 0x0008
_CPOL_ACTVLOW = 0x0000  # ALERT / RDY pin is low when active (default)
_CPOL_ACTVHI = 0x0008   # ALERT / RDY pin is high when active

_CLAT_MASK = 0x0004     # Determines if ALERT / RDY pin latches once asserted
_CLAT_NONLAT = 0x0000   # Non - latching comparator (default)
_CLAT_LATCH = 0x0004    # Latching comparator

_CQUE_MASK = 0x0003
_CQUE_1CONV = 0x0000    # Assert ALERT / RDY after one conversions
_CQUE_2CONV = 0x0001    # Assert ALERT / RDY after two conversions
_CQUE_4CONV = 0x0002    # Assert ALERT / RDY after four conversions
_CQUE_NONE = 0x0003     # Disable the comparator and put ALERT / RDY in high state (default)

# List of all usable gains
_GAINS = [
        _PGA_6_144V,    # 2 / 3x
        _PGA_4_096V,    # 1x
        _PGA_2_048V,    # 2x (default)
        _PGA_1_024V,    # 4x
        _PGA_0_512V,    # 8x
        _PGA_0_256V     # 16x
]

# List of voltage values corresponding to the list of usable gains
_GAINS_V = [
        6.144,          # 2 / 3x
        4.096,          # 1x
        2.048,          # 2x (default)
        1.024,          # 4x
        0.512,          # 8x
        0.256           # 16x
]

# List of the different usable channels
_CHANNELS = [           # CH1|CH2
        _MUX_SINGLE_0,  # (0, None) (default)
        _MUX_SINGLE_1,  # (1, None)
        _MUX_SINGLE_2,  # (2, None)
        _MUX_SINGLE_3,  # (3, None)
        _MUX_DIFF_0_1,  # (0, 1)
        _MUX_DIFF_0_3,  # (0, 3)
        _MUX_DIFF_1_3,  # (1, 3)
        _MUX_DIFF_2_3,  # (2, 3)
]

# List of all usable sample rates
_RATES = [
        _DR_128SPS,     # 8 samples per second
        _DR_250SPS,     # 16 samples per second
        _DR_490SPS,     # 32 samples per second
        _DR_920SPS,     # 64 samples per second
        _DR_1600SPS,    # 128 samples per second (default)
        _DR_2400SPS,    # 250 samples per second
        _DR_3300SPS,    # 475 samples per second
        _DR_860SPS      # 860 samples per Second
]

i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 100000)
utime.sleep_ms(10)

# All global variables used in the library, as well as some predefined variables that serve as default values.
adsaddress = 0x48
adsgain = _GAINS[2]
adsrate = _RATES[4]
adsmode = _MODE_CONTIN
adsgainv = 2
temp2 = bytearray(2)

# Initialization of the ADS based on user input.
def init(adr, gain, rate, mode):
    global adsaddress
    adsaddress = adr
    setGain(gain)
    setRate(rate)
    setMode(mode)

# Change the gains based on the user input.
def setGain(gain):
    global adsgain
    global adsgainv
    adsgain = _GAINS[gain]
    adsgainv = gain

# Change the sampling rate based on user input.
def setRate(rate):
    global adsrate
    adsrate = _RATES[rate]

# Change the mode based on user input.
def setMode(mode = True):
    global adsmode
    if (mode):
        adsmode = _MODE_SINGLE
    else:
        adsmode = _MODE_CONTIN

# Write the desired 16-bit value into the register.
def _write_register(reg, val):
    temp2[0] = val >> 8
    temp2[1] = val & 0xff
    i2c.writeto_mem(adsaddress, reg, temp2)

# Read the 16-bit register value to be returned.
def _read_register(reg):
    i2c.readfrom_mem_into(adsaddress, reg, temp2)
    return (temp2[0] << 8) | temp2[1]

# Reads any raw value (raw) either from the previously specified channel or from another variable and converts it to voltages.
def raw_to_v(raw):
    v_p_b = _GAINS_V[adsgainv] / 32767
    return round(raw * v_p_b, 2)


# Reads the specified channel of the ADS1115.
def read(chan):
    # Linking of all required data by the bitwise operator 'OR ('|')'.
    config = 0x0000
    config |= _CHANNELS[chan]
    config |= adsgain
    config |= adsrate
    config |= adsmode
    config |= _CQUE_NONE
    # Send the required data to the specified register.
    _write_register(_REGISTER_CONFIG, config)
    while not _read_register(_REGISTER_CONFIG) & _OS_NOTBUSY:
        break
    # Reading the returned data.
    res = _read_register(_REGISTER_CONVERT)
    if (res < 32768):
        return res
    else:
        res = res - 65469
        return res
    
# Reading multiple ADS1115 channels at once
def readMulti(start, end):
    res1 = 0
    res2 = 0
    res3 = 0
    res4 = 0
    if (start > 4): start = 4
    if (start < 0): start = 0
    if (end > 4): end = 4
    if (end < 0): end = 0
    for x in range (start, end):
        if (x == 0):
            res1 = read(x)
            utime.sleep_ms(25)
        if (x == 1):
            res2 = read(x)
            utime.sleep_ms(25)
        if (x == 2):
            res3 = read(x)
            utime.sleep_ms(25)
        if (x == 3):
            res4 = read(x)
            utime.sleep_ms(25)
    return res1, res2, res3, res4