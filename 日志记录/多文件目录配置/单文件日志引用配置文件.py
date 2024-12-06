import logging
from config import DIRECTORY_CONFIG, LOG_CONFIG

# 初始化日志记录，日志写入 test_dirs/logging.log 文件
log_file_path = os.path.join(DIRECTORY_CONFIG['base_dir'], 'logging.log')

# 检查日志目录是否存在，如果不存在则创建
log_dir = os.path.dirname(log_file_path)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(level=getattr(logging, LOG_CONFIG['log_level']),
                    format=LOG_CONFIG['log_format'],
                    handlers=[logging.FileHandler(log_file_path, 'a', 'utf-8'), logging.StreamHandler()])

logging.info("日志记录已启动。")