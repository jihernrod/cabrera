
import configuration.constants as Constants

class GetDashBoardActionMatrixAdapter:

    def __init__(self):
        self.types_value = [Constants.TYPE_STR,
                           Constants.TYPE_FLOAT,
                           Constants.TYPE_FLOAT,
                           Constants.TYPE_STR,
                           Constants.TYPE_STR,
                           Constants.TYPE_FLOAT,
                           Constants.TYPE_FLOAT,
                           Constants.TYPE_FLOAT,
                           Constants.TYPE_FLOAT,
                           Constants.TYPE_FLOAT,
                           Constants.TYPE_FLOAT,
                           Constants.TYPE_FLOAT,
                            Constants.TYPE_FLOAT]

    def adapt(self, dashBoardActionObject):

        ret = {"Header": [], "Types": [], "Values":[]}

        if not dashBoardActionObject:
            return ret

        if len(dashBoardActionObject) == 0:
            return ret

        index = 0
        for ticker, obj in dashBoardActionObject.items():
            value = []
            if index == 0 :
                ret["Header"] = list(obj.keys())
                ret["Types"] = self.types_value
                for k, v in obj.items():
                    value.append(v)
            else:
                for k, v in obj.items():
                    value.append(v)
            ret["Values"].append(value)
            index += 1

        return ret

