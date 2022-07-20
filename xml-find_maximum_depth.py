'''
Solution to the XML Maximum Depth problem
Hackerrank.com/challenges/xml-find-maximum-depth/problem
'''
# ---------------------------------------------------------------
# You are given a valid XML document, and you have to print
# the maximum level of nesting in it. Take the depth of the root as 0.
# Input Format
# The first line contains, the number of  N lines in the XML document.
# The next N lines follow containing the XML document.
# Output Format
# Output a single line, the integer value of the maximum level of
# nesting in the XML document.
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
# 1
# -----------------------------------------------------------------------------
# Solution:
import xml.etree.ElementTree as etree

maxdepth = 0


def depth(elem, level):
    global maxdepth
    # your code goes here
    if level == maxdepth:
        maxdepth += 1
    for child in elem:
        depth(child, level + 1)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
