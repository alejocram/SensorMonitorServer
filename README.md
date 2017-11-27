# SensorMonitorServer

Created a MongoDB database, you can use mLab.com that is an open services 

## Dependecies 
Python
Flask
PyMongo


## Deploy
python sensor_monitor.py

## Add record in database 
POST http://<host>:5000/add
{
  "var1": "12",
  "var2": "76"
}
