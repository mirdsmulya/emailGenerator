
class emailGenerator(object):

    def __init__(self, domain):
        self.domain = domain 
    
    def toLower(self, word):
        result = word.lower()
        return result

    def split(self, word):
        result = word.split(' ')
        return result

    def oneWordName(self, words, number):
        return words[0] + str(number) 
        
    def moreThanOneWord(self, words, number):
        return words[0] + "." + words[-1] + str(number)
        
    def generateEmailName(self, words):
        return words + self.domain


if __name__ == "__main__":

    domain = "@paragraph.ai"
    database = {"mirdanx":0, 'halan sukur':2}


    while True:
        input = raw_input('Inputkan nama lengkap anda: \n > ')
        emGenerator = emailGenerator(domain)
        lowerChar = emGenerator.toLower(input)
        splittedChar = emGenerator.split(lowerChar)

        if lowerChar in database:
            number = database[lowerChar] + 1
            database[lowerChar] = number
        else:
            database[lowerChar] = 0
            number = ''

        lengthArray = len(splittedChar)

        if lengthArray == 1:
            userName = emGenerator.oneWordName(splittedChar, number)
        else:
            userName = emGenerator.moreThanOneWord(splittedChar, number)
    
        emailName = emGenerator.generateEmailName(userName)

        print "Username Anda:", userName
        print "Email anda   :", emailName
        print " "

    