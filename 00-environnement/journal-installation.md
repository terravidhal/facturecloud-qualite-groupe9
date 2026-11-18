# Journal d'installation - S1

Binôme : NGUEA ELAME MARSILE-VIDHAL & FOKO TADJUIGE JUNIOR
Date : 19/10/2026
Système : Windows 11

## Versions

- Python : Python 3.12.7
- Flask : Flask 3.1.3

## Ce que j'ai fait

1. Créé l'environnement virtuel (`python -m venv .venv`) puis activé (`.venv\Scripts\activate`)
2. Installé Flask (`pip install flask`)
3. Lancé `api-factures` (`python main.py`) → le port 8080 était occupé (refusé par Windows), relancé avec `set PORT=8090` → http://127.0.0.1:8090
4. Lancé `service-calcul` (`python main.py`) → http://127.0.0.1:8081
5. [à compléter si tu ajoutes d'autres étapes]

## Ce que j'ai observé

- `http://localhost:8090/sante` → {"statut":"ok"}
- `http://localhost:8081/sante` → {"statut":"ok"}
- TVA pour 1000 : [valeur] ; TVA pour 200 que j'attendais : [valeur], obtenue : [valeur]

Capture d'écran — réponse de /sante, api-factures : `00-environnement/capture-api-factures-sante.png`

Capture d'écran — réponse de /sante, service-calcul : `00-environnement/capture-service-calcul-sante.png`

## Problèmes rencontrés

| Message d'erreur (dernière ligne) | Cause | Correction |
| --- | --- | --- |
| `can't open file '...\facturecloud\main.py': [Errno 2] No such file or directory` | Lancé `python main.py` depuis `facturecloud/` au lieu de `facturecloud/service-calcul/` | `cd service-calcul` puis relancer |
| Page "Ce site est inaccessible — localhost n'autorise pas la connexion" (voir `capture-erreurB-service-arrete.png`) | Service `api-factures` arrêté (Ctrl+C) | Relancer `python main.py` dans `api-factures/` |

Erreur A (mauvais dossier) et Erreur B (service arrêté) toutes deux provoquées volontairement puis corrigées, comme demandé par la fiche.

## Autoévaluation

| Je sais… | Seul | Avec aide | Pas encore |
| --- | --- | --- | --- |
| Expliquer ce qu'est un service web | | | |
| Utiliser un terminal | | | |
| Installer Python, Sublime Text et créer un environnement virtuel | | | |
| Lancer deux services et les vérifier | | | |
| Lire un message d'erreur | | | |
