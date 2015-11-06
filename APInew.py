API Assignment

#Question 1 - Filter to just Hillary Clinton's e-mails (case number F-2014-20439)
urllib2.urlopen('https://foia.state.gov/Search/results.aspx?searchText=*&beginDate=&endDate=&publishedBeginDate=&publishedEndDate=&caseNumber=F-2014-20439').read()

#Question 2 - Search for Benghazi
urllib2.urlopen('https://foia.state.gov/Search/results.aspx?searchText=Benghazi&beginDate=&endDate=&publishedBeginDate=&publishedEndDate=&caseNumber=F-2014-20439').read()

#Question 3
import urllib2, json

dirty_json = urllib2.urlopen('https://foia.state.gov/Search/results.aspx?searchText=Benghazi&beginDate=&endDate=&publishedBeginDate=&publishedEndDate=&caseNumber=F-2014-20439').read()
valid_json = clean_json(dirty_json)
	response = urllib2.urlopen('https://foia.state.gov/Search/results.aspx?searchText=Benghazi&beginDate=&endDate=&publishedBeginDate=&publishedEndDate=&caseNumber=F-2014-20439').read()

data = json.loads(response)

    for "pdfLink" in data
        print .pdf