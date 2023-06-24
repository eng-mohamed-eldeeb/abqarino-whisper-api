# import whisper
# import sys
# from flask import Flask
# from flask_socketio import SocketIO, emit

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your-secret-key'

# socketio = SocketIO(app, cors_allowed_origins="*")

# @app.route('/recpy')
# def index():
#     model = whisper.load_model("small")
#     result = model.transcribe("audio.mp3")
#     return result["text"].encode('utf-8').decode(sys.stdout.encoding)


# if __name__ == '__main__':
#     socketio.run(app, host='localhost', port=5000)
# # will this python code work?

import whisper
import sys
import os
from flask import Flask

app = Flask(__name__)
model = whisper.load_model("small")
env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route('/')
def index():
    model = whisper.load_model("small")
    result = model.transcribe("audio.mp3")
    return ( result["text"].encode('utf-8').decode(sys.stdout.encoding))

if __name__ == '__main__':
    app.run()