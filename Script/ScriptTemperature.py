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
codeSql.append("SELECT tempLumiere,hydroLumiere,tempTuring,hydroTuring,tempNobel,hydroNobel,tempTesla,hydroTesla FROM TEST.Temp2 order by TimeStamp DESC limit 1;")
codeSql.append("INSERT INTO `BDD_INTER`.`Temperature`(`Temperature`,`Hygro`,`Locales_idLocal`) VALUES (%(Temperature)s,%(Hygro)s,%(Locales_idLocal)s);")
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

Data_Meteo = []{
    #lumiere
    'Temperature' : ,
    'Hygro' : ,
},{
    #Turing
    'Temperature': ,
    'Hygro': ,
},{
    #Nobel
    'Temperature': ,
    'Hygro': ,
},{
    #Tesla
    'Temperature': ,
    'Hygro': ,
}

################################### Ajout des donnees ###################################


################################### code insertion ###################################

setInformation(codeSql[1],Data_Meteo)

################################### code insertion ###################################