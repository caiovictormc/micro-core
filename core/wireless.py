import ujson
import network

from microconf import conf


class WiFi:
    def __init__(self):
        self._nic = network.WLAN(network.STA_IF)
        self._nic.active(True)
        self._ssid_list = conf('wifi')

    def quickly_connection(self):
        pass

    def better_connection(self):
        pass
