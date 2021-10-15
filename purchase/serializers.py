from purchase.models import Purchase
from rest_framework import serializers


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('user_id', 'books', 'issued', 'amount',
                  'created_at', 'status')
