import re
s = 'ACAABAACAAABACDBADDDFSDDDFFSSSASDAFAAACBAAAFASD'

result = []
# compete the pattern below
pattern = '([B-Z])AAA'
print(re.finditer(pattern,s))
for item in re.finditer(pattern, s):
# identify the group number below.
  result.append(item.group())

