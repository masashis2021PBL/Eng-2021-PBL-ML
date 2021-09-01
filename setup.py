#! /usr/binn/python3 -B
# -*- config: utf-8 -*-

import sys
import os
import subprocess
import config

def install_packages ():
	config.logger.info ("Update packages")
	subprocess.call (["apt-get", "-y", "update"])

	config.logger.info ("Install packages")
	subprocess.call (["apt-get", "-y", "install", "python3-pip"])
	subprocess.call (["pip3", "install", "--upgrade", "setuptools"])
	subprocess.call (["pip3", "install", "--upgrade", "pip"])
	subprocess.call (["pip3", "install", "rpi.gpio"])
	subprocess.call (["pip3", "install", "pyserial"])
	subprocess.call (["pip3", "install", "ntpdate"])
	subprocess.call (["pip3", "install", "git-core"])
	subprocess.call (["pip3", "install", "i2c-tools"])
	subprocess.call (["pip3", "install", "libi2c-dev"])
	subprocess.call (["pip3", "install", "python-smbus"])



########## main () ##########
install_packages ()
