import xml.etree.ElementTreeas as ET
data = '''
<person>
<name>Chuck</name>
<phone type="intl">
+1 734 303 4456
</phone>
<email hide="yes"/>
</person>
'''
tree = ET.fromstring(data)
print('Phone:',tree.find('phone').text)
print('Phone Type:',tree.find('phone').get('type'))
print('Attr:',tree.find('email').get('hide'))
