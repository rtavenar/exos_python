import unittest

class TestExercise(unittest.TestCase):
    def test_all(self):
        {}

if __name__ == '__main__':
    try:
        from main import *
    except:
        print("Le code fourni n'est pas valide")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExercise)
    output = unittest.TextTestRunner(verbosity=2).run(suite)

    if output.wasSuccessful():
        f = open('.passed.json', 'w')
        f.close()
        print('Bravo ! Le code fourni a passé les tests avec succès, il semble valide !')