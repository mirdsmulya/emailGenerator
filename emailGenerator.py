
class emailGenerator(object):

    def __init__(self, domain, database):
        self.domain = domain 
        self.database = database
    
    def createUserName(self, fullname):
        fullname = fullname.lower()
        fullname = fullname.split(' ')
        if len(fullname) == 1:
            return fullname[0]
        else:
            return fullname[0] + '.' + fullname[-1]

    def generateUserName(self, fullname):
        username = self.createUserName(fullname)

        if username in self.database:
            number = self.database[username] + 1
            self.database[username] = number
        else:
            self.database[username] = 0
            number = ''
        
        return username + str(number)

    def generateEmailName(self, username):
        return username + self.domain


if __name__ == "__main__":

    domain = "@paragraph.ai"
    database = {"mirdanx":0, 'halan sukur':2}


    while True:
        fullname = raw_input('Inputkan nama lengkap anda: \n > ')
        emGenerator = emailGenerator(domain, fullname, database)
        userName = emGenerator.generateUserName(fullname)
        emailName = emGenerator.generateEmailName(userName)
        print ""
        print "Username Anda:", userName
        print "Email anda   :", emailName
        print " "

    