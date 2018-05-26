import pymysql


def add_new_token(face_token, familiar_ft):
    maxuid = 0
    pr = open("UNUM.txt","r")
    for line in pr.readlines():
        line = line.strip()
        maxuid = int(line)
    pr.close()

    db = pymysql.connect("127.0.0.1","root","","USERandFACES" )

    cursor = db.cursor()

    sql = 'SELECT * FROM UF WHERE FACETOKEN = "%s"'%(familiar_ft)
    try:
       cursor.execute(sql)
       results = cursor.fetchall()
       if(len(results)>0):
           uid = results[0][0]
       else:
           maxuid = maxuid + 1
           uid = maxuid
    except:
       print ("Error: unable to fetch data")

    print(uid)
    print(face_token)
    try:
       cursor.execute('insert into UF (UID,FACETOKEN) values(%d, "%s")'%(uid, face_token))
       db.commit()
    except:
       db.rollback()
       print ("Error: unable to insert data")
    db.close()

    pw = open("UNUM.txt","w")
    pw.write(repr(maxuid))
    pw.close()

if __name__ == '__main__':
    add_new_token("asdf","qwer")
    add_new_token("tyu","")
