from angela_work import AngelaWork
from sharpie import Sharpie
from animal import Animal
from cows_and_bulls import CAB
import unittest

class Testing_Angela_work(unittest.TestCase):
    def test_get_apple(self):
        apple = AngelaWork()
        param = 'apple'
        self.assertEqual(apple.get_apple(param),'apple')

    def test_list_sum(self):
        sum_instance = AngelaWork()
        integers_list = [1,2,3,4,5]
        self.assertEqual(sum_instance.get_sum(integers_list),15)

    def test_empty_list_sum(self):
        sum_instance = AngelaWork()
        integers_list = []
        self.assertEqual(sum_instance.get_sum(integers_list),0)
    
    def test_one_element_list_sum(self):
        sum_instance = AngelaWork()
        integers_list = [5]
        self.assertEqual(sum_instance.get_sum(integers_list),5)

    def test_none_sum(self):
        sum_instance = AngelaWork()
        integers_list = None
        self.assertEqual(sum_instance.get_sum(integers_list),None)


    def test_anagram(self):
        anagram_instance = AngelaWork()
        s1='angela'
        s2='alegna'
        self.assertTrue(anagram_instance.anagram(s1,s2))

    def test_count_letters(self):
        count_letters_instance = AngelaWork()
        s1 = "angela"
        self.assertEqual( count_letters_instance.count_letters(s1) , {'a':2,'n':1,'g':1,'e':1,'l':1} )

    def test_feibo(self):
        test_feibo_instance = AngelaWork()
        number = 6
        self.assertEqual(test_feibo_instance.feibo(number),8)

    def test_sharpie(self):
        sharpie = Sharpie('blue',10.0,100.0)
        ink_amount1 = 20.0
        ink_amount2 = 20
        ink_amount3 = 'ink'
        ink_amount4 = 'True'
        self.assertEqual(sharpie.use(ink_amount1),80.0)
        self.assertEqual(sharpie.use(ink_amount2),60.0)
        self.assertEqual(sharpie.use(ink_amount3),None)
        self.assertEqual(sharpie.use(ink_amount4),None)

    def test_animal(self):
        animal = Animal()
        self.assertEqual(animal.eat(),49)
        self.assertEqual(animal.drink(),49)
        self.assertEqual(animal.play(),(50,50))
    
    def test_cab(self):
        cab_instance = CAB()
        self.assertEqual(cab_instance.getHint(),'Success!')

if __name__ == "__main__":
    unittest.main()