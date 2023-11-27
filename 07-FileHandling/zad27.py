import re

message = "To be, or not to be, that is the question"

words = re.split(" ", message)
print(len(words))