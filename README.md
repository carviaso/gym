# Gym

## Requrimientos
```
pip install pysqlite
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