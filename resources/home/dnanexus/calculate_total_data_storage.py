##Script to read a json file and calculate the total data storage
##
##Usage: >python calculate_total_data_storage.py <project name> <folder name> <input json file> <output json file> <output plot file>
##
##Usage (interactive): >python -i calculate_total_data_storage.py <project name> <folder name> <input json file> <output json file> <output plot file>
##
##Written by C. Tibbs (May 2025)
##Updated by C. Tibbs (February 2026)
##

##Import Python packages
import json
import sys
import matplotlib.pyplot as plt


##Define paths and filenames


##Define variables
if len(sys.argv) != 6:
    print('')
    print('Please provide 5 inputs...')
    print('')
    sys.exit()
if len(sys.argv) == 6:
    project_name = sys.argv[1]
    folder_name = sys.argv[2]
    input_file = sys.argv[3]
    output_file = sys.argv[4]
    output_plot = sys.argv[5]
user_size = {}
total_data_storage = 0.

##Read in json file
with open(input_file) as f:
    data_files = json.load(f)

##Loop over list of data files
for data in data_files:

    #extract data file information
    if 'describe' in data:

        #extract project id
        if 'project' in data['describe']:
            project_id = data['describe']['project']

        #extract data id    
        if 'id' in data['describe']:
            data_id = data['describe']['id']

        #extract size
        if 'size' in data['describe']:
            data_size = data['describe']['size'] #default size is in Bytes
        else:
            data_size = 0.

        #extract creator
        if 'createdBy' in data['describe']:
            creator = data['describe']['createdBy']['user'].replace("user-", "")
        else:
            creator = "unknown"

    #convert Bytes to GB
    data_size = data_size / 1000. / 1000. / 1000.	

    #store user and data size in dictionary
    if creator in user_size:
        user_size[creator] = user_size[creator] + data_size
    else:
        user_size[creator] = data_size

    #compute total data storage
    total_data_storage = total_data_storage + data_size

##Sort the data from largest to smallest
sorted_user_size = dict(sorted(user_size.items(), key=lambda item: item[1], reverse=True))

##Plot the sorted data
#linear plot
plt.yscale('linear')
plt.ylabel('Data Size [GB]')
plt.xticks(rotation=90, fontsize=5)
plt.grid(visible=True, which='major', axis='y', linestyle='dashed', zorder=0)
plt.bar(*zip(*sorted_user_size.items()), facecolor='Blue')
ax = plt.gca()
ax.set_title(project_name + ':/' + folder_name + '/ - Total storage = '+str(round(total_data_storage/1000., 2))+' TB', wrap=True)
plt.savefig(output_plot)

##Add total to sorted_user_size dictionery
sorted_user_size['total_size'] = total_data_storage

##Print sorted_user_size data dict to a file
with open(output_file, 'w') as file:
    file.write(json.dumps(sorted_user_size))