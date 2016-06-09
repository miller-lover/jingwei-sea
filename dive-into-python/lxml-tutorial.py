from lxml import etree

tree = etree.parse('feed.xml')
root = tree.getroot()
for e in root.findall('{http://www.w3.org/2005/Atom}entry'):
    print(e)
    print(e.attrib)

print('\n')
'''
This query finds all elements in the Atom namespace, anywhere in the document, that have an href
attribute. The // at the beginning of the query means “elements anywhere (not just as children of the root
element).” {http://www.w3.org/2005/Atom} means “only elements in the Atom namespace.” * means
“elements with any local name.” And [@href] means “has an href attribute.”
'''
for e in tree.findall('//{http://www.w3.org/2005/Atom}*[@href]'):
    print(e)
    print(e.attrib)

print('\n')

for e in tree.findall("//{http://www.w3.org/2005/Atom}*[@href='http://diveintomark.org/']"):
    print(e)
    print(e.attrib)

print('query searches for Atom author elements that have an Atom uri element as a child.\n')
NS = '{http://www.w3.org/2005/Atom}'
for e in tree.findall('//{NS}author[{NS}uri]'.format(NS=NS)):
    print(e)

'''
To perform XPath queries on namespaced elements, you need to define a namespace
prefix mapping. This is just a Python dictionary.
'''
nsmap = {'atom': 'http://www.w3.org/2005/Atom'}
'''
The XPath expression searches for category elements (in the Atom namespace)
that contain a term attribute with the value accessibility. Did you notice the /.. bit?
That means “and then return the parent element of the category element you just found.”
'''
entries = tree.xpath("//atom:category[@term='accessibility']/..", namespaces=nsmap)
print(entries)

entry = entries[0]
'''
XPath expressions don’t always return a list of elements. Technically, the DOM of a parsed XML document
doesn’t contain elements; it contains nodes. Depending on their type, nodes can be elements, attributes, or
even text content. The result of an XPath query is a list of nodes. This query returns a list of text nodes:
the text content (text()) of the title element (atom:title) that is a child of the current element (./).
'''
print(entry.xpath('./atom:title/text()', namespaces=nsmap))
