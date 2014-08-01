from redmine import Redmine

import csv
import codecs
import time


redmine = Redmine('https://www.hostedredmine.com', key='ADD My API KEY HERE')

project = redmine.project.get('epubs-for-project-madurai-ebooks')
print project



book_no=1
with open('books.csv', 'rb') as f:
    reader = f.readlines()
    for row in reader:
    
        image_number = '%0*d' % (3, int(book_no) )

        no = row.split('$')[0]
        book_name =  row.split('$')[1].decode('utf-8')
        author= row.split('$')[2].decode('utf-8')
        urls = row.split('$')[4]

#        print author

        if "&" in urls:
#            for link in urls:
                url = urls.split('&')
                for i in url:
                    book_url = "http://www.projectmadurai.org/pm_etexts/utf8/" + i.strip()

#                    print book_url
        else:
            book_url ="http://www.projectmadurai.org/pm_etexts/utf8/" +  urls
#            print book_url + "\n"

        
        
        cover_url = "http://freetamilebooks.com/htmlbooks/project-madurai-cover-images/" + image_number + ".jpg"
        
#        print cover_url    
        print "Importing Book " + str(book_no) + "   " + book_name
#
        desc = "Book Name : " + book_name + "\n" + "Author : " +  author + "\n" + "Book Url : " + book_url + "\n" + "Cover Image : " + cover_url

        print desc
        new_book = redmine.issue.create(project_id='epubs-for-project-madurai-ebooks',subject=book_name,description=desc)
        print "================\n\n"

        book_no = book_no + 1
        
        time.sleep(1)
