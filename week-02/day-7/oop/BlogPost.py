class BlogPost():
    author_name=" "
    title=" "
    text=" "
    publication_date=" "

BlogPostOne=BlogPost()
BlogPostTwo=BlogPost()
BlogPostThree=BlogPost()

BlogPostOne.author_name="John Doe"
BlogPostOne.title="Lorem Ipsum"
BlogPostOne.text="Lorem ipsum dolor sit amet."
BlogPostOne.publication_date="2000.05.04"

BlogPostTwo.author_name="Tim Urban"
BlogPostTwo.title="Wait but why"
BlogPostTwo.text="A popular long-form, stick-figure-illustrated blog about almost everything."
BlogPostTwo.publication_date="2010.10.10"

BlogPostThree.author_name="William Turton"
BlogPostThree.title="One Engineer Is Trying to Get IBM to Reckon With Trump"
BlogPostThree.text="Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing."
BlogPostThree.publication_date="2017.03.28"

print("author_name of BlogPostOne is:" + BlogPostOne.author_name + ", title of BlogPostOne is:" + BlogPostOne.title + ",text of BlogPostOne is:" + BlogPostOne.text + ", publication_date of BlogPostOne is" + BlogPostOne.publication_date)
print("author_name of BlogPostTwo is:" + BlogPostTwo.author_name + ", title of BlogPostTwo is:" + BlogPostTwo.title + ",text of BlogPostTwo is:" + BlogPostTwo.text + ", publication_date of BlogPostTwo is" + BlogPostTwo.publication_date)
print("author_name of BlogPostThree is:" + BlogPostThree.author_name + ", title of BlogPostThree is:" + BlogPostThree.title + ",text of BlogPostThree is:" + BlogPostThree.text + ", publication_date of BlogPostThree is" + BlogPostThree.publication_date)