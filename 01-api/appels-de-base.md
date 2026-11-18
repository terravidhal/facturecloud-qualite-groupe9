# Appels de base — API FactureCloud (S2)

Binôme : NGUEA ELAME MARSILE-VIDHAL & FOKO TADJUIGE JUNIOR
Date : [à remplir]

Note : `api-factures` tourne sur le port 8090 (8080 bloqué par Windows, voir journal TP1).

## Appels

| N° | Requête | Attendu (code + corps) | Source de l'attendu | Obtenu | Verdict |
| --- | --- | --- | --- | --- | --- |
| 1 | GET http://localhost:8090/sante | 200, `{"statut":"ok"}` | vu en démo au TP1 | 200, `{"statut":"ok"}` | conforme |
| 2 | GET http://localhost:8090/factures/FC-2026-000001 | 200, `{"client":"Atelier Mbarga","total_ttc":119250}` | facture de démo donnée au TP1 | 200, `{"client":"Atelier Mbarga","total_ttc":119250}` | conforme |
| 3 | GET http://localhost:8090/factures/XXX | 404, `{"erreur":"FACTURE_INCONNUE"}` | logique : une facture qui n'existe pas doit donner une erreur, pas un plantage | 404, `{"erreur":"FACTURE_INCONNUE"}` | conforme |
| 4 | GET http://localhost:8081/tva?montant=1000 | 200, `{"montant_ht":1000,"tva":193}` | règle TVA 19,25 % arrondie au franc le plus proche : 1000 × 0,1925 = 192,5 → 193 | 200, `{"montant_ht":1000,"tva":193}` | conforme |

## Ce que je constate

1. Dans la réponse de l'appel 2, les clés sont `client` (texte) et `total_ttc` (nombre, pas une chaîne — pas de guillemets autour de 119250).
2. L'appel 3 renvoie 404 : ce n'est pas un plantage du service (qui serait un 5xx), c'est une erreur côté appelant (famille 4xx) — on a demandé une ressource qui n'existe pas, le service répond correctement en le signalant.
3. Pour l'appel 4 : 19,25 % de 1000 = 192,5, arrondi vers le haut à 193 — confirmé par la réponse.
