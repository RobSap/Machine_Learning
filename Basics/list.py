#This is practice problems

myList = ['tacos' , 'burger', 1 , 2 , 3]

print "\nPrinting my list"
print myList

print "\nPringing burger"
print myList[1]

print "\nDelete tacos"
del myList[0];

print "\nPrinting my List"
print myList

myList.append(3)
print "\nAppend: 3 "
print  myList

print "\nInsert: 4"
#Insert at position 1, value 0
myList.insert(1, 0)
print myList

print "\nAdd tacos, and abc to end of list"
array= [ 'tacos' , 'a','b','c']
myList.extend(array)
print myList

print "\nremove an element"
myList.remove('tacos')
print myList

print "\nPop"
myList.pop()
print myList

print "\n Print where 1 is, index: "
print myList.index(1)

print "\nPrint my list reversed"
myList.reverse()
print myList
