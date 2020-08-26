import pyaudio,sounddevice as sd
p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range (0,numdevices):
        if p.get_device_info_by_host_api_device_index(0,i).get('maxInputChannels')>0:
                print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0,i).get('name'))
                sd.default.device = i
        if p.get_device_info_by_host_api_device_index(0,i).get('maxOutputChannels')>0:
                print("Output Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0,i).get('name'))
                sd.default.device = i
        print(sd.query_devices())
devinfo = p.get_device_info_by_index(1)
print("Selected device is ",devinfo.get('name'))
p.terminate()