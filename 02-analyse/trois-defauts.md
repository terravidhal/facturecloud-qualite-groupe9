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
| 100 | 19,25 | 19 | 19 | conforme |
| 150 | 28,875 | 29 | 29 | conforme |
| 200 | 38,5 | 39 | 38 | écart |
| 600 | 115,5 | 116 | 116 | conforme |
| 1 000 | 192,5 | 193 | 192 | écart |
| 3 000 | 577,5 | 578 | 578 | conforme |
| 5 000 | 962,5 | 963 | 962 | écart |

### Chercher le motif

Les écarts (200, 1000, 5000) sont tous des montants où le calcul tombe pile à mi-chemin (...,5) **et** où le chiffre entier juste en dessous est pair (38, 192, 962 sont pairs). Pour 600 et 3000, le calcul tombe aussi à mi-chemin (115,5 et 577,5), mais l'entier en dessous est impair (115, 577) — et là, pas d'écart.

Expérience `round()` en Python : `round(0.5)=0`, `round(1.5)=2`, `round(2.5)=2`, `round(3.5)=4`, `round(38.5)=38`, `round(115.5)=116`. La règle suivie par `round()` à mi-chemin n'est pas « toujours vers le haut » mais **« vers le nombre pair le plus proche »** (arrondi bancaire). C'est pour ça que certains montants sont conformes par coïncidence (quand le nombre pair est aussi celui du dessus) et d'autres non.

### Chaîne — calculer_tva

| Maillon | Contenu |
| --- | --- |
| Défaillance observée | Pour 200, 1000 et 5000 FCFA de HT, la TVA retournée est 1 franc en dessous de l'attendu (38 au lieu de 39, 192 au lieu de 193, 962 au lieu de 963) |
| Résultat attendu et sa source | Arrondi au franc le plus proche, mi-chemin toujours vers le haut — règle écrite en tête de `calculer_tva` |
| Défaut | Ligne `return round(tva)` : utilise `round()` de Python, qui arrondit au pair le plus proche à mi-chemin, pas vers le haut |
| Erreur probable | La personne qui a codé a supposé que `round()` arrondissait toujours les `.5` vers le haut (comme on l'apprend à l'école), sans vérifier le comportement réel de Python |
| Origine | Codage |
| Correction suggérée | Remplacer `round(tva)` par un calcul en entiers, par exemple `(montant_ht * 1925 + 5000) // 10000`, qui arrondit explicitement les `.5` vers le haut |

## Fonction 2 — total_facture

| Cas | Lignes | Attendu | Obtenu | Verdict |
| --- | --- | --- | --- | --- |
| a | aucune ligne | 0 | None | écart |
| b | une ligne : 2 × 5 000 | 10 000 | 10 000 | conforme |
| c | deux lignes : 2 × 5 000 et 1 × 3 000 | 13 000 | 10 000 | écart |
| d | trois lignes : 1 × 100, 1 × 200, 1 × 300 | 600 | 100 | écart |

Les cas conformes ont en commun d'avoir **au plus une seule ligne** : c'est le seul cas où la fonction a le temps de faire quelque chose avant de s'arrêter.

### Chaîne — total_facture

| Maillon | Contenu |
| --- | --- |
| Défaillance observée | Facture vide → `None` au lieu de 0 ; facture à 2 lignes ou plus → seule la première ligne est comptée |
| Résultat attendu et sa source | Somme de toutes les lignes, 0 si aucune ligne — règle écrite en tête de `total_facture` |
| Défaut | `return total` est indenté au même niveau que `total = total + ...`, donc **à l'intérieur** de la boucle `for` : la fonction sort dès la première itération |
| Erreur probable | Erreur d'indentation : la personne voulait sans doute mettre `return total` après la boucle (une colonne à gauche) mais l'a laissé dans le corps du `for` |
| Origine | Codage |
| Correction suggérée | Sortir `return total` de la boucle, en l'alignant avec le `for` (une indentation à gauche) |

## Fonction 3 — niveau_relance

| Jours de retard | 0 | 6 | 7 | 8 | 14 | 15 | 16 | 29 | 30 | 31 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Attendu | 0 | 0 | 0 | 1 | 1 | 1 | 2 | 2 | 2 | 3 |
| Obtenu | 0 | 0 | 1 | 1 | 1 | 2 | 2 | 2 | 3 | 3 |

## Synthèse

| Fonction | Origine du défaut | Où se voit la défaillance | Gravité pour le client |
| --- | --- | --- | --- |
| calculer_tva | Codage | Quelques valeurs (montants à mi-chemin dont l'entier du dessous est pair) | Moyenne à forte — montant facturé faux, de façon imprévisible pour le client |
| total_facture | Codage | Certains cas (dès que la facture a 2 lignes ou plus) | Très forte — faux pour la quasi-totalité des factures réelles |
| niveau_relance | Codage | Quelques valeurs (les 3 bornes exactes 7, 15, 30) | Faible à moyenne — relance envoyée un jour trop tôt, incohérent avec le barème annoncé |

## Réponse à la direction (ticket TVA — Quincaillerie Mbarga)

La fonction de calcul de la TVA utilise l'arrondi standard de Python, qui arrondit parfois vers le bas quand le montant tombe exactement à mi-chemin entre deux francs (par exemple 192,50 devient 192 au lieu de 193). Cela ne touche que certains montants précis, pas toutes les factures — celle de la Quincaillerie Mbarga en faisait partie. Ce n'est ni un plantage ni un hasard : le même montant donnera toujours le même résultat faux. Nous proposons de remplacer cet arrondi par un calcul qui arrondit toujours vers le haut à mi-chemin, comme le prévoit la règle de gestion. La correction est simple et ne touche que cette seule ligne.

Écarts exactement à j=7, j=15 et j=30 — les trois valeurs limites de la règle (3 valeurs sur 10 sont fausses).

### Chaîne — niveau_relance

| Maillon | Contenu |
| --- | --- |
| Défaillance observée | À exactement 7, 15 et 30 jours de retard, le niveau retourné est un cran trop haut (1 au lieu de 0, 2 au lieu de 1, 3 au lieu de 2) |
| Résultat attendu et sa source | Niveau 1 **au-delà de** 7 jours, niveau 2 au-delà de 15, niveau 3 au-delà de 30 — et l'exemple du client confirme qu'à 15 jours pile c'est encore le niveau 1 |
| Défaut | Les trois comparaisons utilisent `>=` (`jours_de_retard >= 7`, etc.) au lieu de `>` |
| Erreur probable | La personne a traduit « au-delà de X » par « à partir de X » (inclusif), alors que le client voulait dire « strictement après X » |
| Origine | Codage (mauvaise traduction d'une règle pourtant bien écrite) |
| Correction suggérée | Remplacer chaque `>=` par `>` dans les trois comparaisons |

Sans l'exemple donné par le client, les deux lectures de « au-delà de » étaient possibles et on n'aurait pas pu trancher seul. Avant de déclarer un défaut sur un cas limite comme celui-ci, il faut vérifier la règle avec la personne qui la connaît plutôt que de deviner.
