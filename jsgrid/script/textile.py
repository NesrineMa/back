import requests


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


urlceram = 'http://www.tunisieindustrie.nat.tn/fr/dbi.asp?secteur=02&branche=&produit=&Denomination=&Gouvernorat=&delegation=&pays=&regime=&ent_prd=&cap1=&cap2=&emp1=&emp2=&action=search'
nbpageceram = nbPage(urlceram)