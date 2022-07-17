import json
from flask import Flask, render_template, Response, request, jsonify
import cv2
import numpy as np
from threading import Thread

from camera.CameraRead import CameraOpenCV

# flask app setup
app = Flask(__name__ ,static_url_path="/static")



# video view stream route
# base
def gen_frames(): 
    while True:
        frame = camera_.getFrameBase()
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 


@app.route('/video_base')
def video_base():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# corner finded
def gen_frames_corner(): 
    while True:
        frame = camera_.getFrame()
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 


@app.route('/video_corner')
def video_corner():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')







@app.route('/')
def index():
    return render_template('index.html')


@app.route('/segment', methods = ['POST', 'GET'])
def segmetParameter():
    try:
        if request.method == 'POST':
            lower_h =  request.form.get("lower-h")
            lower_s =  request.form.get("lower-s")
            lower_v =  request.form.get("lower-v")

            upper_h =  request.form.get("upper-h")
            upper_s =  request.form.get("upper-s")
            upper_v =  request.form.get("upper-v")

            data = {
                "lower-h": lower_h,
                "lower-s": lower_s,
                "lower-v": lower_v,
                "upper-h": upper_h,
                "upper-s": upper_s,
                "upper-v": upper_v,
            }

            return data
    except: 
        return "mkdkmsfs"



# costum functions

def run(camera):
    global camera_
    camera_ = camera
    app.run()


