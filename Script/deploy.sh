#!/bin/bash

sudo apt-get update;
sudo apt-get install python -y;
sudo apt-get install mysql-server -y;
sudo apt-get install python3-mysql.connector -y;
mkdir /opt/TwindevFiles;
mkdir /opt/TwindevFiles/Sript/;
cp *.py /opt/TwindevFiles/Sript/;

crontab -l > mycron

#echo new cron into cron file
echo "* 1 * * * python /opt/TwindevFiles/Sript/ScriptTemperature.py" >> mycron
echo "* 1 * * * python /opt/TwindevFiles/Sript/ScriptWeather.py" >> mycron
echo "* * * * * (sleep 30 ;python /opt/TwindevFiles/Sript/ScriptWindows.py)" >> mycron
echo "* * * * * (sleep 30 ;python /opt/TwindevFiles/Sript/ScriptLuminary.py)" >> mycron

#install new cron file
crontab mycron
rm mycron

#echo "SELECT * FROM Locales" | mysql --user=test BDD_INTER