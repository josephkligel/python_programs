import logging

extraData = {
    'user': 'jk@example.com'
}

def anotherFunction():
    logging.debug("This is a debug-level message", extra=extraData)

def main():
    fmtstr = 'User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s'
    datestr = '%m/%d/%Y %I:%M:%S %p'
    logging.basicConfig(level=logging.DEBUG, filename='output.log', filemode='w', format=fmtstr, datefmt=datestr)
    logging.debug('This is a debug message', extra=extraData)
    logging.info('This is a info message', extra=extraData)
    logging.warning('This is a warning message', extra=extraData)
    logging.error('This is an error message', extra=extraData)
    logging.critical('This is a critical message', extra=extraData)

    logging.info(f"Here's a {'string'} variable and an int.",  extra=extraData)
    anotherFunction()

if __name__ == '__main__':
    main()
