
# Create a function called 'reverse' which takes a string as a parameter
# The function reverses it and returns with the reversed string

reverse_str = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"
def reverse(taget_reverse_str):
    reverse_list=list(taget_reverse_str)
    for i in range(len(reverse_list)//2):
        reverse_list[i],reverse_list[-(i+1)]=(reverse_list[-(i+1)],reverse_list[i])
        taget_reverse_str=''.join(reverse_list)
    return taget_reverse_str

print(reverse(reverse_str))