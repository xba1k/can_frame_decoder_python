#!/usr/bin/python3

import socket
import sys
from datetime import datetime
from struct import unpack

UDP_PORT = 1080

SI_CHARGE_PARAMS_FRAME = 0x351
SI_VOLTAGE_FRAME = 0x356
SI_SOC_FRAME = 0x355
SI_ID_FRAME = 0x35F
SI_NAME_FRAME = 0x35E
SI_FAULT_FRAME = 0x35A


def print_charge_params(frameId, frameData):
    (finalVoltage, maxChargeCurrent, maxDischargeCurrent, finalDischargeVoltage) = unpack("<H H H H", frameData)
    print("Charge params: finalVoltage {:.2f}, maxChargeCurrent {:.2f}, maxDischargeCurrent {:.2f}, finalDischargeVoltage {:.2f}".format(finalVoltage / 10.0, 
maxChargeCurrent / 10.0, maxDischargeCurrent / 10.0, finalDischargeVoltage / 10.0))

def print_voltage(frameId, frameData):
    (batteryVoltage, batteryCurrent, batteryTemp) = unpack("<H H H", frameData)
    print("Voltage params: batteryVoltage {:.2f}, batteryCurrent {:.2f}, batteryTemp {}".format(batteryVoltage / 10.0, batteryCurrent / 10.0, batteryTemp))

def print_soc(frameId, frameData):
    (stateOfCharge, stateOfHealth, stateOfChargeHighPrecision) = unpack("<H H H", frameData)
    print("States: stateOfCharge {}, stateOfHealth {}, stateOfChargeHighPrecision {}".format(stateOfCharge, stateOfHealth, stateOfChargeHighPrecision))

def print_id(frameId, frameData):
    (chemistry, hw_ver, capacity, sw_ver) = unpack("<2s H H H", frameData)
    print("ID: chemistry {}, hw_ver {}, capacity {:.2f}, sw_ver {}".format(chemistry.decode(), hw_ver, capacity / 10.0, sw_ver))

def print_fault(frameId, frameData):
    (f0, f1, f2, f3) = unpack("<H H H H", frameData)
    print("Faults: f0 {}, f1 {}, f2 {}, f3 {}".format(f0, f1, f2, f3))

frame_types = {
    SI_CHARGE_PARAMS_FRAME: lambda frameId, frameData: print_charge_params(frameId, frameData),
    SI_VOLTAGE_FRAME: lambda frameId, frameData: print_voltage(frameId, frameData),
    SI_SOC_FRAME: lambda frameId, frameData: print_soc(frameId, frameData),
    SI_ID_FRAME: lambda frameId, frameData: print_id(frameId, frameData),
    SI_NAME_FRAME: lambda frameId, frameData: print("BMS Name: {}".format(frameData.decode())),
    SI_FAULT_FRAME: lambda frameId, frameData: print_fault(frameId, frameData),
    0: lambda frameId, frameData: print("unknown frame type {}".format(hex(frameId)))
}

def print_frame(data):
    frameId = unpack('<I', data[0:4])[0]

    if frameId in frame_types:
        frame_types[frameId](frameId, data[4:])
    else:
        frame_types[0](frameId, data[4:])


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('', UDP_PORT)
s.bind(server_address)

print("waiting for packets...")

while True:
    data, address = s.recvfrom(64)
    print(str(datetime.now())+" "+address[0]+" ", end='')
    print_frame(data)
