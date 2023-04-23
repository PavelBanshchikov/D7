from celery import shared_task

@shared_task
def send():
    categories = instance.category.all()
    subscribers: list[str] = []
    for category in categories:
        subscribers += category.subscribers.all()
    subscribers = [s.email for s in subscribers]
    send_notifications(instance.preview(), instance.pk, instance.header, subscribers)


