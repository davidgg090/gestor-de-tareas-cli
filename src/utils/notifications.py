from pync import Notifier


def send_notification(message: str):
    """
    Sends a desktop notification with the specified message.

    Args:
        message (str): The message of the notification.

    Raises:
        Exception: If an error occurs while sending the notification.
    """
    try:
        Notifier.notify(message, title=f"Task Manager")
    except Exception as e:
        print(f"An error occurred while sending notification: {e}")
