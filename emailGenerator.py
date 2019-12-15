
class emailGenerator(object):

    def __init__(self, domain):
        self.domain = domain 
    
    def toLower(self, word):
        result = word.lower()
        return result

    def split(self, word):
        result = word.split(' ')
        return result

    def oneWordName(self, words):
        return words[0] 
        
    def moreThanOneWord(self, words):
        return words[0] + "." + words[-1] 
    
    def generateUserName(self, user, number):
        return user + str(number)
        
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

        lengthArray = len(splittedChar)

        if lengthArray == 1:
            userName = emGenerator.oneWordName(splittedChar)
        else:
            userName = emGenerator.moreThanOneWord(splittedChar)
    

        if userName in database:
            number = database[userName] + 1
            database[userName] = number
        else:
            database[userName] = 0
            number = ''

        userNameFinal = emGenerator.generateUserName(userName,number)
        emailName = emGenerator.generateEmailName(userNameFinal)

        print ""
        print "Username Anda:", userName
        print "Email anda   :", emailName
        print " "

    