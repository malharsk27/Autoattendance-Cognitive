import sys
import os, time
import cognitive_face as CF
from global_variables import personGroupId
import urllib
import sqlite3

Key = '222bf86ba9634534a995d3eed09dc857'
CF.Key.set(Key)

def get_person_id():
	person_id = ''
	extractId = str(sys.argv[1])[-2:]
	connect = sqlite3.connect("Face-DataBase")
	c = connect.cursor()
	cmd = "SELECT * FROM Students WHERE ID = " + extractId
	c.execute(cmd)
	row = c.fetchone()
	person_id = row[3]
	connect.close()
	return person_id

if len(sys.argv) is not 1:
    currentDir = os.path.dirname(os.path.abspath(__file__))
    imageFolder = os.path.join(currentDir, "dataset/" + str(sys.argv[1]))
    person_id = get_person_id()
    for filename in os.listdir(imageFolder):
        if filename.endswith(".jpg"):
        	print(filename)
        	imgurl = urllib.pathname2url(os.path.join(imageFolder, filename))
        	res = CF.face.detect(imgurl)
        	if len(res) != 1:
        		print "No face detected in image"
        	else:
        		res = CF.person.add_face(imgurl, personGroupId, person_id)
        		print(res)	
        	time.sleep(6)
