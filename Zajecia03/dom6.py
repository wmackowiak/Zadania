# Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać. Poza pętlą umieść
# pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.

skladniki = ['0,5 kg mąki pszennej','20 g drożdży','1 łyżeczka cukru','2 łyżeczki soli','ok. 1,5 szklanki ciepłej wody']
print(len(skladniki))

for skl in skladniki:
    print("Zacznijmy od przesiania " + skladniki[0] + ".")
    print(skladniki[1] + " rozdrabniamy i razem z kilkoma łyżkami przesianej mąki i ")
    print(skladniki[2] + " mieszamy z ciepłą wodą.")
    print("Zostawiamy na 20 minut i czekamy aż drożdże zaczną pracować i urosną.")
    print("W dużej misce mieszamy mąkę, "+skladniki[3] +" i cukier, a następnie wlewamy " + skladniki[4]  + ".")


