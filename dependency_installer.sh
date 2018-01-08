#!/bin/bash
echo "Step 1/6: Running apt-get update"
apt-get update
echo ""
echo "Installing packages"
echo "Step 2/6: Checking/Installing Theharvester"
apt install theharvester
echo ""
echo "Step 3/6: Checking/Installing Whois"
apt install whois
echo ""
echo "Step 4/6: Checking/Installing DNSrecom"
apt install dnsrecon
echo ""
echo "Step 5/6: Checking/Installing Metagoofil"
apt install metagoofil
echo ""
echo "Step 6/6: Checking/Installing Knockpy"
apt install knockpy
echo ""
echo "Done"
