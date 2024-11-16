def open_file():
    with open("books/frankenstein.txt") as f:
        files_contents = f.read()
    
    return files_contents

def count_words(text):
    words = text.split()

    return len(words)
    

def count_characters(text):
    count_dict = {}
    lowered_text = text.lower()
    unique = set(lowered_text)

    for i in unique:
        count_dict[i] = 0

    for i in lowered_text:
        if i in count_dict:
            count = count_dict[i]
            count_dict[i] = count + 1

    return count_dict


def each_count(dict_count):
    new_dic = {k:v for k, v in dict_count.items() if k.isalpha()}
    list_for_report = sorted(new_dic.items(), key=lambda item: item[1], reverse=True)
    return list_for_report


def report(list_for_report, text):
    words = count_words(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print()
    
    for i in list_for_report:
        print(f"The {i[0]} character was found {i[1]} times")
    print("--- End report ---")

def main():
    text = open_file()
    dict_count = count_characters(text)
    count = each_count(dict_count)
    report(count, text)

main()







        

        










    