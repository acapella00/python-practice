# ==============================================
# 모듈 import
# ==============================================

import theater_module
theater_module.price(3) 
theater_module.price_morning(4) 
theater_module.price_soldier(5) 

# ==============================================
# 모듈 별칭
# ==============================================
import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

# ==============================================
# 특정 모듈 전체 import
# ==============================================
from theater_module import *
# from random import *
price(3)
price_morning(4)
price_soldier(5)

# ==============================================
# 필요한 함수만 import
# ==============================================
from theater_module import price, price_morning
price(5)
price_morning(6)

# ==============================================
# 함수 별칭
# ==============================================
from theater_module import price_soldier as price
price(5)
