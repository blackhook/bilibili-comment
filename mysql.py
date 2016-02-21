import re,requests,MySQLdb,socket,base64,sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
timeout=2
socket.setdefaulttimeout(timeout)
db = MySQLdb.connect("localhost","root","","bilibili",charset='utf8')
i=0
for cid in range(1,500):
    cursor = db.cursor()
    word_list=[]
    sql_list=[]
    comment_url='http://comment.bilibili.com/'+str(cid)+'.xml'
    comment_text=requests.get(comment_url,verify=True).text
    words=re.findall(ur'">(.*)</d>',comment_text)
    word_list.append(words)
    i=i+1
    print i
    for word in  word_list:
        for word in  word:
            b64word=base64.b64encode(word)
            sql = "INSERT INTO comment(comment)  VALUES ('%s')" % (b64word)
            sql_list.append(sql)
    try:
        for sql in  sql_list:
            cursor.execute(sql)
            db.commit()
    except:
        #print sql
        db.rollback()

db.close()