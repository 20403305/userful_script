from log import setup_logger

log_directory = 'logs'  # 指定日志存放的目录
setup_logger(log_directory)  # 初始化日志配置
logger = get_logger()
