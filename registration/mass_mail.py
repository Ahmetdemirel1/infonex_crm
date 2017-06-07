"""
functions related to processing & sending mass mail to delegates
"""

from django.core.mail import EmailMessage
import time


class MassMail():
    def __init__(self, subject, message, msg_type, post_data):
        self._subject = subject
        self._message = message
        self._recipients = self._build_mail_dict(post_data)
        self._msg_type = msg_type
        self._password_dict = {}

    def _build_mail_dict(self, post_data):
        """
        builds dict for sending email:
        key: regdetails.pk (or N + sequence number)
        value: dict: {'email': email, 'salutation': salutation}
        """
        email_dict = {}
        for key in post_data:
            if key[:7] == 'address':
                row_id = key.partition('_')[2]
                if row_id in email_dict:
                    email_dict[row_id]['email'] = post_data[key]
                else:
                    email_dict[row_id] = {'email': post_data[key],
                                          'salutation': None,}
            elif key[:7] == 'salutat':
                row_id = key.partition('_')[2]
                if row_id in email_dict:
                    email_dict[row_id]['salutation'] = post_data[key]
                else:
                    email_dict[row_id] = {'email': None,
                                          'salutation': post_data[key],}
        return email_dict

    def _insert_passwords(self, msg_body, reg_detail_id):
        # do the insert Logic
        return msg_body

    def set_subject(self, subject_text):
        self._subject = subject_text

    def set_message(self, message_text):
        self._message = message_text

    def set_passwords(self, password_list):
        pass

    def send_mail(self):
        # need to ensure address is minimally valid email
        sent_emails = ['', None]
        for key in self._recipients:
            reg_id = key
            address = self._recipients[key]['email']
            salutation = self._recipients[key]['salutation']
            email_body = self._message
            if address not in sent_emails:
                if salutation not in ('', None):
                    email_body = 'Dear ' + salutation + ':<br/><br/>' + \
                        self._message
                if self._msg_type == 'docs':
                    email_body = self._insert_passwords(email_body, key)
                email = EmailMessage(
                    subject = self._subject,
                    body = email_body,
                    to = [address]
                )
                email.content_subtype = 'html'
                email.send()
                sent_emails.append(address)
                time.sleep(0.5)
