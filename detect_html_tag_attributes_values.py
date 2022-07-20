'''
Solution for the detect_html_tag_attributes_values problem.
HackerRank.com
'''
# ----------------------------------------------------------------
# You  are given an HTML code snippet of N lines.
# Your  task is to print all html tags,attribute names and attribute values.
# print detected items in the following format:
#
# Tag1
# Tag2
# -> Attribute2[0] > Attribute_value2[0]
# -> Attribute2[1] > Attribute_value2[1]
# -> Attribute2[2] > Attribute_value2[2]
# Tag3
# -> Attribute3[0] > Attribute_value3[0]
# The symbol "->" indicates that the tag is contains an attribute.
# it is immediately followed by the name of the attribute and the attribute
# value.
# The symbol > acts as a separator for the attribute name and attribute value.
# if an HTML tag has no attribute, then simply print the tag name.
#
# Note: Dont detect any html tag inside the HTML comment <!--->
# all attributes have values.
#
# Input Format
# The first line contains an integer N, the number of lines in the
# HTML code snippet.
# The next N lines contain HTML code.
#
# Constraints:
# 0 < N < 100
#
# Output Format:
# Print the HTML tags, attributes and attribute values in order of their
# occurrence from top to bottom in the snippet.
# Format your answers as explained in the problem statement.
#
# Sample Input:
# 9
# <head>
# <title>HTML</title>
# </head>
# <object type="application/x-flash"
#   data="your-file.swf"
#   width="0" height="0">
#   <!-- <param name="movie" value="your-file.swf" /> -->
#   <param name="quality" value="high"/>
# </object>
#
# Sample Output:
# head
# title
# object
# -> type > application/x-flash
# -> data > your-file.swf
# -> width > 0
# -> height > 0
# param
# -> name > quality
# -> value > high
# -----------------------------------------------------------------------
# Solution:
from html.parser import HTMLParser


# Customized HTML Parser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print('->', attr[0], '>', attr[1])


n = int(input())
data = ''

for i in range(n):
    data += input() + '\n'

parser = MyHTMLParser()
parser.feed(data)
