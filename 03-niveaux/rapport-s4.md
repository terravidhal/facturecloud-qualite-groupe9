# Du composant à la facture — facturation.py (S4)

Binôme : NGUEA ELAME MARSILE-VIDHAL & FOKO TADJUIGE JUNIOR
Date : 18/11/2026

## Niveau composant

| Fonction | Entrée | Attendu | Obtenu | Verdict |
| --- | --- | --- | --- | --- |
| total_ht | [(2, 5000), (1, 3000)] | 13 000 | 13 000 | conforme |
| total_ht | [] (liste vide) | 0 | 0 | conforme |
| calculer_remise | 13 000, client fidèle | 1 300 | 1 300 | conforme |
| calculer_remise | 13 000, client non fidèle | 0 | 0 | conforme |
| calculer_tva | 200 | 39 | 39 | conforme |
| calculer_tva | 11 700 | 2 252 | 2 252 | conforme |

Les 3 fonctions prises isolément sont toutes conformes : `pytest -v` donne 6/6 réussis à ce niveau.

## Niveau intégration — creer_facture([(2, 5000), (1, 3000)], ...)

| Cas | ht | remise | net | tva | ttc |
| --- | --- | --- | --- | --- | --- |
| Client fidèle — attendu | 13 000 | 1 300 | 11 700 | 2 252 | 13 952 |
| Client fidèle — obtenu | 13 000 | 1 300 | 11 700 | **2 503** | **14 203** |
| Client non fidèle — attendu/obtenu | 13 000 | 0 | 13 000 | 2 503 | 15 503 |

Source : ht = somme des lignes ; remise = règle du composant ; net = ht − remise ; **tva = 19,25 % du montant HT *après remise*** (donc calculée sur `net`, pas sur `ht` — c'est écrit tel quel dans la règle en tête de `facturation.py`) ; ttc = net + tva.

## Résultats pytest

`python -m pytest -v` : **7 réussis, 1 échoué**.

```
test_facturation.py::test_total_ht_deux_lignes PASSED
test_facturation.py::test_total_ht_liste_vide PASSED
test_facturation.py::test_remise_client_fidele PASSED
test_facturation.py::test_remise_client_non_fidele PASSED
test_facturation.py::test_tva_200 PASSED
test_facturation.py::test_tva_11700 PASSED
test_facturation.py::test_facture_client_fidele FAILED
    assert facture["tva"] == 2252
    assert 2503 == 2252
test_facturation.py::test_facture_client_non_fidele PASSED
```

Verdict : cas « client fidèle » = **écart** (tva et ttc faux) ; cas « client non fidèle » = **conforme**.

## Fiche d'analyse — écart sur creer_facture (client fidèle)

| Maillon | Contenu |
| --- | --- |
| Défaillance observée | Pour une facture avec remise, la TVA et le TTC retournés sont trop élevés (tva = 2 503 au lieu de 2 252 ; ttc = 14 203 au lieu de 13 952) |
| Résultat attendu et sa source | « La TVA est de 19,25 % du montant HT **après remise** » — règle écrite en tête de `facturation.py` |
| Défaut | Dans `creer_facture`, la ligne `tva = calculer_tva(ht)` utilise `ht` (avant remise) au lieu de `net` (après remise) |
| Erreur probable | La personne qui a assemblé `creer_facture` a relu la variable `ht` sans remarquer que la règle demande le montant *après* remise, c'est-à-dire `net` |
| Origine | Codage (erreur d'assemblage entre fonctions par ailleurs correctes) |
| Correction suggérée | Remplacer `calculer_tva(ht)` par `calculer_tva(net)` |

## Pourquoi les tests composant ne l'ont pas vu

`calculer_tva` est testée seule et reçoit exactement la valeur qu'on lui donne : elle n'a aucun moyen de savoir si c'est `ht` ou `net` qui aurait dû lui être passé. Le défaut n'est pas dans une fonction, mais dans la façon dont `creer_facture` les **assemble** — il n'apparaît donc qu'au niveau intégration, quand on observe le résultat combiné. Le principe illustré : des composants individuellement corrects peuvent produire un système faux si leur **branchement** est incorrect.

Remarque : le cas « client non fidèle » ne révèle rien, car `remise = 0` rend `net` égal à `ht` — le défaut est alors invisible par coïncidence. C'est tester le cas « client fidèle » qui l'a démasqué.

## Vérification ou validation ?

Ici, on fait de la **vérification** : on compare le comportement du code à une règle de gestion déjà écrite et connue à l'avance (« fait-on le produit correctement ? »), pas à un besoin réel du client qu'il faudrait encore découvrir.
