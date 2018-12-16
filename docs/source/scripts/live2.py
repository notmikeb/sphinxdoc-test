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
import ctypes

dll1 = ctypes.WinDLL(r"LiveImportAPI_x64.dll")

b1 = c_bool()
bp1 = pointer(b1)
name = create_string_buffer(b"ComProbe Protocol Analysis System Live Import.FDFFFFFF!7776944237B4D3E24FD48E0EA82BCD697378D2;A43B83FD")
conf = create_string_buffer(b"Version=6\nWindowTitle=Virtual Sniffer\nDriverInfo=Bluetooth Virtual Sniffer\nSides=Host,1000000;Controller,1000000\nSdeName=Octets\nStackAuto=true\nStack=0x7f008039\nDrf=Command;ACL;SCO;Event\n")

g_initializeliveimport = getattr(dll1, "InitializeLiveImport")
init_ret = g_initializeliveimport(name, conf, bp1)


g_releaseliveimport = getattr(dll1, "ReleaseLiveImport")

g_sendframe = getattr(dll1,"SendFrame")

framesize = c_int()
sampleframe1 =  b"\x09\x10\x00"
sampleframe2 = b"\x0e\x0a\x01\x09\x10\x00\x82\x14\x01\x5b\x02\x00" # 0x01 (slide),0x08  (flag)
"""
Action4ButtonText=Send ACL Data
Action4LabelText=Simulate sending ACL data from a Host to a remote Bluetooth Device.
Action4Data=0x00,0x02,0x28,0x20,0x1c,0x00,0x18,0x00,0x40,0x00,0x4d,0x65,0x73,0x73,0x61,0x67,0x65,0x20,0x74,0x6f,0x20,0x72,0x65,0x6d,0x6f,0x74,0x65,0x20,0x64,0x65,0x76,0x69,0x63,0x65
"""
sampleframe3 = b"\x28\x20\x1c\x00\x18\x00\x40\x00\x4d\x65\x73\x73\x61\x67\x65\x20\x74\x6f\x20\x72\x65\x6d\x6f\x74\x65\x20\x64\x65\x76\x69\x63\x65" #
"""
Action5ButtonText=Receive ACL Data
Action5LabelText=Simulate receiving ACL data from a remote Bluetooth Device.
Action5Data=0x01,0x02,0x28,0x20,0x1e,0x00,0x1a,0x00,0x40,0x00,0x4d,0x65,0x73,0x73,0x61,0x67,0x65,0x20,0x66,0x72,0x6f,0x6d,0x20,0x72,0x65,0x6d,0x6f,0x74,0x65,0x20,0x64,0x65,0x76,0x69,0x63,0x65
"""
sampleframe4 = b"\x28\x20\x1e\x00\x1a\x00\x40\x00\x4d\x65\x73\x73\x61\x67\x65\x20\x66\x72\x6f\x6d\x20\x72\x65\x6d\x6f\x74\x65\x20\x64\x65\x76\x69\x63\x65"

if 0 == init_ret:
  import time
  print("init okay !")
  g_sendframe( c_int(len(sampleframe1)), c_int(len(sampleframe1)), sampleframe1, 1, 0, c_longdouble(time.time()))
  g_sendframe( c_int(len(sampleframe2)), c_int(len(sampleframe2)), sampleframe2, 8, 1, c_longdouble(time.time())) 
  g_sendframe( c_int(len(sampleframe3)), c_int(len(sampleframe3)), sampleframe3, 2, 0, c_longdouble(time.time())) 
  g_sendframe( c_int(len(sampleframe4)), c_int(len(sampleframe4)), sampleframe4, 2, 1, c_longdouble(time.time())) 
else:
  print("init failed !")

g_releaseliveimport()