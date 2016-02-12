import unittest

from Fief import Fief
from LandUnit import LandUnit
from Lord import Lord
from Gollyhandler import Gollyhandler


class Test_Lord(unittest.TestCase):
    def __init__(self, classname, level, popup, log):
        super(Test_Lord, self).__init__()
        self.testarea = classname
        self.urgency = level
        self.message = popup
        self.log = " "
        self.gollyh = Gollyhandler()

    def setUp(self):
        self.test_fief = Fief(0)
        self.test_lord = Lord("Lord 0", self.test_fief)
        self.test_fief.ruler = self.test_lord
        self.sidelength = self.gollyh.getuserinputint("Side length of square fief", "2")
        i = 0
        j = 0
        while i < self.sidelength:
            j = 0
            while j < self.sidelength:
                land = LandUnit(i, j, self.test_fief)
                self.test_fief.containedLand.append(land)
                self.gollyh.cellchange(i, j, 1)
                j += 1
            i += 1
        self.test_target = LandUnit(i - 1, j + 1, None)
        self.gollyh.cellchange(i - 1, j + 1, 1)

    def tearDown(self):
        self.doCleanups()
        self.gollyh = None
        self.test_fief = None
        self.test_lord = None
        print("Cleanup done")

    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(self.test_decision())
        suite.addTest(self.test_attack())
        suite.addTest(self.test_buyknight())
        suite.addTest(self.test_checkifdead())
        return suite

    def test_decision(self):
        self.test_lord.decision()
        self.assertEqual(self.test_lord.land.attackoptions, None, "Attack options are not none")
        self.assertIsInstance(self.test_lord.land.attackoptions, [], "Attack options is list")
        self.assertEqual(self.test_lord.land.stores, None, "Wealth is None")
        self.assertEqual(self.test_lord.combantants.getknightcount(), 0, "There are no knights in the army")
        self.assertEqual(self.test_lord.lookforwealthyland(), None, "Target returned is None")

    def test_attack(self):
        self.test_lord.combantants.setknightcount(100)
        self.test_enemy = Lord("Lord 1", None)
        self.test_enemy.combatants.setknightcount(50)
        self.test_enemyfief = Fief(1)
        self.test_enemyfief.containedLand.append(self.test_target)
        self.test_enemy.land = self.test_enemyfief
        self.test_enemyfief.ruler = self.test_enemy

        self.test_lord.attack(self.test_target)
        self.assertEqual(self.test_target.owner.ruler.getname(), self.test_lord.getname(), "Lord 0 has taken target")

    def test_buyknight(self):
        temp = self.test_lord.combatants.getknightcount()
        self.test_lord.land.stores.setwealth(100)
        self.test_lord.buyknight()
        self.assertEqual(temp + 1, self.test_lord.combantants.getknightcount(),
                         "The number of knights has increased by 1")

    def test_checkifdead(self):
        fate = self.test_lord.checkifdead()
        self.assertEqual(fate, False, "Lord isn't dead")
