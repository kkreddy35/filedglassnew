from crontab import CronTab
file_cron=CronTab(user='True')
job = file_cron.new(tab='python C:\\Users\\Kiran Kumar Reddy\\PycharmProjects\\filedglasskiran\\tests\\test1.py')
job.minute.every(1)
file_cron.write()
