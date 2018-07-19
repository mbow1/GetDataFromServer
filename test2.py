import mysql.connector
################################### Connection DDB BDF ###################################

cnx = mysql.connector.connect(user='test',
                                password='',
                                host='localhost',
                                database='BDD_INTER')
curBDD_INTER = cnx.cursor()

################################### Connection DDB BDF ###################################


################################### Ajout des donnees ###################################
data_M = []
data_M.append(str(25))
data_M.append(str(45))
data_M.append(str(6))
data_M.append(str(3))
data_M.append(str(3))
data_M.append(str(3))
data_M.append(str(7))
data_M.append(str(25))
data_M.append(str(78))
data_M.append(str(2.6))



Data_Meteo = {
    'VitesseVent':  data_M[0],
    'DirectionVent':data_M[1],
    'Pression':     data_M[2],
    'Humidite':     data_M[3],
    'PointRosee':   data_M[4],
    'Pyra_N':       data_M[5],
    'Pyra_E':       data_M[6],
    'Pyra_S':       data_M[7],
    'Pyra_O':       data_M[8],
    'Temperature':  data_M[9],
}
Data_Fenetre = {
    'EtatFenetre' : 0,
    'NumeroFenetre' : 3,
    'Locales_idLocal': 4,
 }
################################### Ajout des donnees ###################################
codeSql = []
codeSql.append("INSERT INTO DataMeteos (TimeStamp,VitesseVent,DirectionVent,Pression,Humidite,PointRosee,Pyra_N,Pyra_E,Pyra_S,Pyra_O,Temperature) VALUES (CURRENT_TIMESTAMP(),%(VitesseVent)s,%(DirectionVent)s,%(Pression)s,%(Humidite)s,%(PointRosee)s,%(Pyra_N)s,%(Pyra_E)s,%(Pyra_S)s,%(Pyra_O)s,%(Temperature)s)")
codeSql.append("INSERT INTO `BDD_INTER`.`EvenFenetre`(`TimeStamp`,`EtatFenetre`,`NumeroFenetre`,`Locales_idLocal`) VALUES (CURRENT_TIMESTAMP(),%(EtatFenetre)s,%(NumeroFenetre)s,%(Locales_idLocal)s);")
try:
    curBDD_INTER.execute(codeSql[0],Data_Meteo)
    cnx.commit()
except:
    cnx.rollback

cnx.close()


