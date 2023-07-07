from fluent import sender

print("********  START  ********")

#logger = sender.FluentSender('app')
#logger = sender.FluentSender('app', host = 'localhost', port = 24224)
logger = sender.FluentSender('fluentd')
logger.emit('follow', {'from':'userA', 'to':'dpk_01', 'current_date':"110"})
#logger.close()

print("********  END  ********")
