# A python script to automate execution of TheHarvester, whois, robtex.com, builtwith.com, DNSrecon, metagoofil, & knockpy during an authorized penetration test; & saves the result to a .TXT file
#
# Copyright (C) 2018 Alex John, B.
#
#
# Light Armoured Recon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Light Armoured Recon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details <http://www.gnu.org/licenses/>.

try:
	from subprocess import *
	import os
	import sys
	import subprocess
except ImportError:
	print "\nImport Error! Update Kali & check for prerequisities in README"

fileObject = ''
fileName = ''
target = ''

# INFORMATION       =====================================================================================================================================
NAME		= "Light Armoured Recon Script v1.0"
AUTHOR		= "Alex John, B."
TWITTER		= "@Praetorian_GRD"
GITHUB		= "Github https://github.com/west-wind/LAR"

# TARGET DEFINITION =====================================================================================================================================
def acquireTarget():
	global target
	os.system('clear')
	target = str(raw_input("Enter target URL (exclude www): "))
	print ('\x1b[1;32m' + '\n[OK]\t' + '\x1b[0m' + 'Target Acquired')

# THE HARVESTER     =====================================================================================================================================
def harvester():
	os.system('clear')
	print "\n[*]\tRunning TheHarvester"
	print "[*]\tStep 1/6 in progress"
	global target
	global fileObject
	cmd = 'theharvester -d ' + target + ' -b all'
	try:
		output = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
		out, err = output.communicate()
		if(output.returncode != 0):
			print ('\x1b[1;31m' + '[ERROR]\t' + '\x1b[0m' + 'Step 1 Failed! Check/Update prerequisitie packages. \nError: ' + err.rstrip())
			#fileObject.close()
			sys.exit(1)
		else:
		    #print "Return code: ", output.returncode
		    #print out.rstrip(),err.rstrip()
		    fileObject.write('\nThe Harvester Output: \n')
		    fileObject.write('=========================================================================\n')
		    fileObject.write(str(out.rstrip()))
		    print ('\x1b[1;32m' + '[OK]\t' + '\x1b[0m' + 'Step 1 Executed\n')
	except:
		print "Something went wrong! Check prerequisities.\n"
		sys.exit(1)
	return 0

# WHOIS             =====================================================================================================================================
def whois():
	print "\n[*]\tRunning whois"
	print "[*]\tStep 2/6 in progress"
	global target
	global fileObject
	cmd = 'whois' + ' ' + target
	try:
		output = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
		out, err = output.communicate()
		if(output.returncode != 0):
			print ('\x1b[1;31m' + '[ERROR]\t' + '\x1b[0m' + 'Step 2 Failed! Check/Update prerequisitie packages. \nError: ' + err.rstrip())
			fileObject.close()
			sys.exit(1)
		else:
			#print "Return code: ", output.returncode
			#print out.rstrip(),err.rstrip()
			fileObject.write('\n\nWhois Output: \n')
			fileObject.write('=========================================================================\n')
			fileObject.write(str(out.rstrip()))
			print ('\x1b[1;32m' + '[OK]\t' + '\x1b[0m' + 'Step 2 Executed\n')
	except:
		print "Something went wrong! Check prerequisities.\n"
		sys.exit(1)
	return 0

# BUILTWITH         =====================================================================================================================================
def webtechnology():
	print "\n[*]\tConnecting to Robtex.com & Builtwith.com"
	print "[*]\tStep 3/6 in progress"
	cmmd = 'curl -o ' + target + '_robtex_scan.html' + ' https://www.robtex.com/dns-lookup/' + target
	cmd = 'curl -o ' + target +'_builtwith_scan.html' + ' https://builtwith.com/' + target
	outPut = Popen(cmmd, shell=True, stdout=PIPE, stderr=PIPE)
	output = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
	out, err = output.communicate()
	out, err = outPut.communicate()
	try:
		if(output.returncode != 0):
			print ('\x1b[1;31m' + '[ERROR]\t' + '\x1b[0m' + 'Step 3 Failed! Check/Update prerequisitie packages. \nError: ' + err.rstrip())
			fileObject.close()
			sys.exit(1)
		else:
			#print "Return code: ", output.returncode
			#print out.rstrip(),err.rstrip()
			#print result
			print ('\x1b[1;32m' + '[OK]\t' + '\x1b[0m' + 'Step 3 Executed\n')
	except:
		print "Something went wrong! Check prerequisities.\n"
		sys.exit(1)
	return 0

# DNS RECON         =====================================================================================================================================
def dnslookup():
	print "\n[*]\tRunning DNSrecon"
	print "[*]\tStep 4/6 in progress"
	global target
	global fileObject
	cmd = 'dnsrecon -d' + ' ' + target
	output = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
	out, err = output.communicate()
	try:
		if(output.returncode != 0):
			print ('\x1b[1;31m' + '[ERROR]\t' + '\x1b[0m' + 'Step 4 Failed Check/Update prerequisitie packages. \nError: ' + err.rstrip())
			fileObject.close()
			sys.exit(1)
		else:
			#print "Return code: ", output.returncode
			#print out.rstrip(),err.rstrip()
			fileObject.write('\nDNS Recon Output: \n')
			fileObject.write('=========================================================================\n')
			fileObject.write(str(out.rstrip()))
			print ('\x1b[1;32m' + '[OK]\t' + '\x1b[0m' + 'Step 4 Executed\n')
	except:
		print "Something went wrong! Check prerequisities.\n"
		sys.exit(1)
	return 0

# METAGOOFIL         =====================================================================================================================================
def metagoofil():
	print "\n[*]\tRunning metagoofil"
	print "[*]\tStep 5/6 in progress"
	global target
	global fileObject
	cmd = 'metagoofil -d ' + target + ' -t pdf,doc,xls,ppt,odp,ods,docx,xlsx,pptx -l 10 -n 1 -o metagoofil_downloads -f metagoofil_output.html' 
	output = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
	out, err = output.communicate()
	try:
		if(output.returncode != 0):
			print ('\x1b[1;31m' + '[ERROR]\t' + '\x1b[0m' + 'Step 5 Failed! Check/Update prerequisitie packages. \nError: ' + err.rstrip())
			fileObject.close()
			sys.exit(1)
		else:
			#print "Return code: ", output.returncode
			#print out.rstrip(),err.rstrip()
			fileObject.write('\nMetagoofil Output: \n')
			fileObject.write('=========================================================================\n')
			fileObject.write(str(out.rstrip()))
			print ('\x1b[1;32m' + '[OK]\t' + '\x1b[0m' + 'Step 5 Executed\n')
	except:
		print "Something went wrong! Check prerequisities.\n"
		sys.exit(1)
	return 0

# KNOCKPY           =====================================================================================================================================
def knockDomain():
	print "\n[*]\tRunning knockpy. This step can take ~15 mins. to complete."
	print "[*]\tStep 6/6 in progress"
	global target
	global fileObject, GITHUB, fileName
	cmd = 'knockpy ' + target 
	output = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
	out, err = output.communicate()
	try:
		if(output.returncode != 0):
			print ('\x1b[1;31m' + '[ERROR]\t' + '\x1b[0m' + 'Step 6 Failed! Check/Update prerequisitie packages. \nError: ' + err.rstrip())
			fileObject.close()
			sys.exit(1)
		else:
			#print "Return code: ", output.returncode
			#print out.rstrip(),err.rstrip()
			fileObject.write('\nKnockpy Subdomain Scan Output: \n')
			fileObject.write('=========================================================================\n')
			fileObject.write(str(out.rstrip()))
			print ('\x1b[1;32m' + '[OK]\t' + '\x1b[0m' + 'Results have been saved to %s '%fileName)
			print ('\x1b[1;32m' + '[OK]\t' + '\x1b[0m' + 'Step 6 Executed\n' + '\x1b[1;32m' + '[OK]\t' + '\x1b[0m' + 'Mission Over')
			print "\nThank you for using %s" %NAME 
			print "For suggestions %s" %TWITTER
			print "To contribute, visit %s\n" %GITHUB
			fileObject.close()
	except:
		print "Something went wrong! Check prerequisities.\n"
		sys.exit(1)
	return 0

# INFORMATION           =====================================================================================================================================
def info():
	global target
	global fileObject, GITHUB
	os.system('clear')
	cmd = 'cat README.txt' 
	output = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
	out, err = output.communicate()
	try:
		if(output.returncode != 0):
			print ('\x1b[1;31m' + '[ERROR]\t' + '\x1b[0m' + 'README.txt missing. You can download it by visiting %s \n'%GITHUB + err.rstrip())
			sys.exit(1)
		else:
			#print "Return code: ", output.returncode
			print out.rstrip()
	except:
		sys.exit(1)
	return 0

#============ MAIN ==============================
def main():
	global fileObject
	global target
	global fileName
	print "------------------------------------------------------------"
	print ('\x1b[1;31m' + '\n\t\t\   LIGHT ARMOURED RECON   /' + '\x1b[0m')
	print ('\x1b[1;31m' + '\t\t \    TIP OF THE SPEAR    /' + '\x1b[0m')
	print ('\x1b[1;34m' + '\nLight Armoured Recon Script' + '\x1b[0m')
	print ('\x1b[1;34m' + 'Alex John, B.' + '\x1b[0m')
	print ('\x1b[1;34m' + '@Praetorian_GRD' + '\x1b[0m')
	print "------------------------------------------------------------"
	try:
		while True:
			print "\n------------------------------------------------------------"
			print "1.\tEnter Target Information"
			print "2.\tCreate Output File"
			print "3.\tInitiate Recon"
			print "4.\tREADME"
			print "------------------------------------------------------------"
			if (target == ''):
				print ('\x1b[1;31m' + '\n[!]\t' + '\x1b[0m' + 'Target missing. Select 1 to enter target URL')
			else:
				print ('\x1b[1;32m' + '\n[OK]\t' + '\x1b[0m' + 'Scope: %s' %target)
				
			if (fileObject == ''):
				print ('\x1b[1;31m' + '[!]\t' + '\x1b[0m' + 'Select 2 to enter output file name')
			option = int(raw_input("\nEnter your option or Press Ctrl+C to exit: "))
			if(option == 1):
				acquireTarget()
			elif(option == 3):
				if(target == '' or fileObject == ''):
					print ('\x1b[1;31m' + '[!]\t' + '\x1b[0m' + 'Target or Filename missing!')
				else:
					os.system('clear')
					print ('\x1b[1;31m' + '\nNOTICE:' + '\x1b[0m')
					print "\nType 'EXECUTE' only if you've authorisation from the owner of %s to perform active/passive reconnaisance on %s. Typing EXECUTE will initiate a series of scans againsts %s which might be illegal without prior written authorisation from %s's owner!" %(target, target, target, target)
					print "\nUsage of Light Armoured Recon for sending any traffic to a target without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program."
					print ('\n\t\t(' + '\x1b[1;31m' + ' EXECUTE ' + '\x1b[0m' + '|' + '\x1b[1;34m' + ' NO ' + '\x1b[0m' + ')')
					authorisation = str(raw_input("\nWaiting for input: "))
					if(authorisation == 'EXECUTE' or authorisation == 'execute'):
						print "\nCommencing Recon . ...."
						harvester()
						whois()
						webtechnology()
						dnslookup()
						metagoofil()
						knockDomain()
						os._exit(0)
					else:
						print "\nThank you for using %s" %NAME 
						print "For suggestions %s" %TWITTER
						print "To contribute, visit %s\n" %GITHUB
						sys.exit(0)
			elif(option == 2):
				os.system('clear')
				fileName = str(raw_input("Enter output filename: "))
				fileName += '.txt'
				fileObject = open(fileName,"w+")
				print "[OK]\t%s created." %(fileName)
			elif(option == 4):
				os.system('clear')
				info()
			else:
				os.system('clear')
				print ('\x1b[1;31m' + '\nInvalid option!\n' + '\x1b[0m')
	except KeyboardInterrupt:
		sys.exit(0)
main()