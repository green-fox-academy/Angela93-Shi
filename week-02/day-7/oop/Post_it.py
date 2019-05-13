class PostIt():
    def __init__(self,background_color,text,text_color):
        self.background_color=background_color
        self.text=text
        self.text_color=text_color

PostItOne = PostIt('orange','Idea','blue')
PostItTwo = PostIt('pink','Awesome','black')
PostItThree = PostIt('yellow','Superb','green')

# PostItOne.background_color="orange"
# PostItOne.text="Idea 1"
# PostItOne.text_color="blue"

# PostItTwo.background_color="pink"
# PostItTwo.text="Awesome"
# PostItTwo.text_color="black"

# PostItThree.background_color="yellow"
# PostItThree.text="Superb"
# PostItThree.text_color="green"

print("background_color of PostOne:" + PostItOne.background_color + ", text of PostOne is:" + PostItOne.text + ",text_color of PostOne is:" + PostItOne.text_color)
print("background_color of PostTwo:" + PostItTwo.background_color + ", text of PostTwo is:" + PostItTwo.text + ",text_color of PostTwo is:" + PostItTwo.text_color)
print("background_color of PostThree:" + PostItThree.background_color + ", text of PostThree is:" + PostItThree.text + ",text_color of PostThree is:" + PostItThree.text_color)