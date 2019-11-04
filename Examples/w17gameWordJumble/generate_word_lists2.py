
if __name__ == "__main__":
    word_list = []
    with open('dictionary.txt', 'r') as f:
        for line in f:
            word_list.append(line.strip())        
    f.close()

    #word_list = [x for x in word_list if x[0] == "A"]
    

    
    
    with open('word_lists2.py', 'w') as f:
        f.write("dictionary_list = ")
        f.write(str(word_list))
    f.close()
    