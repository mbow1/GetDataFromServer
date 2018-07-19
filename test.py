import mysql.connector

################################### Connection DDB BDF ###################################
dbcon = mysql.connector.connect(user='ssegard',password='cesi',host='10.192.12.5', database='TEST')
cur = dbcon.cursor()
################################### Connection DDB BDF ###################################



######################################## les fenetres ##############################################
cur.execute("SELECT * FROM TEST.FenetreEvents  order by TimeStamp DESC limit 24;")


for (idFenetreEvents, TimeStamp, Tesla_F1, Tesla_F2, Tesla_F3, Tesla_F4, HallRdc_F1, HallRdc_F2, Lumiere_F1, Lumiere_F2, Lumiere_F3, Nobel_F1, Nobel_F2, Nobel_F3, HallPalier_F1, HallPalier_F2, HallPalier_F3, Turing_F1, Turing_F2, Turing_F3) in cur:
      print("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(idFenetreEvents, TimeStamp, Tesla_F1, Tesla_F2, Tesla_F3, Tesla_F4, HallRdc_F1, HallRdc_F2, Lumiere_F1, Lumiere_F2, Lumiere_F3, Nobel_F1, Nobel_F2, Nobel_F3, HallPalier_F1, HallPalier_F2, HallPalier_F3, Turing_F1, Turing_F2, Turing_F3))



######################################## les fenetres ##############################################







dbcon.close()