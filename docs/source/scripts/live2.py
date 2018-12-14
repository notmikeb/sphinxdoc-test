import sys
import os
import configparser

path = r"C:\Program Files (x86)\Frontline Test System II\Frontline 15"
name = r"Liveimport.ini"

fpath = os.path.join(path, name)

cp1 = configparser.ConfigParser()
cp1data = cp1.read(fpath)
print(cp1data)
print(cp1.sections())

"""
this is the read result of ini file
"""
keys = cp1.sections()
for k1 in keys:
  for k2 in cp1[k1]:
     print("{} {} {}".format(k1, k2, cp1[k1][k2]))

print(r"example file is at C:\Program Files (x86)\Frontline Test System II\Frontline 15\Live Import Developers Kit\Straight C Sample")   





"""
tools
http://www.nirsoft.net/utils/dll_export_viewer.html

C:\Program Files (x86)\Frontline Test System II\Frontline 15\Live Import Developers Kit\h
liveimport.h

typedef HRESULT (InitializeLiveImport)(const TCHAR* szMemoryName, const TCHAR* szConfiguration, bool* pboolSuccess);
typedef HRESULT (SendFrame)(
		int iOriginalLength,				// The "real" length of a frame. Some frames may be truncated, so this may not be the same as included length
		int iIncludedLength,				// The size of the data passed in this call
		const BYTE* pbytFrame,						// The actual bytes of the frame
		int iDrf,							// any errors or other data related flag
		int iStream,						// Which side this data comes from
		__int64 i64Timestamp);
"""

from ctypes import *

dll1 = cdll.WinDll("LiveImportAPI_x64")

b1 = c_bool()
bp1 = pointer(b1)
name = create_string_buffer(b"ComProbe Protocol Analysis System Live Import.FDFFFFFF!7776944237B4D3E24FD48E0EA82BCD697378D2;A43B83FD")
conf = create_string_buffer(b"Version=6\nWindowTitle=Virtual Sniffer\nDriverInfo=Bluetooth Virtual Sniffer\nSides=Host,1000000;Controller,1000000\nSdeName=Octets\nStackAuto=true\nStack=0x7f008039\nDrf=Command;ACL;SCO;Event\n")

g_initializeliveimport = getattr(dll1, "InitializeLiveImport")
g_initializeliveimport(name, conf, bp1)


g_releaseliveimport = getattr(dll1, "ReleaseLiveImport")

g_sendframe = getattr(dll1,"SendFrame")

framesize = c_int()
sampleframe =  b"\x09\x10\x00"
