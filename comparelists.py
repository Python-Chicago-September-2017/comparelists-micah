
list_one = [1,2,5,6,2]
list_two = [1,2,4,6,2]

"""list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
"""

identical = True
for i in range(0, len(list_one)):
    if list_one[i] != list_two[i]:
        identical = False
        break

if identical:
    print "The lists are the same."

else: 
    print "The lists are not the same."
