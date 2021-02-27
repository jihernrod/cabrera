


class RequestDashboardAddapter:

    def __init__(self, parameters, value):

        self._parameters = parameters
        self._value = value

    def get(self, param):
        ret_value = []
        for response_list in self._value["Values"]:
            for items in response_list:
                ret_value.append( items )
        print (ret_value)
        return ret_value