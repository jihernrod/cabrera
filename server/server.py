from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/get', methods=['POST', 'GET'])
def get_dashboard():
    import actions.getDashBoard as getDashBoardModule
    import adapters.getDashBoardMatrixAdapter as getDashBoardMatrixAdapter
    import adapters.RequestAddapter as RequestDashboardAddapter

    rda = RequestDashboardAddapter.RequestDashboardAddapter(request.args,
                                                            request.json)

    return getDashBoardMatrixAdapter.GetDashBoardActionMatrixAdapter().adapt(
                                                                        getDashBoardModule.GetDashBoardAction(rda).do())


if __name__=="__main__":
    app.run()

