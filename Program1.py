name=input('Enter file:') 
# inuput mehtod is giving the given file path as string to the name varaible
print(name)
handle=open(name)
# open methods opens the file and returns an iterateable file object

counts = dict()
# initializes an empty dictionary

for line in handle:
# first line of loop iterating over file String stored in handle variable
    words=line.split()
    # split the line from blank spaces and will return an list to the words variable
    for word in words:
        # loop to iterate over the words list, each time will give one value i.e one word
        counts[word]=counts.get(word,0)+1
        # if the word is present in counts it will give the value, add 1 to it and set the new value
        #  otherwise it will return 0
        #  and 1 is added, returned and set to that word value

# None is used to initialize a variable with no value or null value, it prevents
#  from errors as compared to uninitialized variables
bigCount= None
# initializes a variable with value None
bigWord = None
# initializes a variable with value None

for word,count in counts.items():
    # count.items() method will give a list to iterate over each key/value in dictionary
    # in word pointer we will get key 
    # and in count will get the value
    if bigCount is None or count > bigCount:
        # check if bigCount value is None or the current count value is greate than bigCount, execute this block
        bigWord=word
        # set the bigWord value to that value that has greater count
        bigCount=count
        # set the bigCount value to that value that has greater count

print(bigWord, bigCount)
# printing value of bigWord and bigCount variables