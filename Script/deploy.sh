#!/bin/bash



if [! -e BDD_Intermédiaire.sql]
then {
    echo "Le fichier BDD_Intermediaire est introuvable !!";
    exit 1;
}
if [! -e BDD_Intermédiaire.sql]
then {
    echo "Le fichier BDD_Intermediaire est introuvable !!";
    exit 1;
}


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

# create random password
#PASSWDDB="$(openssl rand -base64 12)"
PASSWDDB="";

# replace "-" with "_" for database username
MAINDB="TwindevUser"

# If /root/.my.cnf exists then it won't ask for root password
if [ -f /root/.my.cnf ]; then

    mysql -e "CREATE USER ${MAINDB}@localhost IDENTIFIED BY '${PASSWDDB}';"
    mysql -e "GRANT ALL PRIVILEGES ON ${MAINDB}.* TO '${MAINDB}'@'localhost';"
    mysql -e "FLUSH PRIVILEGES;"

# If /root/.my.cnf doesn't exist then it'll ask for root password   
else
    echo "Please enter root user MySQL password!"
    read rootpasswd
    mysql -uroot -p${rootpasswd} -e "CREATE USER ${MAINDB}@localhost IDENTIFIED BY '${PASSWDDB}';"
    mysql -uroot -p${rootpasswd} -e "GRANT ALL PRIVILEGES ON ${MAINDB}.* TO '${MAINDB}'@'localhost';"
    mysql -uroot -p${rootpasswd} -e "FLUSH PRIVILEGES;"
fi

mysql -u ${MAINDB} -p  ${MAINDB} < db.sql

