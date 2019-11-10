def alarm_clock(day, vacation):
  weekdays = [1, 2, 3, 4, 5]
  alarm = None
  if day in weekdays:
    if vacation == False:
      alarm = "7:00"
    else:
      alarm = "10:00"
  else:
    if vacation == False:
      alarm = "10:00"
    else:
      alarm = "off"
      
  return alarm