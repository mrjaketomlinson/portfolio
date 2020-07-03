from flask import Flask, render_template
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Start Flask App and App Config
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


# Front page route
@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
