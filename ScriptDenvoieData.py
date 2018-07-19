import mysql.connector

################################### Connection DDB BDF ###################################
dbconBDF  = mysql.connector.connect(user='ssegard',
                                    password='cesi',
                                    host='10.192.12.5',
                                    database='TEST')
curBDF = dbconBDF.cursor()
################################### Connection DDB BDF ###################################

################################### Requete SQL ###################################
codeSql = []
codeSql.append("SELECT Tesla_F1,Tesla_F2,Tesla_F3,Tesla_F4,HallRdc_F1,HallRdc_F2,Lumiere_F1,Lumiere_F2,Lumiere_F3,Nobel_F1,Nobel_F2,Nobel_F3,HallPalier_F1,HallPalier_F2,HallPalier_F3,Turing_F1,Turing_F2,Turing_F3 FROM TEST.FenetreEvents order by TimeStamp DESC limit 1;")
codeSql.append("SELECT TimeStamp,VitesseVent,DirectionVent,Pression,Humidite,PointRosee,Pyra_N,Pyra_E,Pyra_S,Pyra_O,Luxmetre,Temperature FROM TEST.MeteoHour order by TimeStamp DESC limit 1;")
codeSql.append("SELECT tempLumiere,hydroLumiere,tempTuring,hydroTuring,tempNobel,hydroNobel,tempTesla,hydroTesla FROM TEST.Temp2 order by TimeStamp DESC limit 1;")
################################### Requete SQL ###################################


################################### code de recuperation ###################################
def getInformation(codeSql):
      curBDF.execute(codeSql)
      resultat = curBDF.fetchall()
      resultat = resultat[0]
      return resultat
      del resultat
      dbconBDF.close()

################################### code de recuperation ###################################

print getInformation(codeSql[2])

################################### code insertion ###################################
#def setInformation(data,codeSql)
      

################################### code insertion ###################################