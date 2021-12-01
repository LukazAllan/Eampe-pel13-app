import datetime as dt
#>>> dt.datetime.today()
#dt.datetime(2021, 8, 18, 20, 48, 23, 704065)
agora = dt.datetime.today()
#  class dt.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
# dt.date(2010, 6, 16).isocalendar()[1] >>> 24
aa = agora.year
mm = agora.month
dd = agora.day
#aa = 2021
#mm = 5
#dd = 10

(dt.date(aa,mm,dd).isocalendar()[1]-19)%30
