from rest_framework import viewsets, serializers
from api.base import BaseNestedSerializer
from reservations.models import Reservation
from .reservation_units_api import ReservationUnitSerializer


class ReservationSerializer(BaseNestedSerializer):
    # reservation_unit = ReservationUnitSerializer(many=True, exclude_detail_fields=True)

    class Meta:
        model = Reservation
        fields = [
            "id",
            "state",
            "priority",
            "user",
            "begin",
            "end",
            "buffer_time_before",
            "buffer_time_after",
            "reservation_unit",
            "recurring_reservation",
        ]
        read_only_fields = ["state", "priority", "user"]

    # def validate(self, data):
    #     for reservation_unit in data["reservation_unit"]:
    #         if reservation_unit.check_reservation_overlap(data["begin"], data["end"]):
    #             raise serializers.ValidationError(
    #                 "Overlapping reservations are not allowed"
    #             )
    #     return data


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = (
        Reservation.objects.all()
        .prefetch_related("reservation_unit")
        .select_related("recurring_reservation")
    )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
