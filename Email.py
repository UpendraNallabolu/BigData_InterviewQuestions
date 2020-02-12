import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'noreply@grafana.com'

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """

    names = ["Admin", "Admin", "ada_sre"]
    emails = ["Evtadmin1@uat1bank.dbs.com", "Evtuser1@uat1bank.dbs.com", "ada_sre@uat1bank.dbs.com"]
    #with open(filename, mode='r', encoding='utf-8') as contacts_file:
    #    for a_contact in contacts_file:
    #        names.append(a_contact.split()[0])
    #        emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    names, emails = get_contacts('mycontacts.txt') # read contacts
    #message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.uat1bank.dbs.com', port=25)
    s.ehlo()
    #s.starttls()
    #s.login(MY_ADDRESS, PASSWORD)

    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message
        message = """
            Hostname: x01sadaapp111a.vsi.sgp.dbs.com
            Severity: FATAL
            AlertKey: Sample Rule
            Alertgroup: PSG_DBSAPP_ADA
            InstanceID: Test
            IchampGroup: PSG_DBSAPP_ADA
            Message: Alert message. This message is for testing the SNOC Integration.
            ApplicationName: ADA
            ApplicationCode: ADA
            ApplicationCategory: 3
            LOB: C2E
        """
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="This is a sample TEST mail"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        s.send_message(msg)
    #     s.sendmail(MY_ADDRESS, email, message)

    # For each contact, send the email:
    #for name, email in zip(names, emails):
    #    msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        #message = message_template.substitute(PERSON_NAME=name.title())

    #    message = """
    #        Hostname: x01sadaapp111a.vsi.sgp.dbs.com
    #        Severity: FATAL
    #        AlertKey: Sample Rule
    #        Alertgroup: PSG_DBSAPP_ADA
    #        Message:Alert message. This message is for testing the SNOC Integration.
    #    """

    #    # Prints out the message body for our sake
    #    print(message)

    #    # setup the parameters of the message
    #    msg['From']=MY_ADDRESS
    #    msg['To']=email
    #    msg['Subject']="This is TEST"


    #    # add in the message body
    #    msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
    #    s.send_message(msg)
    #    del msg

    # Terminate the SMTP session and close the connection
    s.quit()

if __name__ == '__main__':
    main()
