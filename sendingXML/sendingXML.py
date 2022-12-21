from configparser import ConfigParser
import smtplib
import email.message

configDefault = {'email': 'enviaemailcontabilidade@gmail.com',
                'password': 'enviaemail123'}

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
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(arquivo_config['corpo'])

    if arquivo_config['email'].find('gmail'):
        smtp = smtplib.SMTP(arquivo_config_SMTP_gmail['smtp'])
    elif arquivo_config['email'].find('outlook') or arquivo_config['email'].find('hotmail'):
        smtp = smtplib.SMTP(arquivo_config_SMTP_outlook['smtp'])
    elif arquivo_config['email'].find('yahoo'):
        smtp = smtplib.SMTP(arquivo_config_SMTP_yahoo['smtp'])

