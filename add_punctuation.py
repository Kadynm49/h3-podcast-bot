from punctuator import Punctuator
p = Punctuator('/home/erviewre/h3podcastbot/.punctuator/Demo-Europarl-EN.pcl')

import os

directory = os.fsencode("/home/erviewre/h3podcastbot/raw_scripts")
file_count = len(os.listdir(directory))
progress = 1

for file in os.listdir(directory):
  print(str(progress) + "/" + str(file_count))
  progress += 1
  filename = os.fsdecode(file)
  with open('/home/erviewre/h3podcastbot/raw_scripts/' + filename, 'r') as open_file:
    data = open_file.read().replace('\n', ' ')
    with open('/home/erviewre/h3podcastbot/punctuated_scripts/' + filename, 'w') as punctuated_file:
      punctuated_file.write(p.punctuate(data))
