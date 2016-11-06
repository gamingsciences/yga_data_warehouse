from __future__ import unicode_literals
import datetime
from django.db import models
from taggit.managers import TaggableManager


class DateDimension(models.Model):
    datekey = models.IntegerField(primary_key=True)
    full_date = models.DateField()
    day_of_week = models.IntegerField()
    day_num_in_month = models.IntegerField()
    day_name = models.CharField(max_length=9)
    day_abbrev = models.CharField(max_length=3)
    weekday_flag = models.BooleanField()
    week_num_in_year = models.IntegerField()
    week_begin_date = models.DateField()
    week_begin_datekey = models.IntegerField()
    month = models.IntegerField()
    month_name = models.CharField(max_length=9)
    month_abbrev = models.CharField(max_length=3)
    quarter = models.CharField(max_length=5)
    year = models.IntegerField()
    yearmo = models.IntegerField()
    month_end_flag = models.BooleanField()
    holiday_flag = models.BooleanField()
    
    def __str__(self):
        return "%d" % self.datekey
    
    class Meta:
        db_table = 'date_dim'


class TimeDimension(models.Model):
    minute_of_day = models.IntegerField(default=0)
    hour = models.IntegerField(default=0)
    minute = models.IntegerField(default=0)
    clock_time = models.CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):
        return "%d" % self.minute_of_day
    
    class Meta:
        db_table = 'time_dim'


class ShiftDimension(models.Model):
    shift = models.CharField(max_length= 20, null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return "%s" % self.shift
        
    class Meta:
        db_table = 'shift_dim'
        
class PlayerDimension(models.Model):
    player_id = models.IntegerField()
    effective_date = models.DateTimeField()
    expiration_date = models.DateTimeField(default=datetime.datetime(9999, 12, 31))
    current = models.BooleanField(default=False)
    date_joined = models.DateField()
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=5, null=True)
    email = models.CharField(max_length=50, null=True)
    address_a = models.CharField(max_length=50, null=True)
    address_b = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    city_state = models.CharField(max_length=50, null=True)
    zip_code = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    call_flag = models.BooleanField(default=False)
    mail_flag = models.BooleanField(default=False)
    distance = models.IntegerField(null=True)
    addr_lat = models.FloatField(null=True)
    addr_lon = models.FloatField(null=True)
    
    def __str__(self):
        return "%d" % (self.id)
        
    class Meta:
        db_table = 'player_dim'
        unique_together = ('player_id', 'effective_date')


class SlotGameDimension(models.Model):
    slot_number = models.IntegerField()
    effective_date = models.DateTimeField()
    expiration_date = models.DateTimeField(default=datetime.datetime(9999, 12, 31))
    current = models.BooleanField(default=False)
    game_type = models.CharField(max_length=50, null=True)
    denomination = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=50, null=True)
    cabinet = models.CharField(max_length=50, null=True)
    par = models.FloatField(null=True)
    num_reels = models.IntegerField(null=True)
    num_coins = models.IntegerField(null=True)
    num_paylines = models.IntegerField(null=True)
    volatility = models.FloatField(blank=True, null=True)
    progressive = models.BooleanField(default=False)
    manufacturer = models.CharField(max_length=50, null=True)
    multigame = models.BooleanField(default=False)
    multidenom = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)
    
    def __str__(self):
        return "%d" % (self.id)
        
    class Meta:
        db_table = 'slotgame_dim'
        unique_together = ('slot_number', 'effective_date')

        
class PitGameDimension(models.Model):
    oasis_id = models.IntegerField()
    game = models.CharField(max_length=50)
    game_type = models.CharField(max_length=50)
    pit = models.CharField(max_length=50)
    
    def __str__(self):
        return "%d" % (self.oasis_id)
        
    class Meta:
        db_table = 'pitgame_dim'
        
class EmployeeDimension(models.Model):
    employee_id = models.IntegerField(unique=True)
    user_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return "%s" % (self.user_name)
        
    class Meta:
        db_table = 'employee_dim'
    
class LocationDimension(models.Model):
    casino = models.CharField(max_length=50, null=True)
    area = models.CharField(max_length=5, null=True)
    section = models.CharField(max_length=5, null=True)
    position = models.CharField(max_length=5, null=True)
    location = models.CharField(max_length=20, null=True)
    bank_type = models.CharField(max_length=20, null=True)
    position_type = models.CharField(max_length=20, null=True)
    non_smoking_flag = models.BooleanField(default=False)
    
    def __str__(self):
        return "%d" % (self.id)
        
    class Meta:
        db_table = 'location_dim'
        unique_together = ('casino', 'area', 'section', 'position')

class DailyBudgetDimension(models.Model):
    budget_date = models.DateField()
    casino = models.CharField(max_length=50, null=True)
    previous_year_slot_win = models.FloatField()
    budget_slot_win = models.FloatField()
    budget_coin_in = models.FloatField()
    budget_table_win = models.FloatField()
    budget_f_and_b_revenue = models.FloatField()
    
    def __str__(self):
        return "%d" % (self.id)
        
    class Meta:
        db_table = 'daily_budget_dim'
        unique_together = ('casino', 'budget_date')
