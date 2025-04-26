from celery import app

@app.shared_task(bind=True, queue='default')
def debug_task(self):
    print('Hello World')