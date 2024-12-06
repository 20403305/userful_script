import logging

# 配置日志
log_file_path = "logging.log"
logging.basicConfig(filename=log_file_path, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    encoding='utf-8')
                    
logging.info("日志记录已启动。")
