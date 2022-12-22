# fantasy-bot-boxscores

Provides a celery task which can download nhl box scores
eg: docker run --rm -it --name box -v /tmp/boxscores:/boxscores -e BROKER_URL='amqp://192.168.6.74:5672//' -e CELERY_RESULT_BACKEND='redis://192.168.6.74' craigham/nhl-boxscores:snapshot

