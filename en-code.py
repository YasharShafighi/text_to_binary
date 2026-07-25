def text_to_binary():
    while True:
        print("\n" + "="*40)
        text = input("Enter your text (or 'exit' to quit): ")
        
        if text.lower() == "exit":
            print("Program terminated.")
            break
        
        if not text.strip():
            print("Error: Empty text entered!")
            continue
        
        binary = " ".join(format(ord(char), "08b") for char in text)
        
        print("\n📝 Original text:", text)
        print("🔢 Binary:")
        print(binary)
        print("📊 Character count:", len(text))
        print("📏 Binary length:", len(binary.replace(" ", "")))
        
        # Show character conversion table
        print("\n📋 Conversion table:")
        for char in text:
            print(f"  '{char}'  →  {format(ord(char), '08b')}")
        
        # Ask to continue
        again = input("\n🔄 Convert again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Program terminated.")
            break

if __name__ == "__main__":
    print("🔹 Text to Binary Converter 🔹")
    text_to_binary()