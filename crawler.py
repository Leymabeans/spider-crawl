import os

#Each website that is crawled will create a new folder
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating project " + directory)
        os.makedirs(directory)


#Create queue and crawled files
def create_datafiles(directory, base_url):
    queue = directory + '/queue.txt'
    crawled = directory + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


#Create a new file for information gathered
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()



#Add gathered information to the file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')



#Delete the contents of the file
def delete_file_contents(path):
    with open(path, 'w'):
        pass



#Read the file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


#Iterate the set, a new line for each item
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)







'''
create_project_dir('SoundCloud')
create_datafiles('SoundCloud', 'https://soundcloud.com')
'''






