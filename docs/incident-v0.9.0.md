# Compte-rendu d'incident - Mise en service v0.9.0 (Staging)

- **Ce qui s'est passé** : La mise en service de l'image v0.9.0 a échoué suite à un crash immédiat du conteneur API causé par une exception non gérée `KeyError: 'CLE_API_OBLIGATOIRE'` au lancement de `app/app.py`.
- **Moment de détection** : 15:05:40, soit 71 s après le déploiement de v0.9.0 (15:04:29), par `wait-healthy.sh` (code de sortie 1 après 12 essais). Le conteneur était en `Restarting` (voir chronologie-incident.txt).
- **Action corrective** : retour arrière vers v1.0.0 en changeant `IMAGE_TAG` dans `.env.deploy` puis `up -d`, sans reconstruction. Service sain 5 s après la relance (15:05:46).
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
