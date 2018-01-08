# Light Armoured Recon
**Light Armoured Recon** is a python script designed to automate passive reconnaissance. It automates execution of *TheHarvester*, *whois*, *Robtex.com*, *Builtwith.com*, *DNSrecon*, *metagoofil*, & *knockpy*.
# Installing
## Prerequisites
 - Python 2.7
 - TheHarvester (https://code.google.com/p/theharvester/)
 - whois (https://github.com/rfc1036/whois)
 - DNSrecon (https://github.com/darkoperator/dnsrecon)
 - metagoofil (www.edge-security.com/metagoofil.php)
 - knockpy (https://github.com/guelfoweb/knock)
## Dependencies
 - subprocess
## Installation 

    $ git clone https://github.com/west-wind/LAR.git
    $ cd LAR
    $ ./dependency_installer.sh
    $ python LAR.py
# Getting Started
Usage of **Light Armoured Recon** for sending any traffic to a target without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developer assume no liability and are not responsible for any misuse or damage caused by this program. 

This script requires the user to input the target URL *(excluding www)* by selecting option 1 & the output filename by selecting option 2. Make sure the filename is unique, so as not to overwrite any existing files in the directory.

To begin

    $ cd LAR
    $ python LAR.py

Enter target URL by selecting option 1.

Enter output filename by selecting option 2. Make sure that no other file with the same name exists in the same directory, so as to avoid overwriting any existing files.

Select option 3 to proceed with recon.

Enter 'EXECUTE' to commence execution of packages.

## Customisation
You can customise the execution of each package by editing command specific parameters in **LAR. py**

For example, if you're only interested in downloading **pdf** files with metagoofil, you can do so by editing the filetype parameter.

from

    cmd = 'metagoofil -d ' + target + ' -t pdf,doc,xls,ppt,odp,ods,docx,xlsx,pptx -l 10 -n 1 -o metagoofil_downloads -f metagoofil_output.html'
 to
 
    cmd = 'metagoofil -d ' + target + ' -t pdf -l 10 -n 1 -o metagoofil_downloads -f metagoofil_output.html' 

# Built With
Python
# Authors
Alex John, B. ([@Praetorian_GRD](https://twitter.com/Praetorian_GRD))
# License
Copyright (C) 2018 Alex John, B. This project is licensed under the GNU License - see the [LICENSE.md](https://github.com/west-wind/LAR/LICENSE.md) file for details.
# Acknowledgements
[Joe Perry](https://www.cybrary.it/members/perry/) & [Cybrary](https://www.cybrary.it) for the awesome ‘[Python for Security Professionals](https://www.cybrary.it/course/python/)’ course.