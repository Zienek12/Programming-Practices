from abc import ABC, abstractmethod
class NotificationSender(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass

class EmailSender(NotificationSender):
    def send_notification(self, message: str):
        print(f"Sending email notification: {message}")

class SMSSender(NotificationSender):
    def send_notification(self, message: str):
        print(f"Sending SMS notification: {message}")

class Notification(ABC):
    def __init__(self, sender: NotificationSender):
        self.sender = sender

    @abstractmethod
    def notify(self, message: str):
        pass

class UrgentNotification(Notification):
    def notify(self, message: str):
        self.sender.send_notification(f"URGENT: {message}")

class NormalNotification(Notification):
    def notify(self, message: str):
        self.sender.send_notification(f"Normal: {message}")

if __name__ == "__main__":
    email_sender = EmailSender()
    sms_sender = SMSSender()

    urgent_email = UrgentNotification(email_sender)
    normal_sms = NormalNotification(sms_sender)

    urgent_email.notify("This is an urgent email notification.")
    normal_sms.notify("This is a normal SMS notification.")