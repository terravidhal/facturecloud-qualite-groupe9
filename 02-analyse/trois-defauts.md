# Trois défauts à remonter — fonctions_s3.py (S3)

Binôme : NGUEA ELAME MARSILE-VIDHAL & FOKO TADJUIGE JUNIOR
Date : 18/11/2026

## Règle de chaque fonction (avec mes mots)

- **calculer_tva** : la TVA est 19,25 % du montant HT, arrondie au franc le plus proche. Si le résultat tombe pile à mi-chemin entre deux francs, on arrondit vers le haut.
- **total_facture** : le total d'une facture est la somme de (quantité × prix unitaire) de toutes les lignes. Pas de ligne = total de 0.
- **niveau_relance** : plus les jours de retard augmentent, plus le niveau de relance monte : 0 avant 7 jours, 1 au-delà de 7, 2 au-delà de 15, 3 au-delà de 30. À 15 jours pile, le client dit que c'est encore le niveau 1.

## Fonction 1 — calculer_tva

| Montant HT | Calcul à la main (montant × 0,1925) | Attendu | Obtenu | Verdict |
| --- | --- | --- | --- | --- |
| 100 | 19,25 | 19 | | |
| 150 | 28,875 | 29 | | |
| 200 | 38,5 | 39 | | |
| 600 | 115,5 | 116 | | |
| 1 000 | 192,5 | 193 | | |
| 3 000 | 577,5 | 578 | | |
| 5 000 | 962,5 | 963 | | |

## Fonction 2 — total_facture

| Cas | Lignes | Attendu | Obtenu | Verdict |
| --- | --- | --- | --- | --- |
| a | aucune ligne | 0 | | |
| b | une ligne : 2 × 5 000 | 10 000 | | |
| c | deux lignes : 2 × 5 000 et 1 × 3 000 | 13 000 | | |
| d | trois lignes : 1 × 100, 1 × 200, 1 × 300 | 600 | | |

## Fonction 3 — niveau_relance

| Jours de retard | 0 | 6 | 7 | 8 | 14 | 15 | 16 | 29 | 30 | 31 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Attendu | 0 | 0 | 0 | 1 | 1 | 1 | 2 | 2 | 2 | 3 |
| Obtenu | | | | | | | | | | |
