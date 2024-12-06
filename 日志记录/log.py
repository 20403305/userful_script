import os
import logging
import sys

# 全局logger变量
logger = None

def setup_logger(log_directory, log_level=logging.DEBUG):
    global logger
    if logger is not None:
        return logger  # 如果logger已经配置，直接返回

    # 如果日志目录不存在，创建目录
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    log_file = os.path.join(log_directory, 'logging.log')

    # 创建一个logger
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    # 创建文件处理器
    file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
    file_handler.setLevel(log_level)

    # 创建控制台处理器
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)

    # 创建格式器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 添加处理器到logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info(f'日志文件存储在: {log_file}')
    return logger

def get_logger():
    global logger
    if logger is None:
        raise Exception("Logger not initialized. Call setup_logging first.")
    return logger