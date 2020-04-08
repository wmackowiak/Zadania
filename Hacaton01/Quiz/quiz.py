pytania = \
    [
        {'pytanie':'Gdzie zmarł Adam Mickiewicz?','odpowiedzi': ['w Paryżu','w Warszawie','w Konstantynopolu','w Krakowie'], 'popr_odp': 'w Paryżu'},
        {'pytanie':'Która planeta znajduje się najbliżej Słońca?','odpowiedzi': ['Ziemia','Merkury','Wenus','Mars'], 'popr_odp': 'Merkury'},
        {'pytanie':'Kto wyreżyserował film "Titanic"?','odpowiedzi': ['James Cameron','Quentin Tarantino','Stanley Kubrick','Mel Gibson'], 'popr_odp': 'James Cameron'},
        {'pytanie':'Pierwszy rozbiór Polski odbył się w:','odpowiedzi': ['1772','1792','1793','1795'], 'popr_odp': '1772'},
        {'pytanie':'Czy kwas foliowy w największych ilościach znajduje się w warzywach strączkowych?','odpowiedzi': ['tak','nie'], 'popr_odp': 'tak'},
        {'pytanie':'Dokończ przysłowie: "Nosił wilk razy kilka..."','odpowiedzi': ['przyszedł czas na chytrego wilka','ponieśli i wilka','teraz futro noszą z wilka','później owca zjadła wilka'], 'popr_odp': 'ponieśli i wilka'},
        {'pytanie':'Najgłębsze jezioro świata znajduje się w:','odpowiedzi': ['Gruzji','Rosji','Ameryce Północnej','Indiach'], 'popr_odp': 'Rosji'},
        {'pytanie':'Czy granit to skała magmowa?','odpowiedzi': ['tak','nie'], 'popr_odp': 'tak'},
        {'pytanie':'Który król zapoczątkował obiady czwartkowe?','odpowiedzi': ['Stanisław August Poniatowski','Bolesław I Chrobry','Władysław I Łokietek','Ludwik Węgierski'], 'popr_odp': 'Stanisław August Poniatowski'},
        {'pytanie':'Kto wynalazł żarówkę?','odpowiedzi': ['bracia Wright','Alexander Fleming','Thomas Edison'], 'popr_odp': 'Thomas Edison'}
    ]
punkty = 0
for i in range(10):
    print("-"*70)
    print(pytania [i]['pytanie'])
    for x in range(len(pytania[i]['odpowiedzi'])):
        print(pytania [i]['odpowiedzi'][x])

    odp = input("Odpowiedz: ")
    print("Poprawna odpowiedz:", pytania [i]['popr_odp'])

    if odp.upper() == pytania [i]['popr_odp'].upper():
        print("Brawo, właściwa odpowiedz!")
        punkty +=1
    else:
        print("Niestety nie udało się")
    print("")

print(f"Gratulacje zdobyłeś: {punkty}/10 punktów")
