# PciIdsParser.py
#
# Copyright (C) 20025 MaxWu efipy.core@gmail.com All rights reserved.
#
# License GPL V2
#

PciIds = {}
PciClass = {}

def ParsingPciName (s):
    global VendorId, DeviceId

    if s [0:2] == '\t\t':
        SubVendor, SubDevice, SubName = int (s[2: 6], 16), int (s[7: 11], 16), s[13: -1]
        VendorName, DeviceDict = PciIds [VendorId]
        DeviceName, SubDict    = DeviceDict [DeviceId]
        SubDict [(SubVendor, SubDevice)] = SubName

    elif s[0] == '\t':
        DeviceId, DeviceName = int (s[1:5], 16), s[7: -1]
        VendorName, DeviceDict = PciIds [VendorId]
        DeviceDict [DeviceId]  = (DeviceName, {})           # Device Name, Sub Dict

    else:
        VendorId, VendorName = int(s[:4], 16), s[6: -1]
        PciIds [VendorId] = (VendorName, {})                 # Vendor Name, Device Dict

def ParsingPciClass (s):
    global ClassCode, SubClass

    if s[0] == 'C':
        ClassCode, ClassName = int (s[2:4], 16), s[6:-1]
        PciClass [ClassCode] = (ClassName, {})      # Class Name, SubClass Dict

    elif s[0:2] == '\t\t':
        ProgIf, ProgName = int (s[2:4], 16), s[6:-1]

        ClassName, SubDict = PciClass [ClassCode]
        SubName, ProgIfDict = SubDict [SubClass]
        ProgIfDict [ProgIf] = ProgName

    elif s[0:1] == '\t':
        SubClass, SubName = int(s[1:3], 16), s[5:-1]

        ClassName, SubDict = PciClass [ClassCode]
        SubDict [SubClass] = (SubName, {})          # SubClass Name, Prof-If Idct

import os
PciIdsFileHandle = open (os.path.join ('pciids', 'pci.ids'), 'r', encoding = 'utf-8')

while True:
    Line = PciIdsFileHandle.readline ()
    if Line == None or len (Line) == 0:
        break
    if Line[0] in ('#', '\n', '\r', ' '):
        continue
    elif Line [0] != '\t':
        if Line[:2] == 'C ':
            ParsingFunc = ParsingPciClass
        else:
            ParsingFunc = ParsingPciName

    ParsingFunc (Line)


if __name__ == '__main__':
  print (f'''# pciids.py
#
# Copyright (C) 2025 - 2926 MaxWu efipy.core@gmail.com All rights reserved.
#
# License GPL V2
#
# Reference from
#   pci.ids         https://pci-ids.ucw.cz/
#
# This file is created by PciIdsParser.py. Do not edit it.
#
#  Command:
#   python PciIdsParser.py > pciids.py
#
#
PciIds = {PciIds}

PciClass = {PciClass}
''')
