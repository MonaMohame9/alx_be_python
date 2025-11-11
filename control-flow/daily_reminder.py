# daily_reminder.py

# طلب إدخال المهمة من المستخدم
task = input("Enter your task for today: ")

# طلب أولوية المهمة
priority = input("Enter the priority of the task (high/medium/low): ").lower()

# السؤال إذا كانت المهمة محددة بالوقت
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# استخدام Match Case لمعالجة المهمة حسب الأولوية
match priority:
    case "high":
        reminder = f"High priority task: {task}"
    case "medium":
        reminder = f"Medium priority task: {task}"
    case "low":
        reminder = f"Low priority task: {task}"
    case _:
        reminder = f"Task: {task} (unknown priority)"

# تعديل التذكير إذا كانت المهمة محددة بالوقت
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# طباعة التذكير النهائي
print("\nYour reminder:")
print(reminder)
