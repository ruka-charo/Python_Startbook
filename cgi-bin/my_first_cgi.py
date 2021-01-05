#!/usr/bin/env python

import cgitb
cgitb.enable()

html_body = '''<!DOCTYPE html>
<html lang='ja'>
  <head>
    <meta charset='UTF-8'>
    <title>CGI</title>
  </head>
  <body>
    初めてのCGI
  </body>
</html>'''

print('Content-type: text/html')
print('')
print(html_body)
