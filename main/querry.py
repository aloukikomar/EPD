from main.models import List,Student

def lidata(ids):
    new = List.objects.raw('SELECT * FROM Main_List WHERE id='+ids+'')
    for obj in new:
        datab = obj.Markslowb
        datac = obj.Markslowc
        databr = obj.Branch
        data12 = obj.Markslow12
    return {"br":databr,"12":data12,"coll":datac,"10":datab}

def result(ids):
    data = lidata(ids)
    DATA=[]  
    if data["br"] == "all":
        new = Student.objects.raw('SELECT * FROM Main_Student WHERE Markslowc >='+str(data["coll"])+' AND Markslow12 >='+str(data["12"])+' AND Markslowb >='+str(data["10"])+' ORDER BY rollno')
    else:
        new = Student.objects.raw('SELECT * FROM Main_Student WHERE Markslowc >='+str(data["coll"])+' AND Markslow12 >='+str(data["12"])+' AND Markslowb >='+str(data["10"])+' AND Branch =="'+str(data["br"])+'" ORDER BY rollno')
    for obj in new:
        DATA.append([obj.Name,obj.rollno,obj.Branch,obj.Markslowc,obj.Markslow12,obj.Markslowb],)
    return DATA
  
    #{"marksc":marksc,"markss":markss,"marksb":marksb}
