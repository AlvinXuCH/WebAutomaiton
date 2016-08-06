import subprocess
from datetime import datetime
import LogUtility
import EmailUtils

class RunTests(object):
    """description of class"""
    def __init__(self):
        self.testcaselistfile = "testcases.txt"
        

    def LoadAndRunTestCases(self):
        try:
            f = open(self.testcaselistfile)
            testfiles = [test for test in f.readlines() if not test.startswith("#")]
            f.close()
            for item in testfiles:
                subprocess.call("nosetests TestCasesRepository\\"+str(item).replace("\\n",""),shell = True)
        except Exception as err:
            LogUtility.logger.debug("Failed running test cases, error message: {}".format(str(err)))
        finally:
            EmailUtils.send_report()

    def CreateRunFolder(self):
        try:
            time = datetime.now()
            subprocess.call("mkdir TestRun_"+time.strftime("%Y_%m_%d_%H_%M_%S"),shell=True)
        except Exception as err :
            LogUtility.logger.debug("Failed creating run folder, error message: {}".format(str(err)))

if __name__ == "__main__":
    newrun = RunTests()
    newrun.CreateRunFolder()
    newrun.LoadAndRunTestCases()
    
