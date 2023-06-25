# Gym
## Start
```
pythom -m venv env
.\env\Scripts\activate
```

## Requrimientos
```
pythom -m venv env

pip install pysqlite
pip install Flask
```

## Backup Requiriments
```
pip freeze  > requirements.txt
```

## Restore Requiriments
```
pip install -U -r requirements.txt
```

## Update 
```
powershell -c "pip freeze  | %{$_.split('==')[0]} | %{pip install --upgrade $_}"
```

## Iniciar la BD
```
python init_db.py
```

## Ejecutar el app
``` 
python hola.py
```

# Informacion

Para informacion de [How To Use an SQLite Database in a Flask Application](https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application)