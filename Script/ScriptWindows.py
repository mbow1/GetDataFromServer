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
codeSql.append("SELECT Tesla_F1,Tesla_F2,Tesla_F3,Tesla_F4,HallRdc_F1,HallRdc_F2,Lumiere_F1,Lumiere_F2,Lumiere_F3,Nobel_F1,Nobel_F2,Nobel_F3,HallPalier_F1,HallPalier_F2,HallPalier_F3,Turing_F1,Turing_F2,Turing_F3 FROM TEST.FenetreEvents order by TimeStamp DESC limit 1;")
codeSql.append("INSERT INTO `BDD_INTER`.`EvenFenetre`(`TimeStamp`,`EtatFenetre`,`NumeroFenetre`,`Locales_idLocal`) VALUES (CURRENT_TIMESTAMP(),%(EtatFenetre)s,%(NumeroFenetre)s,%(Locales_idLocal)s);")

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
    #Tesla
    'EtatFenetre'     : getInformation(codeSql[0])[0],
    'NumeroFenetre'  :  11,
    'Locales_idLocal':  1,
},{
    'EtatFenetre'     : getInformation(codeSql[0])[1],
    'NumeroFenetre'  :  12,
    'Locales_idLocal':  1,

},{
    'EtatFenetre'     : getInformation(codeSql[0])[2],
    'NumeroFenetre'  :  13,
    'Locales_idLocal':  1,
},{
    'EtatFenetre'     : getInformation(codeSql[0])[3],
    'NumeroFenetre'  :  14,
    'Locales_idLocal':  1,
},{
    #Hall
    'EtatFenetre'    :  getInformation(codeSql[0])[4],
    'NumeroFenetre'  :  51,
    'Locales_idLocal':  5,
},{
    'EtatFenetre'    :  getInformation(codeSql[0])[5],
    'NumeroFenetre'  :  52,
    'Locales_idLocal':  5,
},{
    'EtatFenetre'    :  getInformation(codeSql[0])[6],
    'NumeroFenetre'  :  53,
    'Locales_idLocal':  5,
},{
    'EtatFenetre'    :  getInformation(codeSql[0])[7],
    'NumeroFenetre'  :  54,
    'Locales_idLocal':  5,
},{
    'EtatFenetre'    :  getInformation(codeSql[0])[8],
    'NumeroFenetre'  :  55,
    'Locales_idLocal':  5,
},{
    #Lumiere
    'EtatFenetre'    :  getInformation(codeSql[0])[9],
    'NumeroFenetre'  :  31,
    'Locales_idLocal':  3,
},{
    'EtatFenetre'    :  getInformation(codeSql[0])[10],
    'NumeroFenetre'  :  32,
    'Locales_idLocal':  3,
},{
    'EtatFenetre'    :  getInformation(codeSql[0])[11],
    'NumeroFenetre'  :  33,
    'Locales_idLocal':  3,
},{
    'EtatFenetre'    :  getInformation(codeSql[0])[12],
    'NumeroFenetre'  :  34,
    'Locales_idLocal':  3,
},{
    'EtatFenetre'    :  getInformation(codeSql[0])[13],
    'NumeroFenetre'  :  35,
    'Locales_idLocal':  3,
},{
    'EtatFenetre'    :  getInformation(codeSql[0])[14],
    'NumeroFenetre'  :  36,
    'Locales_idLocal':  3,
},{
    #Turing
    'EtatFenetre'    :  getInformation(codeSql[0])[15],
    'NumeroFenetre'  :  21,
    'Locales_idLocal':  2,
},{
    'EtatFenetre'    :  getInformation(codeSql[0])[16],
    'NumeroFenetre'  :  22,
    'Locales_idLocal':  2,
},{
    'EtatFenetre'    :  getInformation(codeSql[0])[17],
    'NumeroFenetre'  :  23,
    'Locales_idLocal':  2,
})

################################### Ajout des donnees ###################################

#SELECT * FROM BDD_INTER.EvenFenetre INNER JOIN Locales ON EvenFenetre.Locales_idLocal = Locales.idLocal order by TimeStamp DESC;

################################### code insertion ###################################

for i in range(0, len(Data)):
    setInformation(codeSql[1],Data[i])

################################### code insertion ###################################

################################### Fermeture des BDD ###################################
dbconBDF.close()
cnx.close()
################################### Fermeture des BDD ###################################