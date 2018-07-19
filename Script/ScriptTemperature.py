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
codeSql.append("INSERT INTO `BDD_INTER`.`Temperature`(`TimeStamp`,`Temperature`,`Hygro`,`Locales_idLocal`) VALUES (CURRENT_TIMESTAMP(),%(Temperature)s,%(Hygro)s,%(Locales_idLocal)s);")
################################### Requete SQL ###################################


################################### code de recuperation ###################################
def getInformation(codeSql):
      curBDF.execute(codeSql)
      resultat = curBDF.fetchall()
      resultat = resultat[0]
      return resultat
      del resultat
     


def setInformation(codeSql,Data):
    try:
        curBDD_INTER.execute(codeSql,Data)
        cnx.commit()
    except:
        cnx.rollback

################################### code de recuperation ###################################

################################### Ajout des donnees ###################################

Data = ({
    #lumiere
    'Temperature' :     getInformation(codeSql[0])[0],
    'Hygro' :           getInformation(codeSql[0])[1],
    'Locales_idLocal' : 3
},{
    #Turing
    'Temperature':      getInformation(codeSql[0])[2],
    'Hygro':            getInformation(codeSql[0])[3],
    'Locales_idLocal' : 2
},{
    #Nobel
    'Temperature':      getInformation(codeSql[0])[4],
    'Hygro':            getInformation(codeSql[0])[5],
    'Locales_idLocal' : 4
},{
    #Teslab
    'Temperature':      getInformation(codeSql[0])[6],
    'Hygro':            getInformation(codeSql[0])[7],
    'Locales_idLocal' : 1
})

################################### Ajout des donnees ###################################

#SELECT * FROM BDD_INTER.Temperature INNER JOIN Locales ON Temperature.Locales_idLocal = Locales.idLocal;

################################### code insertion ###################################

setInformation(codeSql[1],Data[0])
setInformation(codeSql[1],Data[1])
setInformation(codeSql[1],Data[2])
setInformation(codeSql[1],Data[3])

################################### code insertion ###################################

################################### Fermeture des BDD ###################################
dbconBDF.close()
cnx.close()
################################### Fermeture des BDD ###################################