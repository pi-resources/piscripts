#!/usr/bin/env python

import os, re;
sensors = [];

def getTemperature(sensorid):
	return getRawTemperature(sensorid) / 1000;

def getRawTemperature(sensorid):
	fh = open("/sys/bus/w1/devices/{}/w1_slave".format(sensorid), "r");
	for line in fh:
		pass
	temperature = re.search('t=([0-9]+)', line).group(1);
	return float(temperature);
	
def printSensors():
	print("The following sensors were found on this system:");
	for sensor in sensors:
		print "  {}".format(sensor);

def getSensors():
	return sensors;

def getTemperatures():
	temperatures = {};
	for sensor in sensors:
		temperatures[sensor] = getTemperature(sensor);
	return temperatures;

def _loadSensors():
	dir = os.listdir("/sys/bus/w1/devices/");
	for a in dir:
		if a <> 'w1_bus_master1':
			sensors.append(a);
	#print(sensors);

_loadSensors();

if __name__ == "__main__":
	printSensors();