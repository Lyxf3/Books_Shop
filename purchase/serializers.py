from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from user.models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('user_id', 'books', 'issued', 'amount',
                  'created_at', 'status')
