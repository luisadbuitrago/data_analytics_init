import numpy as np

def analyser_ventes(transactions):
    transactions_valides = []
    calculs_stat = {}
    outliers = []
    for t in transactions:
        if t is not None and t > 0:  #Filtrer la liste pour ignorer les valeurs négatives ou nulles
            transactions_valides.append(t)

    calculs_stat["Transactions valides"] = len(transactions_valides)
    calculs_stat["Somme totale"] = sum(transactions_valides)
     
    if calculs_stat["Transactions valides"] > 0:
        calculs_stat["Moyenne"] = calculs_stat["Somme totale"] / calculs_stat["Transactions valides"]
        calculs_stat["Médiane"] = np.median(transactions_valides)
        calculs_stat["Ecart-type"] = np.std(transactions_valides).round(2)
        calculs_stat["Minimum"] = np.min(transactions_valides)
        calculs_stat["Maximum"] = np.max(transactions_valides)
        for i in transactions_valides:
            if i > 2 * calculs_stat["Moyenne"]:  #Détection des anomalies
                outliers.append(i)
        calculs_stat["Outliers"] = outliers

    else:
        print("Les transactions ne sont pas valides.")     

    return calculs_stat   #Retourner un dictionnaire contenant tous ces indicateurs.
    
#Bloc d'exécution et de test
test = [50, -70, 100, None, 130, 500, 0]
resultats = analyser_ventes(test)
for cle, valeur in resultats.items():
    print(f"{cle}: {valeur}")
    