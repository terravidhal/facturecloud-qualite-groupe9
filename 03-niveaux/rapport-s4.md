# Du composant à la facture — facturation.py (S4)

Binôme : NGUEA ELAME MARSILE-VIDHAL & FOKO TADJUIGE JUNIOR
Date : 18/11/2026

## Niveau composant

| Fonction | Entrée | Attendu | Source de l'attendu |
| --- | --- | --- | --- |
| total_ht | [(2, 5000), (1, 3000)] | 13 000 | somme quantité × prix de chaque ligne |
| total_ht | [] (liste vide) | 0 | "liste vide : 0" |
| calculer_remise | 13 000, client fidèle | 1 300 | 10 % de 13 000 = 1 300 (exact) |
| calculer_remise | 13 000, client non fidèle | 0 | "0 sinon" |
| calculer_tva | 200 | 39 | 200 × 0,1925 = 38,5 → arrondi vers le haut |
| calculer_tva | 11 700 | 2 252 | 11 700 × 0,1925 = 2 252,25 → arrondi au plus proche |

## Niveau intégration — creer_facture([(2, 5000), (1, 3000)], ...)

| Cas | ht | remise | net | tva | ttc |
| --- | --- | --- | --- | --- | --- |
| Client fidèle | 13 000 | 1 300 | 11 700 | 2 252 | 13 952 |
| Client non fidèle | 13 000 | 0 | 13 000 | 2 503 | 15 503 |

Source : ht = somme des lignes ; remise = règle du composant ; net = ht − remise ; **tva = 19,25 % du montant HT *après remise*** (donc calculée sur `net`, pas sur `ht` — c'est écrit tel quel dans la règle en tête de `facturation.py`) ; ttc = net + tva.
