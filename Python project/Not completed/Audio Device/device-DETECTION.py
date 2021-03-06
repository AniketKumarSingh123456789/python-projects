# lsusbBus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
#Bus 001 Device 002: ID 0424:9512 Standard Microsystems Corp.
#Bus 001 Device 003: ID 0424:ec00 Standard Microsystems Corp.
#Bus 001 Device 006: ID 05e3:0606 Genesys Logic, Inc. USB 2.0 Hub / D-Link DUB-H4 USB 2.0 Hub
#Bus 001 Device 009: ID 1130:f211 Tenx Technology, Inc. TP6911 Audio Headset

# cat d.py
import pyaudio

p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
#for each audio device, determine if is an input or an output and add it to the appropriate list and dictionary
for i in range (0,numdevices):
        if p.get_device_info_by_host_api_device_index(0,i).get('maxInputChannels')>0:
                print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0,i).get('name'))

        if p.get_device_info_by_host_api_device_index(0,i).get('maxOutputChannels')>0:
                print("Output Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0,i).get('name'))

devinfo = p.get_device_info_by_index(1)
print("Selected device is ",devinfo.get('name'))
if p.is_format_supported(44100.0,  # Sample rate
                         input_device=devinfo["index"],
                         input_channels=devinfo['maxInputChannels'],
                         input_format=pyaudio.paInt16):
  print('Yay!')
p.terminate()