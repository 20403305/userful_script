# 基本目录配置
DIRECTORY_CONFIG = {
    'base_dir': os.path.join(os.getcwd(), 'test_dirs'),  # 创建的基础目录
}
# 日志配置
LOG_CONFIG = {
    'log_format': '%(asctime)s - %(levelname)s - %(message)s',
    'log_level': 'INFO',  # 可以改为 'DEBUG' 以显示更多信息
}