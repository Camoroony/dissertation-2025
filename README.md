# Hypertrophy EDU

**Hypertrophy EDU** is a full-stack AI application designed for educational content and data-driven hypertrophy training insights. The app includes:

- A React-based frontend
- A FastAPI backend
- MySQL for structured data
- MongoDB for unstructured/document-based data
- A vector store for semantic data storage

All services are orchestrated via **Docker Compose** for easy deployment and local testing.

---

## Prerequisites

Before getting started, ensure you have the following tools installed:

- **Docker Desktop**: [Install Docker Here](https://docs.docker.com/get-docker/)

You can verify installation with:
```bash
docker --version
```
To check docker is running, you'll see the Docker whale icon in the system tray (Windows) or the menu bar (Mac).

- **Ports**:

The following ports `3000`, `8000`, `3306` and `27017` are required to be free on your local PC, so if the application fails to build, check they are not being used.

---

## Installation

Below is the compose file used to run the entire Hypertrophy EDU stack.
Create a file called `docker-compose.yml` in a directory on your PC containing the following code:

```yaml
version: '3.8'
services:
  hypertrophy_edu_backend:
    image: ghcr.io/camoroony/hypertrophy-edu-backend:latest
    container_name: hypertrophy-edu_backendcontainer
    restart: always
    environment:
      SQLDB_URL: mysql+pymysql://root:password@sql/hypertrophy_edu_sqldb 
      MONGODB_URL: mongodb://mongo:27017/hypertrophy_edu_mongodb
    depends_on:
      - sql  
      - mongo
    ports:
      - "8000:8000" 
    volumes:
      - vectorstore_data:/app/database/chroma/chroma_dbs

  hypertrophy_edu_frontend:
    image: ghcr.io/camoroony/hypertrophy-edu-frontend:latest
    container_name: hypertrophy-edu_frontendcontainer
    restart: always
    ports:
      - "3000:80"
    depends_on:
      - hypertrophy_edu_backend

  sql:
    image: mysql:8.0
    container_name: hypertrophy-edu_dbcontainer
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_DATABASE: hypertrophy_edu_sqldb
    ports:
      - "3306:3306"
    volumes:
      - sqldb_data:/var/lib/mysql

  mongo:
    image: mongo:latest
    container_name: hypertrophy-edu_mongocontainer
    restart: always
    environment:
      MONGO_INITDB_DATABASE: hypertrophy_edu_mongodb
    ports:
      - "27017:27017"
    volumes:
      - mongodb_data:/data/db
      - mongodb_config:/data/configdb

volumes:
  sqldb_data:
  mongodb_data:
  mongodb_config:
  vectorstore_data:
```

Navgate to the directory containing the compose file in a terminal and run the command:
```bash
docker-compose up
```
Once this is complete, navigate to `http://localhost:3000` in a browser to begin using the app.

---

## Uninstalling

Once you are finished with the app, you can close all the application resources by running the command: 
```bash
docker stop hypertrophy-edu_mongocontainer hypertrophy-edu_dbcontainer hypertrophy-edu_backendcontainer hypertrophy-edu_frontendcontainer
```

If you need to start the app up again, you can run: 
```bash
docker start hypertrophy-edu_mongocontainer hypertrophy-edu_dbcontainer hypertrophy-edu_backendcontainer hypertrophy-edu_frontendcontainer
```

If you want to uninstall the app resources without uninstalling docker, first stop all your containers, then run: 
```bash
docker rm hypertrophy-edu_dbcontainer hypertrophy-edu_mongocontainer hypertrophy-edu_backendcontainer hypertrophy-edu_frontendcontainer
```
then finally run:
```bash
docker rmi ghcr.io/camoroony/hypertrophy-edu-frontend:latest
docker rmi mongo:latest
docker rmi ghcr.io/camoroony/hypertrophy-edu-backend:latest
docker rmi mysql:8.0
```

To fully uninstall docker, follow these steps:

**Windows:**
- Open the Start menu and search for "Docker Desktop".
- Right-click on the Docker Desktop application and choose Uninstall.
- Follow the on-screen prompts to complete the uninstallation.

**MacOS:**
- Open Docker Desktop from the Applications folder.
- In the Docker menu (at the top-right of your screen), click on Preferences.
- Go to the Uninstall tab and click Uninstall.
  
---

## Feedback survey

The following project is my University Dissertation artefact.
For anyone who intends on using this, I would greatly appreciate if you would provide feedback on the project through [**This Survey**](https://docs.google.com/forms/d/e/1FAIpQLSdeeP_d0XTodh2ilcNOAn6Pl1wbi-zH2CmGvnUOIuM6lfaoEA/viewform?usp=dialog).

---

## Thanks

Thank you to all who have used this application and provded feedback on it for my dissertation, your the best! - Cameron :)

