import numpy as np

def analyser_ventes(transactions):
    calculs_stat = {}
    transactions_valides = [t for t in transactions if t is not None and t > 0]

    calculs_stat["Transactions valides"] = len(transactions_valides)
    calculs_stat["Somme totale"] = sum(transactions_valides)
    if calculs_stat["Transactions valides"] > 0:
        calculs_stat["Moyenne"] = calculs_stat["Somme totale"] / calculs_stat["Transactions valides"]
        calculs_stat["Médiane"] = np.median(transactions_valides)
        calculs_stat["Ecart-type"] = np.std(transactions_valides)
        calculs_stat["Minimum"] = np.min(transactions_valides)
        calculs_stat["Maximum"] = np.max(transactions_valides)
        calculs_stat["Outliers"] = [anom for anom in transactions_valides if anom > 2 * calculs_stat["Moyenne"]]    
    else:
        print("Les transactions ne sont pas valides.")     

    return calculs_stat   #Retourner un dictionnaire contenant tous ces indicateurs.
    
#Bloc d'exécution et de test
if __name__ == "__main__":
    test = [50, -70, 100, None, 130, 500, 0]
    resultats = analyser_ventes(test)
    for cle, valeur in resultats.items():
        print(f"{cle}: {valeur}")