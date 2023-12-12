#!/usr/bin/env python3
import json
'''
Context Managers allow us to setup and tear something down
automatically. For instance when opening a file. 
'''
# Old way of doing it
path = 'oldfile.txt'
new_path = 'newfile.txt'
my_data={'a-key':'a-value'}
old_file = open(path,'w')
json.dump(my_data, old_file) 
old_file.close()

# Using Context manager:
with open(new_path, 'w') as new_file:
   json.dump(my_data, new_file) 

print('-------------')

