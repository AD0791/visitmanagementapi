# visitmanagementapi

---

REST Web services for a visit management application - FASTAPI

## How to Start the server

We have a setup for development and production

### Start up

For development:

```zsh
docker-compose -f docker-compose.dev.yml up --build
```

For production:

```zsh
docker-compose -f docker-compose.prod.yml up --build
```

> add the --build command if you have added deps in the requirement.txt file. Or if it's your first build.

**Tear down**

To stop and remove the containers, networks, etc:

```zsh
docker-compose -f docker-compose.dev.yml down
```

```zsh
docker-compose -f docker-compose.prod.yml down
```
