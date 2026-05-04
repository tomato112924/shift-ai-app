def generate_shift(hourly_wage, target_income, available_days, max_hours_per_day):
   required_hours = target_income / hourly_wage
   days_count = len(available_days)
   hours_per_day = required_hours / days_count
   shift_plan = {}
   for day in available_days:
       shift_plan[day] = min(hours_per_day, max_hours_per_day)
   return shift_plan
# サンプル
shift = generate_shift(1100, 50000, ["月","火","木","金"], 6)
print(shift)
