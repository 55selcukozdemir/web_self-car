from tkinter.ttk import setup_master
from flaskweb import app
from flaskweb.setupSql import Sql
from camera.CameraRead import CameraOpenCV
from threading import Thread

camera = CameraOpenCV()

def flaskRun():
    app.run(camera)
    

def cameraRun():
    camera.cameraRead("name")
    

t1 = Thread(target = flaskRun)
t1.start()


t2 = Thread(target = cameraRun)
t2.start()

sql = Sql()

sql.hsv_valuses(55,55,66,99,77,88)

sql.updateHsv(1111,89,66,99,77,88)
print(sql.getHsvValues()[0][2])



