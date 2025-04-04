# PciIdsSample.py
#
# Copyright (C) 20225 MaxWu efipy.core@gmail.com All rights reserved.
#
# PciIdsSample.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# PaTest.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy2.  If not, see <http://www.gnu.org/licenses/>.
#
import pciids

vid = 0x8086
did = 0x0116

SubId = (0x144d, 0xc652)

VendorName, DeviceDict = pciids.PciIds [vid]
print (f'{vid:04X}, {VendorName}')

DeviceName, SubIdDict = DeviceDict [did]
print (f'{did:04X}, {DeviceName}')

SubIdName = SubIdDict [SubId]
print (f'{SubId}, {SubIdName}')

print ()
ClassId  = 0x0C
SubClass = 0x03
ProgIf   = 0x40

ClassName, SubClassDict = pciids.PciClass [ClassId]
print (f'{ClassId:02X}, {ClassName}')

SubClassName, ProgIfDict = SubClassDict [SubClass]
print (f'{SubClass:02X}, {SubClassName}')

ProgIfName = ProgIfDict [ProgIf]
print (f'{ProgIf:02X}, {ProgIfName}')