import dns.resolver
import os
import http.client
iplist=[]
appdomain='www.baidu.com'
def get_iplist(domain=""):
    try:
        A=dns.resolver.query(domain,'A')
    except Exception as e:
        return print('dns resolver error:'+str(e))
        
    for i in A.response.answer:
        for j in i.items :
            iplist.append(j)
    return True
def checkip(ip):
    checkurl=str(ip)+str(":")
    getcontent=''
    http.client.socket.setdefaulttimeout(5)
    conn=http.client.HTTPConnection(checkurl)
    try:
        conn.request('GET','/',headers={'Host':appdomain})
        r=conn.getresponse()
        getcontent=r.read(15)
    finally:
        if getcontent=='<!doctype html>':
            print(str(ip)+'[ok]')
        else:
            print(str(ip)+'[error]')
if __name__=="__main__":
    if get_iplist(appdomain) and len(iplist)>0:
        for ip in iplist:
            checkip(str(ip))
    else:
        print("dns resolver error")