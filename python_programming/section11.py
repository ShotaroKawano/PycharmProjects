# import configparser

# config = configparser.ConfigParser()
# config['DEFAULT'] = {
#     'debug': True
# }
# config['web_server'] = {
#     'host': '127.0.0.1',
#     'port': 80
# }
# config['db_server'] = {
#     'host': '127.0.0.1',
#     'port': 3306
# }
# with open('config.ini', 'w') as config_file:
#     config.write(config_file)

# config.read('config.ini')
# print(config['web_server'])
# print(config['web_server']['host'])


# import yaml
#
# with open('config.yaml', 'w') as yaml_file:
#     yaml.dump({
#         'web_server': {
#             'host': '127.0.0.1',
#             'port': 80
#         },
#         'db_server': {
#             'host': '127.0.0.1',
#             'port': 3306
#         }
#     }, yaml_file, default_flow_style=False)
#
# with open('config.yaml', 'r') as yaml_file:
#     data = yaml.load(yaml_file)
#     print(data)
#     print(data['web_server']['host'])


import logging

# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(filename='test.log', level=logging.INFO)
# formatter = '%(levelname)s:%(message)s'
# formatter = '%(asctime)s:%(message)s'
# logging.basicConfig(level=logging.INFO, format=formatter)

# logging.critical('critical')
# logging.error('error')
# logging.warning('warning')
# logging.info('info')
# logging.debug('debug')

# logging.info('info {}'.format('test'))
# logging.info('info %s %s' % ('test', 'test2'))
# logging.info('info %s %s', 'test', 'test2')

# import logtest

# logging.basicConfig(level=logging.INFO)

# logger = logging.getLogger(__name__)
# logger.info('from main')
# logtest.do_something()


# class NoPassFilter(logging.Filter):
#     def filter(self, record):
#         log_message = record.getMessage()
#         return 'password' not in log_message

# logger = logging.getLogger(__name__)
# logger.addFilter(NoPassFilter())
# logger.info('from main')
# logger.info('from main password = "test"')
# logger.info('from main xxxxxxxx = "test"')


from optparse import OptionParser

def main():
    usage = 'usage: %prog [option] arg1 arg2'
    parser = OptionParser(usage=usage)
    parser.add_option('-f', '--file', action='store', type='string',
                      dest='filename', help='File name')
    parser.add_option('-n', '--num', action='store', type='int',
                      dest='num', default=10)
    parser.add_option('-v', action='store_true', dest='verbose')
    options, args = parser.parse_args()
    print(options)
    print(args)

if __name__ == '__main__':
    main()



