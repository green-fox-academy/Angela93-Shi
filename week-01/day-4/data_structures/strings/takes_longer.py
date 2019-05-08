# When saving this quote a disk error has occured. Please fix it.
# Add "always takes longer than" between the words "It" and "you"
quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."
quote_list=list(quote)
target_str="always takes longer than "
quote_list.insert(21,target_str)
str_list=''.join(quote_list)
print(str_list)