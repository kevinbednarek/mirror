from flask import Flask, render_template
from mouse import get_mouse
from handrecognition import hand_stuff

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/kevin')
def kevin():
    return render_template('kevin.html')


@app.route('/background_process_test')
def background_process_test():
    print("Hands???")
    get_mouse()
    return "nothing"


# For Raspberry PI
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')

# For development
if __name__ == '__main__':
    hand_stuff()
    # get_mouse()
    # app.run(debug=True, port=8001)
