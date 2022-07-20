'''Solution for HTML Parser part 1 HackerRank.com'''
# -----------------------------------------------------------------------------
# Task:
# You are given an HTML code snippet of N lines.
# Your task is to print start tags, end tags and empty tags separately.
# format result as follows:
# Start: Tag1
# End: Tag1
# Start: Tag2
# -> Attribute2[0] = Attribute_Value2[0]
# -> Attribute2[1] = Attribute_Value2[1]
# -> Attribute2[2] = Attribute_Value2[2]
# Start: Tag3
# -> Attribute3[0] = None
# Empty: Tag4
# -> Attribute4[0] = Attribute_Value4[0]
# End: t=Tag3
# End: Tag2

# Note: Do not detect any HTML tag, attribute or attribute
# value inside the HTML
# comment tags (<!-- Comments -->).Comments can be multiline as well.

# Input Format:
# The first line contains an integer N, the number of lines in the HTML code.
# The next N lines contain HTML code.

# Constraints:
# 1 <= N <= 100

# Output Format:
# Print the HTML tags, attributes and attribute values in order of their
# occurrence from top to bottom in the given snippet.
# Use proper formatting as explained in the problem statement

# Sample Input:
# 2
# <html > <head > <title > HTML Parser - I < /title > </head >
# <body data-modal-target class = '1' > <h1 > HackerRank < /h1 > <br / >
# <html /body > </html >

# Sample Output:

# Start: html
# Start: head
# Start: title
# End: title
# End: head
# Start: body
# -> data-modal-target > None
# -> class > 1
# Start: h1
# End: h1
# Empty: br
# End: body
# End: html

# ------------------------------------------------------------------------------

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for name, value in attrs:
            print("->", name+" >", value)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for name, value in attrs:
            print("->", name+" >", value)


# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
n = int(input())
for _ in range(n):
    parser.feed(input())

