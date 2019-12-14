# Database connection
import mysql.connector
from mysql.connector import Error

hostname="localhost"
databasename="lesrooster"
gebruiker="root"
wachtwoord=""

connection = mysql.connector.connect(host=hostname,
                                     database=databasename,
                                     user=gebruiker,
                                     password=wachtwoord)

# insert data
def toevoegen(vak, lesuur, dag, tijd, lokaal):
    sQuery = "INSERT INTO lesrooster VALUES(0,'"+vak+"', '"+lesuur+"', '"+dag+"', '"+tijd+"', '"+lokaal+"')"
    cursor = connection.cursor()
    cursor.execute(sQuery)
    connection.commit()

# select data
def ophalen():
    sQuery = "SELECT * FROM lesrooster ORDER BY dag ASC, lesuur ASC"
    cursor = connection.cursor()
    cursor.execute(sQuery)
    records=cursor.fetchall()
    tempDag = ""

    for rij in records:
        if(tempDag != rij[3]):
             tempDag = rij[3]
             print("")
             print(rij[3],"\n""Tijd:", rij[4],"Vak:", rij[1],"Lokaal:", rij[5])
        else:
             print("Tijd:", rij[4],"Vak:", rij[1],"Lokaal:", rij[5])
# back to menu 
def terug():
    terug = input("Wilt u terug naar menu? (j/n)")
    if(terug == "j"):
        menu()
    else:
        print("Tot ziens!")

# menu
def menu():
    
    print('''(1) Les toevoegen
(2) Rooster opvragen
(3) Afsluiten
''')
    keuze=input("Uw keuze: ")
 
    if (keuze == "1"):
        lesToevoegen()
    elif (keuze == "2"):
        opvragen()
    elif (keuze == "3"):
        afsluiten()

# insert rooster
def lesToevoegen():
    print("Les toevoegen")
    vak = input("Vak: ")
    lesuur = input("Lesuur: ")
    dag = input("Dag: ")
    tijd = input("Tijd: ")
    lokaal = input("Lokaal: ")
    
    print("Vak: "+vak+", Lesuur: "+lesuur+", Dag: "+dag+", Tijd: "+tijd+", Lokaal: "+ lokaal)
    toevoegen(vak, lesuur, dag, tijd, lokaal)
    print("")
    meer = input("Wilt u nog iets toevoegen? (j/n)")
    if(meer == "j"):
        lesToevoegen()
    else:
        print("")
        terug()

# show rooster
def opvragen():
    print("Uw rooster")
    ophalen()
    print("")
    terug()

# close
def afsluiten():
    print("Tot ziens!")
    exit()

menu()
