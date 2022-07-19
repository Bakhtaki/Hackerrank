'''Solution to the problem "Hex Color Code" on HackerRank'''
# -----------------------------------------------------------------------------
# CSS colors are defined using a hexadecimal(HEX) notation for the combination
# of Red, Green, and Blue color values(RGB).
# Specifications of HEX Color Code
# It must start with a '#' symbol.
# It can have 3 or 6 digits.
# Each digit is a hex number from 0 to F.{0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F}
# A - F can be upper or lower case.
# Examples of HEX Color Code:

# Valid Hex Color Codes
# #FFF
# #025
# #F0A1FB

# Invalid Hex Color Codes
# #fffabg
# #abcf
# #12365erff

# Task:
# You are given N lines of CSS code. Your task is to print all
# valid Hex Color Codes, in order of their occurrence from top to bottom.
#
# Input Format:
# The first line contains, N the number of code lines.
# The next N lines contains CSS Codes
#
# Constraints:
# 1 < N < 50
#
# Output Format:
# Output the color codes with '#' symbols on separate lines.
#
# Sample Input:
# 11
# #BED
# {
#     color:  # FfFdF8; background-color:#aef;
#     font-size: 123px;
#     background: -webkit-linear-gradient(top,  # f9f9f9, #fff);
#                                         }
#     #Cab
#     {
#         background-color:  # ABC;
#         border: 2px dashed  # fff;
#     }
#
# Sample Output:
# #FfFdF8
# #aef
# #f9f9f9
# #fff
# #ABC
# #fff
# -----------------------------------------------------------------------------
# Solution:
import re

for i in range(int(input())):
    matches = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
    if matches:
        print(*matches, sep='\n')
