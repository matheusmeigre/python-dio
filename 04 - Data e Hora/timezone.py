from datetime import datetime, timezone, timedelta

data_london = datetime.now(timezone(timedelta(hours=2), "BRT")) #BRT = name, todo Name = None e será usado para retornar do método tzname
data_sp = datetime.now(timezone(timedelta(hours=-3)))

print(data_london)
print(data_sp)
