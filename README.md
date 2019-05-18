# gpio
Wiring

There are four pins on the ultrasound module that are connected to the Raspberry:

    VCC to Pin 2 (VCC)
    GND to Pin 6 (GND)
    TRIG to Pin 12 (GPIO18)
    connect the 330Ω resistor to ECHO.  On its end you connect it to Pin 18 (GPIO24) and through a 470Ω resistor you connect it also to Pin6 (GND).

We do this because the GPIO pins only tolerate maximal 3.3V. The connection to GND is to have a obvious signal on GPIO24. If no pulse is sent, the signal is 0 (through the connection with GND), else it is 1. If there would be no connection to GND, the input would be undefined if no signal is sent (randomly 0 or 1), so ambiguous.

Here is the structure as a circuit diagram:
