# “I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my
# fear. I will permit it to pass over me and through me. And when it has gone past I will turn the inner eye to see
# its path. Where the fear has gone there will be nothing. Only I will remain.” – Frank Herbert, Dune

import re

search_string = "“I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. " \
                "I will face my fear. I will permit it to pass over me and through me. And when it has gone past I " \
                "will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will " \
                "remain.” – Frank Herbert, Dune "
withF = re.findall(r"\w*f\w*", search_string, flags=re.IGNORECASE)
print(withF, len(withF))
startF = re.findall(r"f\w*", search_string, flags=re.IGNORECASE)
print(startF, len(startF))
findNot = re.findall("not", search_string, flags=re.IGNORECASE)
print(findNot, len(findNot))

replaceI = re.sub(r"\b[I]\b", "you", search_string, flags=re.IGNORECASE)
replaceMy = re.sub("my", "your", replaceI, flags=re.IGNORECASE)
replaceMe = re.sub("me", "you", replaceMy, flags=re.IGNORECASE)
print(replaceMe)
