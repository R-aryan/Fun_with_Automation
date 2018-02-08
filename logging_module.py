import logging 

#basic format for logging
logging.basicConfig(filename= 'mylogs.txt',filemode='w',level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
#to disable logging
#logging.disable(logging.CRITICAL)
#five types of log levels
#DEBUG(lowest),info,warning,error, crirical(highest)

logging.debug('start the program')

def fact(n):
    total=1
    for i in range(1,n+1):
        total*=i
        logging.info('Value at iteration '+str(i)+' is '+str(total))
    
    print('factorial of '+str(n)+' is  '+str(total))
    logging.debug('factorial of '+str(n)+' is  '+str(total))
    


fact(10)


