if __name__ == '__main__':
    poem_dict = {}

    with open('04_hashMaps/poem.txt') as file:
        for row in file:
            words = row.split(" ")
            for word in words:
                word=word.replace('\n','')
                if word in poem_dict:
                    poem_dict[word] += 1
                else:
                    poem_dict[word] = 1    

    print(poem_dict)
                    
                
        