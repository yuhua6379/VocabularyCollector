import logging

def conf():

    # 创建一个logger
    logger = logging.getLogger()

    # 设置日志级别为INFO
    logger.setLevel(logging.INFO)

    # # 创建一个handler用于写入日志文件
    # handler = logging.FileHandler('example.log')

    # 再创建一个handler用于输出到控制台
    console = logging.StreamHandler()

    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    # handler.setFormatter(formatter)
    console.setFormatter(formatter)

    # 给logger添加handler
    # logger.addHandler(handler)
    logger.addHandler(console)
