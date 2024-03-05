from notify2 import Notification


def send_notification(type: str, message: str):
    """
    Sends a desktop notification with the specified type and message.

    Args:
        type (str): The type of the notification.
        message (str): The message of the notification.

    Raises:
        Exception: If an error occurs while sending the notification.
    """
    try:
        Notification.init("Task Manager")
        n = Notification(
            summary=f"Task {type}",
            message=message,
        )
        n.show()
    except Exception as e:
        print(f"An error occurred while sending notification: {e}")
