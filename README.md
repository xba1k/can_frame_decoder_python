# can_frame_decoder

## Overview

This is an example Python decoder for CAN frames broadcasted by the CANBridge via UDP. Compatible with SMA frame format.

## Installation

Depends on Python 3, should be in path.

## Demo

```
./frame_decoder.py 
waiting for packets...
2022-03-04 10:29:19.500907 192.168.1.62 BMS Name: SIConfig
2022-03-04 10:29:20.105072 192.168.1.62 ID: chemistry Li, hw_ver 3844, capacity 66.00, sw_ver 5905
2022-03-04 10:29:20.709253 192.168.1.62 States: stateOfCharge 85, stateOfHealth 80, stateOfChargeHighPrecision 8500
2022-03-04 10:29:30.616441 192.168.1.62 BMS Name: SIConfig
2022-03-04 10:29:31.220604 192.168.1.62 ID: chemistry Li, hw_ver 3844, capacity 66.00, sw_ver 5905
2022-03-04 10:29:31.824770 192.168.1.62 States: stateOfCharge 85, stateOfHealth 80, stateOfChargeHighPrecision 8500
```
