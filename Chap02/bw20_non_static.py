from datetime import datetime
from time import sleep

# 로그 메세지를 출력한다고 해보자
def log(message, when=datetime.now()):
    print('%s %s' % (when, message))

# test
log('hello world!')
sleep(0.5)
log('hello again!')

# 기본값을 None 으로 하고 문서화 문자열을 추가해준다
def log(message, when=None):
    """
    시간과 문자열을 출력해준다
    :param message: 메세지내용
    :param when: 시간정보
    :return: 표준 화면 로깅
    """
    when = datetime.now() if when is None else when
    print('%s %s' % (when, message))

# test
log('hello world!')
sleep(0.5)
log('hello again!')


