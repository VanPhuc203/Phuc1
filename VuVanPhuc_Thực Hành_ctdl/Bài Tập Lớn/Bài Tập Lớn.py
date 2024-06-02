import json
import os
# Mỗi mục từ là một từ tiếng Anh có nhiều nghĩa, mỗi nghĩa có ba phần: loại từ, nghĩa, ví dụ.
class DictionaryEntry:
    def __init__(self, word, meanings):
        self.word = word
        self.meanings = meanings  # meanings là danh sách các nghĩa, mỗi nghĩa là một từ điển

    def __repr__(self):
        return f"{self.word}: {self.meanings}"

# Từ điển là danh sách các DictionaryEntry
class Dictionary:
    def __init__(self):
        self.entries = []

    def load_from_file(self, filename):
        """Nạp từ điển từ tập tin văn bản"""
        self.entries = []
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    # Mỗi dòng chứa từ và nghĩa dưới dạng JSON
                    word, meanings_json = line.strip().split('\t')
                    meanings = json.loads(meanings_json)
                    entry = DictionaryEntry(word, meanings)
                    self.entries.append(entry)
            print("Từ điển đã được nạp từ tập tin văn bản.")
        except FileNotFoundError:
            print("Không tìm thấy tập tin. Tạo một từ điển mới.")
        

    def save_to_file(self, filename):
        """Lưu từ điển vào tập tin văn bản"""
        with open(filename, 'w', encoding='utf-8') as file:
            for entry in self.entries:
                # Lưu trữ từ và nghĩa của nó dưới dạng JSON trong một dòng
                line = f"{entry.word}\t{json.dumps(entry.meanings, ensure_ascii=False)}\n"
                file.write(line)
        print("Từ điển đã được lưu vào tập tin văn bản.")

    def add_entry(self, entry):
        """Thêm một mục từ mới vào từ điển"""
    # Kiểm tra xem từ đã tồn tại hay chưa
        for existing_entry in self.entries:
         if existing_entry.word == entry.word:
            print("Từ này đã tồn tại trong từ điển!")
            return
    # Thêm mục từ mới nếu chưa tồn tại
        self.entries.append(entry)
        
        self.selection_sort()

        print(f"Đã thêm mục từ '{entry.word}' vào từ điển.")
        print(self.entries)


    
    def remove_entry(self, word):
        """Loại bỏ một mục từ của từ điển"""
        for i, entry in enumerate(self.entries):
            if entry.word == word:
                del self.entries[i]
                print(f"Đã loại bỏ mục từ '{word}' khỏi từ điển.")
                return
        print(f"Không tìm thấy mục từ '{word}' trong từ điển.")

    def lookup_word(self, word):
        """Tra cứu các nghĩa của một mục từ trong từ điển"""
        for entry in self.entries:
            if entry.word == word:
                for meaning in entry.meanings:
                    print(f"===== {word} =====")
                    print(f"Loại từ: {meaning['word_type']}")
                    print(f"Nghĩa: {meaning['definition']}")
                    print(f"Ví dụ: {meaning['example']}")
                    print(f"===============")
                return
        print(f"Không tìm thấy mục từ '{word}' trong từ điển.")
    def selection_sort(self):
        entries = self.entries
        n = len(entries)
        for i in range(n):
        # Tìm phần tử nhỏ nhất trong đoạn [i..n-1]
            min_idx = i
            for j in range(i + 1, n):
                if entries[j].word < entries[min_idx].word:
                    min_idx = j
        
        # Hoán đổi phần tử nhỏ nhất với phần tử đầu tiên trong đoạn [i..n-1]
            entries[i], entries[min_idx] = entries[min_idx], entries[i]
    

def main():
    dictionary = Dictionary()
    filename = 'VUVANPHUC_mang.txt'  # Tên tập tin văn bản để lưu/nạp từ điển
    while True:
        os.system("cls")
        print("\n============== Menu ==============")
        print("1. Thêm một mục từ mới vào từ điển")
        print("2. Loại bỏ một mục từ khỏi từ điển")
        print("3. Tra cứu các nghĩa của một mục từ trong từ điển")
        print("4. Lưu từ điển vào tập tin văn bản")
        print("5. Nạp từ điển từ tập tin văn bản")
        print("6. Kết thúc chương trình")
        print("============== END ==============")
        choice = input("Chọn chức năng (1-6): ")
        
        if choice == "1":
            word = input("Nhập từ: ")
            num_meanings = int(input("Số nghĩa của từ này: "))
            meanings = []
            for i in range(num_meanings):
                word_type = input(f"Nhập loại từ (danh từ, động từ, tính từ...) cho nghĩa {i + 1}: ")
                definition = input(f"Nhập nghĩa cho nghĩa {i + 1}: ")
                example = input(f"Nhập ví dụ cho nghĩa {i + 1}: ")
                meaning = {
                    'definition': definition,
                    'word_type': word_type,
                    'example': example
                }
                meanings.append(meaning)
            os.system("cls")
            entry = DictionaryEntry(word, meanings)
            dictionary.add_entry(entry)
            os.system("pause")
        
        elif choice == "2":
            word = input("Nhập từ cần loại bỏ: ")
            os.system("cls")
            dictionary.remove_entry(word)
            os.system("pause")
        
        elif choice == "3":
            word = input("Nhập từ cần tra cứu: ")
            os.system("cls")
            dictionary.lookup_word(word)
            os.system("pause")
        
        elif choice == "4":
            dictionary.save_to_file(filename)
            os.system("pause")
        elif choice == "5":
            dictionary.load_from_file(filename)
            os.system("pause")
        
        elif choice == "6":
            print("Kết thúc chương trình.")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
       
if __name__ == "__main__":
    main()
