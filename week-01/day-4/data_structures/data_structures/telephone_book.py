#Create a map with the following key-value pairs.
map={'William A. Lathan':'405-709-1865','John K. Miller':'402-247-8568','Hortensia E. Foster':'606-481-6467','Amanda D. Newland‬':'319-243-5613','Brooke P. Askew':'307-687-2982'}
print(map['John K. Miller'])
#Whose phone number is 307-687-2982?
for key,value in map.items():
    if value == '307-687-2982':
        print(key)
#Do we know Chris E. Myers' phone number?
for key,value in map.items():
    if key == 'Chris E. Myers':
        print('Yes')
    else:
        print('No')
        break


    
