from configparser import ConfigParser
import smtplib
import email.message

configDefault = {'email': 'enviaemailcontabilidade@gmail.com',
                'password': 'sxeksjtdrxfjfeqy'}

config = ConfigParser(configDefault)
config.read('arquivoConfig.ini')
arquivo_config = dict(config['config'])
configSMTP = ConfigParser()
configSMTP.read('arquivoConfig.ini')
arquivo_config_SMTP_gmail = dict(configSMTP['gmail'])
arquivo_config_SMTP_outlook = dict(configSMTP['outlook'])
arquivo_config_SMTP_yahoo = dict(configSMTP['yahoo'])

def envia_email():
    msg = email.message.Message()
    msg['Subject'] = arquivo_config['assunto']
    msg['From'] = arquivo_config['email']
    msg['To'] = arquivo_config['emailrecebedor']
    password = arquivo_config['password']
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(arquivo_config['corpo'])

    if '@gmail' in arquivo_config['email']:
        smtp = smtplib.SMTP(arquivo_config_SMTP_gmail['smtp'])
    elif '@outlook' in arquivo_config['email'] or '@hotmail' in arquivo_config['email']:
        smtp = smtplib.SMTP(arquivo_config_SMTP_outlook['smtp'])
    elif '@yahoo' in arquivo_config['email']:
        smtp = smtplib.SMTP(arquivo_config_SMTP_yahoo['smtp'])
    else:
        print('Dominio do E-mail não esta definido ')

    smtp.starttls()
    smtp.login(msg['From'], password)
    smtp.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email Enviado')


envia_email()