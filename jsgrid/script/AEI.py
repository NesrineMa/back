import requests
from bs4 import BeautifulSoup
import mysql.connector


# retourner l'identifiant de chaque url ramenant les détails d'une entreprise // # retourner l'identifiant de chaque url ramenant les détails d'une entreprise //
def ident(list):
    for i in range(len(list)):
        j = 0
        if list[i] != None:
            while list[i][j] != "'":
                j = j + 1
            list[i] = list[i][j + 29:len(list[i]) - 1]

# return the number of pages of every "secteur"
def nbPage(urlsec):
    with requests.Session() as s:
        r = s.get(urlsec)

        soup = BeautifulSoup(r.text, "html.parser")

        data = []

        rows = soup.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
        d = str(data[1])
        res = [int(s) for s in d.split() if s.isdigit()]
        i = res[1]
        return i

# insert values to "profil" table in database
def insertVariablesIntoTable(id, denomination, raison_sociale, responsable, activites, produits, adresse_usine, gouvernorat, delegation, telephone_siege_usine, fax_siege_usine, email, URL, regime, pays_du_participant_etranger, entree_en_production, capital_en_DT, emploi, secteur):
    try:      # BD connection

        mydb = mysql.connector.connect(host='localhost',
                                         database='annuaire',
                                         user='root',
                                         password='')

        values = (id, denomination, raison_sociale, responsable, activites, produits, adresse_usine, gouvernorat, delegation, telephone_siege_usine, fax_siege_usine, email, URL, regime, pays_du_participant_etranger, entree_en_production, capital_en_DT, emploi,secteur)
        cursor = mydb.cursor()
        # create queries
        mysql_insert_query = """ INSERT INTO profil ( id, denomination, raison_sociale, responsable, activites, produits, adresse_usine, gouvernorat, delegation, telephone_siege_usine, fax_siege_usine, email, URL, regime, pays_du_participant_etranger, entree_en_production, capital_en_DT, emploi,secteur)
         VALUES (%s, %s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s,%s, %s,%s, %s,%s, %s, %s) """
        cursor.execute(mysql_insert_query, values)
        mydb.commit()
        print("Record inserted successfully into Profil table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (mydb.is_connected()):
            cursor.close()
            mydb.close()
            print("MySQL connection is closed")


def extract_data(mylist):
    for i in range(len(mylist)):
        j = 0
        if mylist[i] != None:
            while mylist[i][j] != ">":
                j = j + 1
            if mylist[i].find('a href=""') != -1 or mylist[i].find('a href="mailto:">') != -1:
                mylist[i] = ""

            elif mylist[i].find('mailto:') != -1:

                if mylist[i].find('.com.tn') != -1:
                    mylist[i] = mylist[i][mylist[i].find('mailto:') + 7: mylist[i].find('.com.tn"') + 7]

                elif mylist[i].find('.tn') != -1:
                    mylist[i] = mylist[i][mylist[i].find('mailto:') + 7: mylist[i].find('.tn"') + 3]

                elif mylist[i].find('.fr') != -1:
                    mylist[i] = mylist[i][mylist[i].find('mailto:') + 7: mylist[i].find('.fr"') + 3]

                elif mylist[i].find('.com') != -1:
                    mylist[i] = mylist[i] = mylist[i][mylist[i].find('mailto:') + 7: mylist[i].find('.com"') + 4]

                elif mylist[i].find('.it') != -1:
                    mylist[i] = mylist[i] = mylist[i][mylist[i].find('mailto:') + 7: mylist[i].find('.it"') + 3]

                elif mylist[i].find('.net') != -1:
                    mylist[i] = mylist[i] = mylist[i][mylist[i].find('mailto:') + 7: mylist[i].find('.net"') + 4]

                elif mylist[i].find('.biz') != -1:
                    mylist[i] = mylist[i] = mylist[i][mylist[i].find('mailto:') + 7: mylist[i].find('.biz"') + 4]

            elif mylist[i].find('http') != -1:
                if mylist[i].find('.tn') != -1:
                    mylist[i] = mylist[i][mylist[i].find('http') + 7: mylist[i].find('.tn"') + 3]

                elif mylist[i].find('.com') != -1:
                    mylist[i] = mylist[i][mylist[i].find('http') + 7: mylist[i].find('.com"') + 4]

                elif mylist[i].find('.net') != -1:
                    mylist[i] = mylist[i][mylist[i].find('http') + 7: mylist[i].find('.net"') + 4]

                elif mylist[i].find('.it') != -1:
                    mylist[i] = mylist[i][mylist[i].find('http') + 7: mylist[i].find('.it"') + 3]
            else:
                mylist[i] = mylist[i][j + 1:len(mylist[i]) - 6]

# extract data from list having <td> tags (mails and urls)
def deleteFromTable():
    try:      # BD connection

        mydb = mysql.connector.connect(host='localhost',
                                         database='annuaire',
                                         user='root',
                                         password='')

        cursor = mydb.cursor()
        # create queries
        mysql_delete_query = """DELETE FROM profil;"""

        cursor.execute(mysql_delete_query)
        mydb.commit()
        print("Record deleted successfully from Profil table")

    except mysql.connector.Error as error:
        print("Failed to delete from MySQL table {}".format(error))

    finally:
        if (mydb.is_connected()):
            cursor.close()
            mydb.close()
            print("MySQL connection is closed")


# access urls from form to page having Etse , secteur bois liège et ameublement
def treat(myurl, nbpage, secteur):
    with requests.Session() as s:
        r = s.get(myurl)
        links = []
        if r.ok:
            soup = BeautifulSoup(r.text, "html.parser")
            for link in soup.find_all('tr'):
                click = link.get('onclick')
                if click is None:
                    continue
                links.append(click)  # add content of "onclick" to the list links only for the first page
        # the following code: consult all the pages and add content of onclick to the same list "links"
        for i in range(nbpage):
            url_next = "http://www.tunisieindustrie.nat.tn/fr/dbi.asp?action=search&pagenum="+str(i+2)

            rn = s.get(url_next)
            soup = BeautifulSoup(rn.text, "html.parser")
            for link in soup.find_all('tr'):
                click = link.get('onclick')
                if click is None:
                    continue
                links.append(click)
        temp_links = links
        ident(temp_links)
    # create links using ids extracted above then here is the final access to information of every enterprise
        for l in range(len(temp_links)):
            url_fin = "http://www.tunisieindustrie.nat.tn/fr/dbi.asp?action=result&ident=" + temp_links[l]
            rf = s.get(url_fin)
            soup = BeautifulSoup(rf.text, "html.parser")
            table = soup.find("table")
            title = soup.find("title")
            data = []

            if str(title) == "<title>Annuaire des entreprises industrielles</title>":
                for link_f in table.find_all('tr'):
                    var = link_f.find_all('td')
                    data.append(str(var[1]))
                extract_data(data)
                insertVariablesIntoTable(l, data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7],
                                         data[8],
                                         data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16],
                                         secteur)
            else:

                print(str(title))

                pass

# "Industries agro-alimentaires"
urlagro = 'http://www.tunisieindustrie.nat.tn/fr/dbi.asp?secteur=05&branche=&produit=&Denomination=&Gouvernorat=&delegation=&pays=&regime=&ent_prd=&cap1=&cap2=&emp1=&emp2=&action=search'
nbpageagro = nbPage(urlagro)
agro = "Industries agro-alimentaires"
treat(urlagro, nbpageagro, agro)