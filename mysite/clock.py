#
# import email_ASR as mail
#
# from apscheduler.schedulers.blocking import BlockingScheduler
# # from apscheduler.schedulers.background import BackgroundScheduler
#
# sched = BlockingScheduler()
#
# @sched.scheduled_job('interval', minutes=3)
# def timed_job():
#     print('This job is run every three hundreds minutes.')
#     mail.email_reminder()
#
# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=5)
# def scheduled_job():
#     print('This job is run every weekday at 5pm.')
#
# sched.start()