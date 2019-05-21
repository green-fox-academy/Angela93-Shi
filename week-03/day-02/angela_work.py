
class AngelaWork:
    def get_apple(self,name):
        self.name = name
        return f"{self.name}"

    def get_sum(self,integers_list):
        sum = 0
        try:
            if not integers_list is None:
                for i in integers_list:
                    sum += i
                return sum
        except:
            pass
    
    def anagram(self,s1,s2):
        a_list = list(s1)
        b_list = list(s2)
        a_list.sort()
        b_list.sort()
        still_work = True
        pos = 0
        while pos < len(s1) and still_work:
            if a_list[pos] == b_list[pos]:
                pos += 1
            else:
                still_work = False
        return still_work
    
    def count_letters(self,s1):
        self.s1 = s1
        d={}
        for i in self.s1:
            if i in d:
                d[i] = d[i] + 1           #if i in d, the value of d[i] add 1
            else:
                d[i] = 1                  #if not, the value of d[i] equals 1
        return d
    
    def feibo(self,number):
        self.number = number
        a,b,i = 0,1,1
        while i < number:
            a,b = b, a+b
            i += 1
        return b



# angela_work = AngelaWork()
# print(angela_work.feibo(6))

