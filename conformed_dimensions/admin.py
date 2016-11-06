from django.contrib import admin

from .models import DateDimension, TimeDimension, ShiftDimension, PlayerDimension,\
                    SlotGameDimension, PitGameDimension, LocationDimension,\
                    EmployeeDimension, DailyBudgetDimension


@admin.register(DateDimension)
class DateDimensionAdmin(admin.ModelAdmin):
    pass


@admin.register(TimeDimension)
class TimeDimensionAdmin(admin.ModelAdmin):
    pass


@admin.register(ShiftDimension)
class ShiftDimensionAdmin(admin.ModelAdmin):
    pass


@admin.register(PlayerDimension)
class PlayerDimensionAdmin(admin.ModelAdmin):
    search_fields = ('player_id',)


@admin.register(SlotGameDimension)
class SlotGameDimensionAdmin(admin.ModelAdmin):
    search_fields = ('slot_number',)


@admin.register(PitGameDimension)
class PitGameDimensionAdmin(admin.ModelAdmin):
    pass


@admin.register(EmployeeDimension)
class EmployeeDimensionAdmin(admin.ModelAdmin):
    pass


@admin.register(LocationDimension)
class LocationDimensionAdmin(admin.ModelAdmin):
    search_fields = ('location',)
    list_display = ('casino', 'area', 'section', 'position')


@admin.register(DailyBudgetDimension)
class DailyBudgetDimensionAdmin(admin.ModelAdmin):
    list_display = ('casino', 'budget_date')
