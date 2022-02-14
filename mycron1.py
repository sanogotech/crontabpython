from crontab import CronTab

cron = CronTab(user=True)
job = cron.new(command='python example1.py',comment='my comment')
job.minute.every(1)

cron.write()