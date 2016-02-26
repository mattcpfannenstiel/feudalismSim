import unittest

from Fief import Fief
from Grain import Grain
from LandUnit import LandUnit
from Lord import Lord

class Test_Lord(unittest.TestCase):
    """
    This class is for specifically testing the Lord Class
    """
    def __init__(self, *args, **kwargs):
        """
        This makes a new instance of the Test Lord class
        :param level: The level of log to write to
        :param log: The log to be made for the Test
        """
        super(Test_Lord, self).__init__(*args, **kwargs)

    def setUp(self):
        """
        Sets up the instances of the classes need for the test of the Lord class
        """
        self.test_fief = Fief(0)
        self.test_grain = Grain(self.test_fief)
        self.test_fief.stores = self.test_grain
        self.test_lord = Lord("Lord 0", self.test_fief)
        self.test_fief.ruler = self.test_lord
        self.sidelength = 2
        i = 0
        j = 0
        while i < self.sidelength:
            j = 0
            while j < self.sidelength:
                land = LandUnit(i, j, self.test_fief)
                self.test_fief.containedLand.append(land)
                j += 1
            i += 1
        self.test_target = LandUnit(i - 1, j + 1, None)

    def tearDown(self):       
        print("Clean up done")


    def suite(self):
        """
        Creates a suite of tests to be run on the Lord class
        :return:
        """
        suite = unittest.TestSuite()
        suite.addTest(self.test_decision())
        suite.addTest(self.test_attack())
        suite.addTest(self.test_buyknight())
        suite.addTest(self.test_checkifdead())
        return suite

    def test_decision(self):
        """
        This is a battery of test to ensure the functionality of the decision method in Lord
        """
        self.setUp()
        self.test_lord.decision()
        self.assertNotEqual(self.test_lord.land.stores, None, "Wealth isn't None")
        self.assertEqual(self.test_lord.combatants.getknightcount(), 0, "There are knights in the army")
        self.assertEqual(self.test_lord.lookforwealthyland(), None, "Target returned isn't None")

    def test_attack(self):
        """
        This is a battery of tests for the attack method in the Lord class
        :return:
        """
        self.setUp()
        self.test_lord.combatants.setknightcount(100)
        self.test_enemy = Lord("Lord 1", None)
        self.test_enemy.combatants.setknightcount(50)
        self.test_enemyfief = Fief(1)
        self.test_enemyfief.containedLand.append(self.test_target)
        self.test_target.owner = self.test_enemyfief
        self.test_enemy.land = self.test_enemyfief
        self.test_enemyfief.ruler = self.test_enemy

        self.test_lord.attack(self.test_target)
        self.assertEqual(self.test_target.owner.ruler.getname(), self.test_lord.getname(), "Lord 0 hasn't taken target")

    def test_buyknight(self):
        """
        This is a test to ensure the functionality of buyknight in the Lord class
        """
        self.setUp()
        temp = self.test_lord.combatants.getknightcount()
        self.test_lord.land.stores.setwealth(100)
        self.test_lord.buyknight()
        self.assertEqual(temp + 1, self.test_lord.combatants.getknightcount(),
                         "The number of knights hasn't increased by 1")

    def test_checkifdead(self):
        """
        Tests the functionality of the check if dead method in the Lord class
        """
        self.setUp()
        fate = self.test_lord.checkifdead()
        self.assertEqual(fate, False, "Lord is dead")

    def runTest(self):
        t = Test_Lord()
        suite = t.suite()

