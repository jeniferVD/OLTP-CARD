from rest_framework import routers
from .views import UserViewset, CardViewset, AccountViewset, TransactionViewset

router = routers.DefaultRouter()
router.register("user", UserViewset, "user")
router.register("card", CardViewset, "card")
router.register("account", AccountViewset, "account")
router.register("transaction", TransactionViewset, "transaction")

urlpatterns = router.urls
