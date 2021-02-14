from flask import Flask
app = Flask(__name__)



@app.route('/')
def get_dashboard():
    import actions.getDashBoard as getDashBoardModule
    import adapters.getDashBoardMatrixAdapter as getDashBoardMatrixAdapter
    return getDashBoardMatrixAdapter.GetDashBoardActionMatrixAdapter().adapt(
                                                                        getDashBoardModule.GetDashBoardAction().do())




