import time, random

print(time.time())

def nextTime(x):
        return (time.time() + float(x))

def fragmentLines(inputString):
        numberOfWords = inputString.split(' ')
        returnString = ''
        numberOfChars = 0
        charsPerLine = 50

        for word in numberOfWords:
                previousNumberOfChars = numberOfChars
                numberOfChars = numberOfChars + len(word)

                if numberOfChars > charsPerLine and previousNumberOfChars != 0:
                        returnString = '\n' + word
                        numberOfChars = len(word)
                else:
                        if returnString == '':
                                returnString += word
                        else:
                                returnString += ' ' + word

        return returnString
                        

timeToRefresh = 12
timeForBullet = 1

fAllMessagesAndAuthors = open("allmessages.txt","r")
allPotentialMessages = fAllMessagesAndAuthors.readlines()
fAllMessagesAndAuthors.close()

currentMessage = ''

nextRefresh = nextTime(0)
nextBullet = nextTime(timeForBullet)

numBullets = 1

while True:
        
        currentTime = time.time()
        
        if currentTime >= nextRefresh:
        
                line = random.randint(0, len(allPotentialMessages)-1)
                #print(line)
                lineOfMessage = allPotentialMessages[line]

                currentMessage, author = lineOfMessage.split(';')

                currentMessage = fragmentLines(currentMessage)
                author = fragmentLines(author)

                fCurrentMessage = open("titlecard.txt","w+")
                fCurrentAuthor = open("author.txt","w+")

                fCurrentAuthor.write(author)

                fCurrentMessage.write(currentMessage)

                fCurrentAuthor.close()
                fCurrentMessage.close()
                
                nextRefresh = nextTime(timeToRefresh)
                nextBullet = nextTime(0)
                
                numBullets = 0

                #print(currentMessage)
                
        if currentTime >= nextBullet:
                
                if numBullets <= 3:

                        newMessage = currentMessage
                        for i in range(numBullets):
                                newMessage = newMessage + '.'

                        fCurrentMessage = open("titlecard.txt","w+")
                        fCurrentMessage.write(newMessage)
                        fCurrentMessage.close()

                        
                        numBullets = numBullets + 1

                        nextBullet = nextTime(timeForBullet)

                        print(newMessage)
                
                else:
                
                        newMessage = currentMessage

                        fCurrentMessage = open("titlecard.txt","w+")
                        fCurrentMessage.write(newMessage)
                        fCurrentMessage.close()
                        
                        numBullets = 1

                        nextBullet = nextTime(timeForBullet)

                        print(newMessage)
