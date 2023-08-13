from flask import Flask, render_template, Response

from camera import VideoCamera


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashbord.html")
def dashbord():
    return render_template("dashbord.html")


@app.route("/exercise_select.html")
def exercise_select():
    return render_template("exercise_select.html")


@app.route("/planworkout.html")
def planworkout():
    return render_template("planworkout.html")


@app.route('/shoulder.html')
def sample():
    return render_template('shoulder.html')


@app.route('/video_feed1')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type : image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
