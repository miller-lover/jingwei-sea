import xml.etree.ElementTree as etree

'''
To add attributes to the newly created element, pass a dictionary of attribute names and values in the
attrib argument. Note that the attribute name should be in the standard ElementTree format, {namespace}localname
'''
new_feed = etree.Element('{http://www.w3.org/2005/Atom}feed',
    attrib={'{http://www.w3.org/XML/1998/namespace}lang': 'en'})
# At any time, you can serialize any element (and its children) with the ElementTree tostring() function.
print(etree.tostring(new_feed))

import lxml.etree as etree

NSMAP = {None: 'http://www.w3.org/2005/Atom'}
new_feed = etree.Element('feed', nsmap = NSMAP)
print(etree.tounicode(new_feed))
new_feed.set('{http://www.w3.org/XML/1998/namespace}lang', 'en')
print(etree.tounicode(new_feed))
title = etree.SubElement(new_feed, 'title', attrib={'type':'html'})
print(etree.tounicode(new_feed))
title.text = 'dive into &hellip;'
print(etree.tounicode(new_feed, pretty_print=True))

et = etree.ElementTree(new_feed)
et.write('generated.xml', pretty_print=True)
