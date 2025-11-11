# pattern_drawing.py

# طلب حجم المربع من المستخدم
size = int(input("Enter the size of the pattern: "))

# التحقق من أن الرقم موجب
if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0
    while row < size:
        # طباعة النجوم في كل صف
        for col in range(size):
            print("*", end="")
        print()  # للانتقال للسطر التالي
        row += 1
