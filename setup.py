#! /usr/binn/python3 -B
# -*- config: utf-8 -*-

import sys
import os
import subprocess
import config

def install_packages ():
#	subprocess.call (["cd", /home/pi"])
	config.logger.info ("Update packages")
	subprocess.call (["sudo", "apt-get", "-y", "update"])
	subprocess.call (["sudo", "apt-get", "-y", "upgrade"])

	config.logger.info ("Install packages")
	subprocess.call (["sudo", "apt-get", "-y", "install", "config"])
	subprocess.call (["sudo", "apt-get", "-y", "install", "python3-pip"])
	subprocess.call (["sudo", "apt-get", "-y", "install", "python-dev"])
	subprocess.call (["sudo", "apt-get", "-y", "install", "python3-scipy"])
	subprocess.call (["sudo", "apt-get", "-y", "install", "build-essential"])
	subprocess.call (["sudo", "pip3", "install", "--upgrade", "setuptools"])
	subprocess.call (["sudo", "pip3", "install", "--upgrade", "pip"])
	subprocess.call (["sudo", "pip3", "install", "rpi.gpio"])
	subprocess.call (["sudo", "pip3", "install", "pyserial"])
	subprocess.call (["sudo", "pip3", "install", "ntpdate"])
	subprocess.call (["sudo", "pip3", "install", "i2c-tools"])
	subprocess.call (["sudo", "pip3", "install", "libi2c-dev"])
	subprocess.call (["sudo", "pip3", "install", "subversion"])
	subprocess.call (["sudo", "pip3", "install", "python-smbus"])
	subprocess.call (["sudo", "pip3", "install", "jupyter"])
	subprocess.call (["sudo", "apt-get", "-y", "install", "python3-matplotlib"])
	subprocess.call (["sudo", "apt-get", "-y", "install", "python3-numpy"])
	subprocess.call (["sudo", "apt-get", "-y", "install", "git"])

	config.logger.info ("Install deep-learning packages")
	subprocess.call (["sudo", "apt-get", "-y", "install", "libatlas-base-dev"])
	subprocess.call (["sudo", "pip3", "--default-timeout=100", "install", "tensorflow==1.15.5"])
	subprocess.call (["sudo", "pip3", "--default-timeout=100", "install", "keras==2.3.1"])
	subprocess.call (["sudo", "apt-get", "-y", "install", "libatlas-base-dev"])
	subprocess.call (["sudo", "git", "clone", "https://github.com/fchollet/deep-learning-models.git"])
	subprocess.call (["wget", "-P", "/home/pi/deep-learning-models", "https://github.com/masashis2021PBL/Eng-2021-PBL-ML/raw/main/elephant.jpg"])


########## main () ##########
install_packages ()
