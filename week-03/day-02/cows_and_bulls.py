import random
class CAB:
    def getHint(self):
        self.secret = str(random.randint(1000,9999))
        print(self.secret)
        bull = 0
        secret_list = {}
        guess_list = {}
        to_del = []
        self.state = 'palying'
        self.counter = 0
        guess = 1000
        while guess != self.secret:
            guess = input('please type a 4 digit number: ')
            self.counter += 1
            for i in range(len(self.secret)):
                if self.secret[i] == guess[i]:
                    to_del.append(i)
                    bull += 1
                else:
                    secret_list[self.secret[i]] = 1
                
                if guess[i] in guess_list:
                    guess_list[guess[i]] += 1
                else:
                    guess_list[guess[i]] = 1
            
            cows = 0
            
            for i in guess_list.keys():
                if i in secret_list.keys():
                    cows += min(guess_list[i],secret_list[i])
            
            print (f'{bull} bulls {cows} cows')

        self.state = 'finished'   
        print(f"Success!You guess {self.counter} times")
        return "Success!"

cab = CAB()
cab.getHint()