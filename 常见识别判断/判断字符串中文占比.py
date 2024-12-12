# 判断字符串中文占比
def is_chinese_ratio_over_threshold(text, threshold=0.8):
    # 统计汉字数量
    chinese_count = sum(1 for char in text if '\u4e00' <= char <= '\u9fff')
    
    # 计算总字符数(不包括空白字符)
    total_count = len(''.join(text.split()))
    
    # 避免除以0
    if total_count == 0:
        return False
        
    # 计算汉字占比
    chinese_ratio = chinese_count / total_count
    print(chinese_ratio)
    return chinese_ratio > threshold

# 使用示例
text = ""
result = is_chinese_ratio_over_threshold(text)
print(result)
