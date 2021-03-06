"""
13. wordcount
Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.
Ou seja...
Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.
Por exemplo:
$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.
Ou seja...
Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.
Por exemplo:
$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2
Abaixo já existe um esqueleto do programa para você preencher.
Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.
Seu trabalho é implementar as funções print_words() e depois print_top().
"""

import sys

from typing import List, Dict


def read_all_words_in_the_file(file_name: str, separator: str = ' ') -> List[str]:
    words = []
    with open(file_name) as file:
        for line in file.readlines():
            for w in line.split(separator):
                words.append(w.lower())
    return words


def count_how_many_words_exists(words:List[str]) -> List[str]:
    words_count = []
    for w in words:
        find_word = False
        for item in words_count:
            if item.get('word') == w:
                item['count'] += 1
                find_word = True
        if not find_word:
            words_count.append({'word': w, 'count': 1})
    return words_count


def sort_words_by(words_count:List[Dict[str, int]], field:str, reverse:bool=False) -> None:
    def sort_words_by_key(e):
        return e.get(field)
    words_count.sort(key=sort_words_by_key, reverse=reverse)


# SEU CÓDIGO AQUI...
def print_words(file_name):
    SORT_BY_WORD_KEY = 'word'
    words = read_all_words_in_the_file(file_name)
    words_count = count_how_many_words_exists(words)
    sort_words_by(words_count, SORT_BY_WORD_KEY)
    for word_count in words_count:
        print(f"{word_count.get('word')} {word_count.get('count')}")


def print_top(file_name):
    TOP_MAX = 20
    SORT_BY_COUNT_KEY = 'count'
    words = read_all_words_in_the_file(file_name)
    words_count = count_how_many_words_exists(words)
    sort_words_by(words_count, SORT_BY_COUNT_KEY, reverse=True)
    for word_count in words_count[0:TOP_MAX]:
        print(f"{word_count.get('word')} {word_count.get('count')}")


# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
