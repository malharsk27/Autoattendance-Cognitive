import sys
import cognitive_face as CF
from global_variables import personGroupId
import sqlite3

Key = '222bf86ba9634534a995d3eed09dc857'
CF.Key.set(Key)
if len(sys.argv) is not 1:
    res = CF.person.create(personGroupId, str(sys.argv[1]))
    print(res)
    extractId = str(sys.argv[1])[-2:]
    connect = sqlite3.connect("Face-DataBase")
    cmd = "SELECT * FROM Students WHERE ID = " + extractId
    cursor = connect.execute(cmd)
    isRecordExist = 0
    for row in cursor:                                                          # checking wheather the id exist or not
        isRecordExist = 1
    if isRecordExist == 1:                                                      # updating name and roll no
        connect.execute("UPDATE Students SET personID = ? WHERE ID = ?",(res['personId'], extractId))
    connect.commit()                                                            # commiting into the database
    connect.close()
    print "Person ID successfully added to the database"
