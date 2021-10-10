import logging
from datetime import datetime


# debug < info < warning < error < critical
# logging.basicConfig(level=logging.DEBUG, format = "%(asctime)s [%(levelname)s] %(message)s")
## 시간, 로그레벨, 메세지

# logging.debug("디버그 메세지")
# logging.info("디버그 메세지")
# logging.warning("디버그 메세지")
# logging.error("디버그 메세지")
# logging.critical("디버그 메세지")

# print("")

# logging.basicConfig(level=logging.WARNING, format = "%(asctime)s [%(levelname)s] %(message)s")

# logging.debug("디버그 메세지")
# logging.info("디버그 메세지")
# logging.warning("디버그 메세지")
# logging.error("디버그 메세지")
# logging.critical("디버그 메세지")


# 터미널과 파일에 로그 남기기

logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()

# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
# %Y%m%d%H%M%S : 년, 월(소), 일(소), 시, 분, 초
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")

fileHandler = logging.FileHandler(filename, encoding = "utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

# 로그 메세지
logger.debug("디버그 메시지")
logger.warning("워닝 메시지")
logger.critical("크리티컬 메시지")
logger.debug("디버그 메시지")
logger.warning("워닝 메시지")
logger.critical("크리티컬 메시지")
logger.debug("디버그 메시지")
logger.warning("워닝 메시지")
logger.critical("크리티컬 메시지")
logger.debug("디버그 메시지")
logger.warning("워닝 메시지")
logger.critical("크리티컬 메시지")
logger.debug("디버그 메시지")
logger.warning("워닝 메시지")
logger.critical("크리티컬 메시지")
logger.debug("디버그 메시지")
logger.warning("워닝 메시지")
logger.critical("크리티컬 메시지")
logger.debug("디버그 메시지")
logger.warning("워닝 메시지")
logger.critical("크리티컬 메시지")
logger.debug("디버그 메시지")
logger.warning("워닝 메시지")
logger.critical("크리티컬 메시지")
logger.debug("디버그 메시지")
logger.warning("워닝 메시지")
logger.critical("크리티컬 메시지")