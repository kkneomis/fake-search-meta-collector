import os
import json
import lxml.html
import requests
pages = []

rootdir = '/Users/simeonkakpovi/Documents/hu_webmaster/bschoolbeta'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if ('html' in file) and ('partial' not in subdir):
            try:
                with open(os.path.join(subdir, file)) as f:
                    page = f.read()
            except:
                #print 'could not open file: ' + file
                break
                
            current = {}
            
            try:
                tree = lxml.html.fromstring(page)
            except:
                #print 'something went wrong: ' + file
                pass
                
            try:
                pre = subdir
                pre = pre.replace('/Users/simeonkakpovi/Documents/hu_webmaster/bschoolbeta', '..')
                #print os.path.join(pre, file)
                current['url'] = os.path.join(pre, file)
            except:
                current['url'] = ''
                #print 'something went wrong'
           
            try:
                current['title'] = tree.xpath('//title/text()')[0]
            except:
                current['title'] = ''
                #print 'something went wrong with the title'
            
            try:
                current['text']  = tree.xpath('//meta[@name="description"]/@content')[0]
            except:
                current['text'] = ''
                #print 'something went wrong with the ext'
            
            try:
                current['tags'] = tree.xpath('//meta[@name="keywords"]/@content')[0]
            except:
                current['tags'] = ''
                #print 'something went wrong with tags'
            
            pages.append(current)
            
        
            
print json.dumps(pages)
