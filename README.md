# Campus Tasks

## Démarrage

Projet utilisé dans les ateliers DevOps.

## Santé du service

Point prévu : GET /health

## Support
Contact : equipe-a@example.invalid

## Lancer avec Docker Compose

Pile : `api` (Flask, port 8080) et `db` (PostgreSQL 17), sur un reseau prive Compose.

```bash
docker compose config            # valider
docker compose up -d --build     # demarrer
docker compose ps                # etat (db et api healthy)
curl http://localhost:8080/health
curl http://localhost:8080/db-check
```

- La base n'est pas publiee sur l'hote : seul `api` la joint, par le nom `db`.
- Les donnees sont dans le volume nomme `pgdata` (survit a `docker compose down`).
- `docker compose down -v` supprime aussi les donnees.
- Adminer (port 8081) ne demarre qu'a la demande : `docker compose --profile debug up -d`.
- Les mots de passe du fichier sont fictifs, pour un usage local uniquement.
