
import unittest

import actions.getDashBoard as getDashBoardAction
import adapters.getDashBoardMatrixAdapter as getDashBoardMatrixAdapter

class TestActionsClass(unittest.TestCase):

    def test_GetDashBoardAction(self):
        getDashBoardMatrixAdapter.GetDashBoardActionMatrixAdapter().adapt(getDashBoardAction.GetDashBoardAction().do())



if __name__ == '__main__':
    unittest.main()