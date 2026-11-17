# Compte-rendu d'incident - Mise en service v0.9.0 (Staging)

- **Ce qui s'est passé** : La mise en service de l'image v0.9.0 a échoué suite à un crash immédiat du conteneur API causé par une exception non gérée `KeyError: 'CLE_API_OBLIGATOIRE'` au lancement de `app/app.py`.
- **Moment de détection** : L'incident a été détecté dès la fin du déploiement par le script `./scripts/wait-healthy.sh` qui s'est soldé par un échec (code de sortie 1) après 12 vérifications infructueuses sur `http://localhost:8080/health`.
- **Action corrective** : Un rollback immédiat vers l'image validée précédente a été opéré en modifiant `IMAGE_TAG=v1.0.0` dans `.env.deploy` et en réexécutant `docker compose --env-file .env.deploy -f compose.staging.yaml up -d` sans aucune reconstruction d'image.
- **Durée d'indisponibilité** : 77 secondes mesurées, du `up -d` de v0.9.0 au retour de `staging sain` après rollback (chronologie dans docs/preuves/chronologie-incident.txt).
- **Mesure préventive** : Ajouter dans le pipeline CI une étape de test d'exécution du conteneur Docker (smoke test du conteneur complet) pour bloquer la publication de toute image dont le processus principal crashe au démarrage.

## Première erreur utile identifiée dans les logs

```text
Traceback (most recent call last):
  File "/app/app/app.py", line 36, in <module>
    __import__("os").environ["CLE_API_OBLIGATOIRE"]
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen os>", line 714, in __getitem__
KeyError: 'CLE_API_OBLIGATOIRE'
```
