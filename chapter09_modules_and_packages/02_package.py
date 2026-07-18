# ===========================================
# 패키지 import
# ===========================================

import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# ===========================================
# 클래스 직접 import
# ===========================================

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()
