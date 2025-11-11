# multiplication_table.py

# طلب الرقم من المستخدم
number = int(input("Enter a number to see its multiplication table: "))

# إنشاء جدول الضرب باستخدام حلقة for
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
