from string import ascii_letters as letters
import random
import sys


MIN_WORD_LENGTH = 5
MAX_WORD_LENGTH = 10


def get_args():
    if len(sys.argv) == 1:
        print(''''\
how to run: python3 <chapter_count> <chapter_length> (file_name)\n
chapter_count - positional, how many chapters will be in the book
chapter_length - positional, the length of each chapter
file_name = optional, the file with which the book will be saved, default: random_book1''')
        exit(0)
    ch_count, max_words_in_chapter = int(sys.argv[1]), int(sys.argv[2])
    try:
        fname = sys.argv[3]
    except IndexError:
        fname = None
    return ch_count, max_words_in_chapter, fname


def generate_word():
    word = ''.join(random.sample(letters, 
                   random.randint(MIN_WORD_LENGTH, MAX_WORD_LENGTH)))
    return word

def generate_chapter(words_in_chapter):
    chapter = []  # chapter content
    line = []
    while words_in_chapter > 0:
        if random.randint(0, 10) == 0 and line:  
            chapter.append(' '.join(line) + '.')
            line.clear()
        else:
            line.append(generate_word())
            words_in_chapter -= 1
    if line:
        chapter.append(' '.join(line) + '.')
    return '\n'.join(chapter) + '\n'
            
    

def generate_book(ch_count, max_words_in_chapter, book_name):
    curr_chapter = 1
    with open(book_name, 'w') as f:
        while curr_chapter <= ch_count:
            f.write(f'# Chapter {curr_chapter}\n\n')
            f.write(generate_chapter(max_words_in_chapter))
            f.write('\n')
            curr_chapter += 1


def main():
    # print(generate_word())
    ch_count, max_words_in_chapter, fname = get_args()
    if fname == None:
        book_name = 'random_book1.txt'
    else:
        book_name = fname
    generate_book(ch_count, max_words_in_chapter, book_name)
    # print(generate_chapter(20))

if __name__ == "__main__":
    main()