# طلب الدخل الشهري من المستخدم
monthly_income = float(input("Enter your monthly income: "))

# طلب المصروفات الشهرية من المستخدم
monthly_expenses = float(input("Enter your total monthly expenses: "))

# حساب المدخرات الشهرية
monthly_savings = monthly_income - monthly_expenses

# حساب المدخرات السنوية مع الفائدة
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# طباعة النتائج
print("Your monthly savings are:", monthly_savings)
print("Your projected savings after one year (with 5% interest) are:", projected_savings)
