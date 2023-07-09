from flask import Flask
from controllers.daily_list_controller import select_relevant_episodes_from_search

app = Flask(__name__)

# startup checks detect if a container has started successfully which will then kickoff the liveness and readiness checks
@app.route('/startup/', methods=['GET'])
def startup_check():
    return "Startup check succeeded."

# liveness checks detect deployment containers that transition to an unhealthy state and remedy said situations through targeted restarts
@app.route('/liveness/', methods=['GET'])
def liveness_check():
    return "Liveness check succeeded."

# readiness checks tell our load balancers when a container is ready to receive traffic
@app.route('/readiness/', methods=['GET'])
def readiness_check():
    return "Readiness check succeeded."

@app.route('/', methods=['GET'])
#async def root():
def root():
    return {"message": "Welcome to my Flask app!"}

# Add additional endpoints below
@app.route("/v2/generate_learn_list")
def handle_generate_learn_list():
    return select_relevant_episodes_from_search()