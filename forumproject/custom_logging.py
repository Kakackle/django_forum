from .settings import BASE_DIR
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'filters': [],
        },
        'file_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': f"{BASE_DIR}/logs/forumlog.log",
            'mode': 'a',
            'encoding': 'utf-8',
            'formatter': 'standard',
            'backupCount': 5,
            'maxBytes': 1024 * 1024 * 5,
        },
    },
    'loggers': {
        logger_name: {
            'level': 'WARNING',
            'propagate': True,
        } for logger_name in ('django', 'django.request', 'django.db.backends', 'django.template', 'forum')
    },
    'root':{
        'level': 'DEBUG',
        'handlers': ['console', 'file_handler'],
    }
}

# ex.

# with custom name
# logger = logging.getLogger('name_value')

# with the name of the module
# logger = logging.getLogger(__name__)

# usage
# import logging
# logger = logging.getLogger('user')
#     logger.debug('This is a test debug log message')
#     logger.info('this is info')