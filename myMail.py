#!/usr/lib/python2.7
# −∗− coding: utf−8 −∗−
import os
import sys
import imaplib
import email, getpass
# import emails #'My own dictionary for acount and pw'
# from emails import dicCorreos,dicContras

def get_text(self, email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
            if part.get_content_maintype() == 'multipart':
                for part2 in part.get_payload():
                    return part2.get_payload()
    elif maintype == 'text':
        print 'FALLO','maintype',email_message_instance.get_payload()
        return email_message_instance.get_payload()

def get_mail(lista_data):
    print "entro en get_text_successful\n"
    for correoElectronico in list_data:
        correoDeOrigen=email.utils.parseaddr(correoElectronico['From'])[1]
        mail=correoElectronico
        #    if correoDeOrigen!=dicCorreos['correo1']
        #        and email_message_list[i]['Subject']=='Voy a probar':
        #        print "No era lo esperado \n",correoDeOrigen,dicCorreos['correo1']
        #        pass
        mensaje = get_text('',list_data[i])
        print 'Titulo: ',list_data[i]['Subject']
        print 'Mensaje: ',mensaje
        for part in correoElectronico.walk():
            if part.get_content_maintype=='multipart':
                continue
            if part.get("Content-Disposition") is None:
                continue
            fileName = part.get_filename().decode('utf8')
            print fileName
            if bool(fileName):
                filePath = os.path.join('.','attachments',fileName)
                print fileName
                fp=open(filePath,'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
        print "\n---------------------End of iteration N",i,"------------------------------"

if __name__=="__main__":
    userName = raw_input('Enter your GMail username: \n\t')
    passwd = getpass.getpass('Enter your password: \n\t')    
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(userName,passwd)
    mail.list()
    mail.select("inbox")
    result,data = mail.search(None,"ALL")
        # result=OK,data=['1 2 3 4 5 6 7 8 9 10 11 ...'
    line = raw_input('How many mails do you want to get?\n    ')
    numberOfmails=int(line)
    if result=='OK':
        latest_id = data[0].split()[-numberOfmails:]
    
    list_data=[]
    print data[0].split()
    print latest_id
    for i in range(numberOfmails): print latest_id[i]
    for i in range(numberOfmails):
        email2=mail.fetch(int(latest_id[i]),"(RFC822)")
        print latest_id[i],type(latest_id[i])
        list_data.append(email.message_from_string(email2[1][0][1]))
    
    print ''
    print ''
    if len(list_data)>=2:
        get_mail(list_data)
    else:
        get_mail([list_data])
    mail.close()
    mail.logout()
