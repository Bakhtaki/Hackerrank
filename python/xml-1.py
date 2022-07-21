'''Solution to the XML 1 challenge from Hackerrank'''
# ---------------------------------------------------------------
# Task:
# Yoy are given a valid XML document, and you have to print
# its score.
# The score is calculated by the sum of the  each element's score.
# for any element in the XML documents score is equal to the number
# attribute of the element.
# Input Format:
# The first line contains the integer N, the number of line
# in the XML document.
# The next N lines contains the XML document.
#
# Sample Input:
# 6
# <feed xml:lang='en'>
#     <title>HackerRank</title>
#     <subtitle lang='en'>Programming challenges</subtitle>
#     <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
#     <updated>2013-12-25T12:00:00</updated>
# </feed>
#
# Sample Output:
# 5
# ---------------------------------------------------------------
# Solution:
import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    # your code goes here
    return sum(len(child.attrib) for child in node.iter())


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
