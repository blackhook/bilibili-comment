import re,requests
for all in str(re.findall(ur'">(.*)</d>',requests.get('http://comment.bilibili.com/'+re.search(r'(cid=([\s\S]*?)&)',requests.get('http://www.bilibili.com/video/'+raw_input("Enter your av: "),verify=True,timeout=2).text).group()[4:-1]+'.xml',verify=True,timeout=2).text)[2:-4]).decode("unicode_escape").split( ):
        all=all[2:-2]
        if len(all)!=0:print all

