Light Armoured Recon 
Light Armoured Recon is a python script designed to automate execution of various tools used during target reconnaissance. It automates execution of theharvester, whois, Robtex.com, Builtwith.com, DNSrecon, metagoofil, & knockpy.

Installing
Prerequisites
 • Python 2.7
 • theharvester (https://code.google.com/p/theharvester/)
 • whois (https://github.com/rfc1036/whois)
 • DNSrecon (https://github.com/darkoperator/dnsrecon)
 • metagoofil (www.edge-security.com/metagoofil.php)
 • knockpy (https://github.com/guelfoweb/knock)

Dependencies
 • subprocess

Installing
  $ git clone https://github.com/west-wind/LAR.git
  $ cd LAR
  $ ./dependency_installer.sh
  $ python LAR.py

Getting Started
Usage of Light Armoured Recon for sending any traffic to a target without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developer assume no liability and are not responsible for any misuse or damage caused by this program. 

This script requires the user to input the target URL (excluding www) by selecting option 1 & the output filename by selecting option 2. Make sure the filename is unique, so as not to overwrite any existing files in the directory.

Built With
Python

Authors
Alex John, B. (@Praetorian_GRD)

License
Copyright (C) 2018 Alex John, B. This project is licensed under the GNU License - see the LICENSE.md file for details
