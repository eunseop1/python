from konlpy.tag import Kkma
from konlpy.utils import pprint

a = Kkma()

pprint(a.sentences(u'네, 안녕하세요. 반갑습니다.'))

# ['네, 안녕하세요.', '반갑습니다.']
