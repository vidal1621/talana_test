# talana_test
tener un archivo requirements.txt en el mismo directorio que el Dockerfile, que contenga las dependencias necesarias para Flask
ejemplo
Flask==2.0.1
para crear el contenedor con docker primero
docker build -t pelea-app . 
luego para correr el contenedor
docker run -p 5000:5000 pelea-app
```
