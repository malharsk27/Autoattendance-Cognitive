import cognitive_face as CF
from global_variables import personGroupId

Key = '222bf86ba9634534a995d3eed09dc857'
CF.Key.set(Key)

res = CF.person_group.get_status(personGroupId)
print res
