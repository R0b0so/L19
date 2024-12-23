def Match_Words(words):
 count = 0
 list = []
 for word in words:
  if len(word) > 1 and word[0] == word[-1]:
   count += 1
   list.append(word)
 print("List words with the same first and last character \n", list)
 return count
counter = Match_Words(['asd', 'rer', 'uku', 'wieu', '1199', '2022'])
print("Number of words having the same first and last character:", counter)