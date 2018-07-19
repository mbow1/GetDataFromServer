#Ti = 3600s

import mysql.connector

################################### Connection DDB BDF ###################################
dbconBDF  = mysql.connector.connect(user='ssegard',
                                    password='cesi',
                                    host='10.192.12.5',
                                    database='TEST')
curBDF = dbconBDF.cursor()
################################### Connection DDB BDF ###################################



################################### Connection DDB BDF ###################################

cnx = mysql.connector.connect(user='test',
                                password='',
                                host='localhost',
                                database='BDD_INTER')
curBDD_INTER = cnx.cursor()

################################### Connection DDB BDF ###################################



################################### Requete SQL ###################################
codeSql = []
codeSql.append("SELECT VitesseVent,DirectionVent,Pression,Humidite,PointRosee,Pyra_N,Pyra_E,Pyra_S,Pyra_O,Luxmetre,Temperature FROM TEST.MeteoHour order by TimeStamp DESC limit 1;")
codeSql.append("INSERT INTO DataMeteos (TimeStamp,VitesseVent,DirectionVent,Pression,Humidite,PointRosee,Pyra_N,Pyra_E,Pyra_S,Pyra_O,Luxmetre,Temperature) VALUES (CURRENT_TIMESTAMP(),%(VitesseVent)s,%(DirectionVent)s,%(Pression)s,%(Humidite)s,%(PointRosee)s,%(Pyra_N)s,%(Pyra_E)s,%(Pyra_S)s,%(Pyra_O)s,%(Luxmetre)s,%(Temperature)s)")
################################### Requete SQL ###################################


################################### code de recuperation ###################################
def getInformation(codeSql):
      curBDF.execute(codeSql)
      resultat = curBDF.fetchall()
      resultat = resultat[0]
      return resultat
      del resultat
      dbconBDF.close()


def setInformation(codeSql,Data_Meteo):
    try:
        curBDD_INTER.execute(codeSql,Data_Meteo)
        cnx.commit()
    except:
        cnx.rollback
    cnx.close()
################################### code de recuperation ###################################

################################### Ajout des donnees ###################################

Data_Meteo = {
    'VitesseVent':  getInformation(codeSql[0])[0],
    'DirectionVent':getInformation(codeSql[0])[1],
    'Pression':     getInformation(codeSql[0])[2],
    'Humidite':     getInformation(codeSql[0])[3],
    'PointRosee':   getInformation(codeSql[0])[4],
    'Pyra_N':       getInformation(codeSql[0])[5],
    'Pyra_E':       getInformation(codeSql[0])[6],
    'Pyra_S':       getInformation(codeSql[0])[7],
    'Pyra_O':       getInformation(codeSql[0])[8],
    'Luxmetre':     getInformation(codeSql[0])[9],
    'Temperature':  getInformation(codeSql[0])[10],
}

################################### Ajout des donnees ###################################


################################### code insertion ###################################

setInformation(codeSql[1],Data_Meteo)

################################### code insertion ###################################