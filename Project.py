import re
file_store=[]
with open('syslog.txt', 'rt') as file_content:
    for i in file_content:
        file_store.append(i)
file_store=re.split('; |, |\n|\W',str(file_store))
print(file_store)
print(file_store[128])
'''
import re
text = 'The quick brown\nfox jumps*over the lazy dog.'

'''