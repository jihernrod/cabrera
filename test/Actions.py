
import unittest

import actions.getDashBoard as getDashBoardAction

class TestActionsClass(unittest.TestCase):

    def test_GetDashBoardAction(self):
        getDashBoardAction.GetDashBoardAction().do()



if __name__ == '__main__':
    unittest.main()