from django.contrib import admin
from .models import ReservationUnit, Period, Day, DayPart


@admin.register(ReservationUnit)
class ReservationUnitAdmin(admin.ModelAdmin):
    model = ReservationUnit


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    model = Period


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    model = Day


@admin.register(DayPart)
class DayPartAdmin(admin.ModelAdmin):
    model = DayPart