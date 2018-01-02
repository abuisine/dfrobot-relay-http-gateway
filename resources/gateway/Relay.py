import json
import socket

class Relay:
	def __init__(self, hostname, port):
		self.hostname	= hostname
		self.port		= port

	def send(self, message):
		self.socket	= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.settimeout(3)
		self.socket.connect((self.hostname, int(self.port)))
		self.socket.sendall(json.dumps(message, separators=(',',':')))
		received = self.socket.recv(1024)[:-1]
		print "Received (%d): %s"%(len(received),received)
		self.socket.close()

		return json.loads(received)

	def setRelayStatus(self, relays):
		return self.send(relays)

	def getRelayStatus(self):
		return self.send({"get":"relayStatus"})
		
	def setDeviceName(self, name):
		{"name":"DFRobot"}
		pass
	def getDeviceName(self):
		{"get":"name"}
		pass
	def setNetworkConfiguration(self, configuration):
		{"ipaddr":"192.168.1.10","gateway":"192.168.1.1","netmask":"255.255.2 55.0","port":"2000"}
		pass
	def getNetworkConfiguration(self):
		{"get":"netconfig"}
		pass
	def getVersion(self):
		return self.send({"get":"version"})

	def setRS485Address(self, address):
		{"RS485addr":"22"}
		pass
	def getRS485Address(self):
		{"get":"RS485addr"}
		pass
	def setBaudRate(self, baudrate):
		{"baudrate":"9600"}
		pass
	def getBaudRate(self):
		{"get":"baudrate"}
		pass
	def setDHCPState(self, state):
		{"dhcp":"on"}
		pass
	def getDHCPState(self):
		{"get":"dhcp"}
		pass
	def reboot(self):
		{"reboot":"1"}
		pass



