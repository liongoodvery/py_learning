import re
comment=re.compile(r'/\*((?:.|\s)*)\*/')
text1 = '/* this is a comment */'
text2 = '/*this a\n multiline comment*/'
print(comment.findall(text1))
print(comment.findall(text2))


comment=re.compile(r'/\*(.*)\*/',flags=re.DOTALL)
print(comment.findall(text1))
print(comment.findall(text2))
