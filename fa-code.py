def text_to_binary():
    while True:
        print("\n" + "="*40)
        text = input("متن رو وارد کن (یا 'خروج' برای پایان): ")
        
        if text.lower() == "خروج":
            print("برنامه خاتمه یافت.")
            break
        
        if not text.strip():
            print("خطا: متن خالی وارد کردی!")
            continue
        
        binary = " ".join(format(ord(char), "08b") for char in text)
        
        print("\n📝 متن اصلی:", text)
        print("🔢 باینری:")
        print(binary)
        print("📊 تعداد کاراکترها:", len(text))
        print("📏 طول باینری:", len(binary.replace(" ", "")))
        
        # نمایش جدول کاراکترها
        print("\n📋 جدول تبدیل:")
        for char in text:
            print(f"  '{char}'  →  {format(ord(char), '08b')}")
        
        # پیشنهاد ادامه
        again = input("\n🔄 دوباره تبدیل کنی؟ (بله/خیر): ").strip()
        if again.lower() not in ["بله", "بل", "yes", "y"]:
            print("برنامه خاتمه یافت.")
            break

if __name__ == "__main__":
    print("🔹 برنامه تبدیل متن به باینری 🔹")
    text_to_binary()