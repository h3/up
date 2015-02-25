import logging
import coloredlogs

coloredlogs.install(level=0)
coloredlogs.install(level=1)
coloredlogs.install(level=2)
coloredlogs.install(level=3)
coloredlogs.install(level=4)
coloredlogs.install(level=5)


def get_logger(name='up'):
    return logging.getLogger(name)


