from redmine import Redmine
import csv
import codecs

redmine = Redmine('http://demo.redmine.org', username='', password='Vanakkam@1')

redmine = Redmine('https://www.hostedredmine.com', key='b7780b63000c6181d2ce0a38f753396115331b8f')

project = redmine.project.get('project-madurai')
print project

issue = redmine.issue.get('322281')
print issue



with open('index-all.csv', 'rb') as f:
    reader = f.readlines()
    for row in reader:
    
        no = row.split('$')[0]
        book_name =  row.split('$')[1].decode('utf-8')
        author= row.split('$')[2].decode('utf-8')
        print "Importing Book " + book_name

        new_book = redmine.issue.create(project_id='project-madurai-epubs',subject=book_name,description=book_name + "  " + author)


