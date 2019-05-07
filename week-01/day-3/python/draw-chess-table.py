# Crate a program that draws a chess table like this
#
# % % % % 
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % % 
#  % % % %
#
input_num = int(input())
for i in range(input_num):
    if(i%2!=0):
        print("% % % %")
    else:
        print(" % % % %")
