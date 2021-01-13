import re

def result():
    s = 'ACAABAACAAABACDBADDDFSDDDFFSSSASDAFAAACBAAAFASD'

    result = []
    # compete the pattern below
    pattern = '([A-Z]*?)AAA'
    for item in re.finditer(pattern, s):
      # identify the group number below.
      result.append(item.group())
      
    return result

print(result())