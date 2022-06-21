import unittest
from io import StringIO
import sys

# class StringIO(io.StringIO):
#     """
#     A "safely" wrapped version
#     """

#     def __init__(self, value=''):
#         value = value.encode('utf8', 'backslashreplace').decode('utf8')
#         io.StringIO.__init__(self, value)

#     def write(self, msg):
#         io.StringIO.write(self, msg.encode(
#             'utf8', 'backslashreplace').decode('utf8'))


def stub_stdin(testcase_inst, inputs):
    stdin = sys.stdin

    def cleanup():
        sys.stdin = stdin

    testcase_inst.addCleanup(cleanup)
    sys.stdin = StringIO(inputs)


def stub_stdouts(testcase_inst):
    stderr = sys.stderr
    stdout = sys.stdout

    def cleanup():
        sys.stderr = stderr
        sys.stdout = stdout

    testcase_inst.addCleanup(cleanup)
    sys.stderr = StringIO()
    sys.stdout = StringIO()


class TestExercise(unittest.TestCase):
    def test_1(self):
        stub_stdin(self, '42')
        stub_stdouts(self)
        import main
        self.assertEqual(sys.stdout.getvalue().strip(), '42\n'.strip())

if __name__ == '__main__':
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExercise)
    output = unittest.TextTestRunner(verbosity=2).run(suite)

    if output.wasSuccessful():
        f = open('.passed.json', 'w')
        f.close()
        print('Bravo ! Le code fourni a passé les tests avec succès, il semble valide !')