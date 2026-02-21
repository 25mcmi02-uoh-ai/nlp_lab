import re

re.findall(r'[0-9]', "abc123xyz")
# ['1', '2', '3']
re.findall(r'[0-9]+', "abc123xyz")
# ['123']
re.findall(r'\d+', "abc123xyz")
# ['123']
re.findall(r'\d+', "abc123xyz0212_2")
# ['123', '0212', '2']
re.sub(r'\d+', r'*', "abc123xyz0212_2")
#'abc*xyz*_*'
re.subn(r'\d+', r'*', "abc123xyz0212_2")
# ('abc*xyz*_*', 3)


# tr -sc ’A-Za-z’ ’\n’ < shakes.txt | sort | uniq -c | sort –n –r