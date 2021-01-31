from flask import Flask
app = Flask(__name__)



@app.route('/')
def get_dashboard():
    import actions.getDashBoard as getDashBoardModule
    return getDashBoardModule.GetDashBoardAction().do()

