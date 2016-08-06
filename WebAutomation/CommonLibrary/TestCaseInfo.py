class TestCaseInfo(object):
    """description of class"""
    def __init__(self, id="",name="",owner="",result="Failed",starttime="",endtime="",secondsDuration="",errorinfo=""):
        self.id = id
        self.name = name
        self.owner = owner
        self.result = result
        self.starttime = starttime
        self.endtime = endtime
        self.secondsDuration = secondsDuration
        self.errorinfo = errorinfo

