#! /usr/binn/python3 -B
# -*- config: utf-8 -*-

import sys
import os
import subprocess
import config

def install_packages ():
	config.logger.info ("Update packages")
	subprocess.call (["sudo", "apt-get", "-y", "update"])

	config.logger.info ("Install packages")
	subprocess.call (["sudo", "apt-get", "-y", "install", "python3-pip"])
	subprocess.call (["sudo", "pip3", "install", "--upgrade", "setuptools"])
	subprocess.call (["sudo", "pip3", "install", "--upgrade", "pip"])
	subprocess.call (["sudo", "pip3", "install", "rpi.gpio"])
	subprocess.call (["sudo", "pip3", "install", "pyserial"])
	subprocess.call (["sudo", "pip3", "install", "ntpdate"])
	subprocess.call (["sudo", "pip3", "install", "git-core"])
	subprocess.call (["sudo", "pip3", "install", "i2c-tools"])
	subprocess.call (["sudo", "pip3", "install", "libi2c-dev"])
	subprocess.call (["sudo", "pip3", "install", "subversion"])
	subprocess.call (["sudo", "pip3", "install", "python-smbus"])

	config.logger.info ("Install deep-learning packages")
	subprocess.call (["sudo", "apt-get", "install", "libatlas-base-dev"])
	subprocess.call (["sudo", "pip3", "--default-timeout=100", "install", "tensorflow"])
	subprocess.call (["sudo", "pip3", "--default-timeout=100", "install", "keras"])
	subprocess.call (["sudo", "apt-get", "install", "libatlas-base-dev"])
	subprocess.call (["sudo", "git", "clone", "https://github.com/fchollet/deep-learning-models.git"])


########## main () ##########
install_packages ()
