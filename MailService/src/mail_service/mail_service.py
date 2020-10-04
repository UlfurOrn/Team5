from mail_service.mail_service_creator import MailServiceCreator
from mail_service.mail_service_sendgrid import MailServiceSendgrid


creator = MailServiceCreator(MailServiceSendgrid)
mail_service = creator.get_mail_service()
