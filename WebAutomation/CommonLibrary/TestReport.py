from xml.etree import ElementTree as ET
import os
import lxml.etree as mytree
from io import StringIO, BytesIO
from lxml import html
import ResultFolder
class TestReport(object):
    """description of class"""
    def __init__(self):
        #self.testreport = "TestResult.xml"
        self.reportfile = ResultFolder.GetRunDirectory()+"\TestResult.html"

    #Create init test report file
    def CreateHtmlFile(self):
        if os.path.exists(self.reportfile) == False:
            f = open(self.reportfile,'w')
            message = """<html>
            <head>    
                <title>Automation Test Result</title>
                <style>
                    table {
			                border-collapse: collapse;
			                padding: 15px;
			                font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
		                    }
		            th{
			            background-color: green;
			            color: white;
			            border: 1px solid #ddd;
			            padding-bottom: 15px;
			            padding-top: 15px;
		            }
		            tr{
			            border: 1px solid #008000;
			            padding-bottom: 8px;
			            padding-top: 8px;
			            text-align: left;
		            }
                    td{
                        border: 1px solid #008000;
                    } 
                </style>
            </head>
            <body>
                <h1>Automation Test Result</h1>
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Owner</th>
                        <th>Result</th>
                        <th>StartTime</th>
                        <th>EndTime</th>
                        <th>Duration(s)</th>
                        <th>ErrorMessage</th>
                   </tr>
                </table>
            </body>
            </html>
            """
            f.write(message)
            f.close()


    def WriteHTML(self,testcaseinfo):

        self.CreateHtmlFile()

        f = open(self.reportfile,"r")
        
        htmlcontent = f.read()
        f.close()
        #tree = mytree.fromstring(str(htmlcontent))
        htmlcontent.encode('utf-8')
        tree = html.fromstring(htmlcontent)
        tableElem = tree.find(".//table")
        if testcaseinfo.result == "Failed":
            mytablerow = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td bgcolor=\"#FF0000\">{3}</td><td>{4}</td><td>{5}</td><td>{6}</td><td>{7}</td></tr>".format(testcaseinfo.id,testcaseinfo.name,testcaseinfo.owner,testcaseinfo.result,testcaseinfo.starttime,testcaseinfo.endtime,testcaseinfo.secondsDuration,testcaseinfo.errorinfo)
        else:
            mytablerow = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td><td>{6}</td><td>{7}</td></tr>".format(testcaseinfo.id,testcaseinfo.name,testcaseinfo.owner,testcaseinfo.result,testcaseinfo.starttime,testcaseinfo.endtime,testcaseinfo.secondsDuration,testcaseinfo.errorinfo)
        tableElem.append(mytree.HTML(str(mytablerow)))

        f = open(self.reportfile,"w")
        #html.tostring
        newContent = repr(html.tostring(tree,method="html",with_tail=False))
        newContent = newContent.replace(r"\n","").replace(r"\t","").replace('b\'',"")
        newContent = newContent[:len(newContent)-1]
        f.write(newContent)
        f.close()


        