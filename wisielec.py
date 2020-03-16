import os
from random import choice
from string import ascii_lowercase

global word, encrypted, mistakes, finish

word_list = (
    'lekkoatletyka', 'interpunkcja', 'telekomunikacja', 'metamorfoza', 'zwierzchnictwo', 'prześladowanie',
    'antyterrorysta',
    'dźwiękonaśladownictwo', 'antykoncepcja', 'kolorowanka', 'konstantynopolitański', 'lumpenproletariat',
    'luminescencja', 'magnetoelektryczny', 'malkontenctwo', 'primaaprilisowy', 'pięćdziesięciogroszówka',
    'anatomopatologiczny', 'deoksyrybonukleinowy', 'niekonwencjonalny', 'Elaborat', 'Dyletant', 'Miraż', 'Kuriozum',
    'Trywialny', 'Eksplikacja', 'Reminiscencja', 'Abstrahować', 'Relewantny', 'Konkluzja', 'Afirmacja', 'Pejoratywny',
    'Frywolność', 'Konfabulacja', 'Defetyzm', 'Eskalować', 'Afront')
word = list(choice(word_list))
encrypted = ['-'] * len(word)
mistakes = 0
finish = False

available_letters = list(ascii_lowercase)
available_letters.extend(['ą', 'ę', 'ć', 'ź', 'ś', 'ł', 'ż', 'ń', 'ó'])
available_letters.sort()
message = ''
all_letters = list(available_letters)


def hangman(mistakes=0, win=False):
    if mistakes == 0:
        print('')
        return
    stage1 = stage2 = stage3 = stage4 = stage5 = stage6 = stage7 = stage8 = stage9 = stage10 = \
        stage11 = stage12 = stage13 = stage14 = stage15 = stage16 = stage17 = stage18 = stage19 = \
        stage20 = stage21 = stage22 = stage23 = stage24 = stage25 = stage26 = ' '
    if mistakes >= 1:
        stage1 = '/'
        stage2 = '\\'
    if mistakes >= 2:
        stage3 = '/'
        stage4 = '\\'
    if mistakes >= 3:
        stage5 = '-' * 42
    if mistakes >= 4:
        stage6 = '|'
    if mistakes >= 5:
        stage7 = '|'
    if mistakes >= 6:
        stage8 = ''
        stage8 = stage8.join(('|', '-' * 42, '|'))
    if mistakes >= 7:
        stage9 = '/'
    if mistakes >= 8:
        stage10 = '\\'
    if mistakes >= 9:
        stage11 = '|'
    if mistakes >= 10:
        stage12 = '/'
    if mistakes >= 11:
        stage13 = '\\'
    if mistakes >= 12:
        stage14 = '-'
        stage15 = '\\'
        stage16 = '/'
        stage17 = 'o'
    if mistakes >= 13:
        stage18 = '|'
    if mistakes >= 14:
        stage17 = 'x'
        stage5 = ' ' * 42
    if win == True:
        stage9 = stage10 = stage11 = stage12 = stage13 = \
            stage14 = stage15 = stage16 = stage17 = stage18 = ' '
        stage19 = '\\'
        stage20 = 'v'
        stage21 = '|'
        stage22 = '/'
        stage23 = '_' * 5
        stage24 = '^ ^'
        stage25 = '-' * 3
        stage26 = ' ' * (65 - len(stage5))
    hangman = \
        f'\n           {stage8}\n' \
        f'           {stage6}                    {stage18}                     {stage7}\n' \
        f'           {stage6}                    {stage18}                     {stage7}\n' \
        f'           {stage6}                    {stage18}                     {stage7}\n' \
        f'           {stage6}                   {stage14}{stage14}{stage14}                    {stage7}\n' \
        f'           {stage6}                  {stage16}{stage17} {stage17}{stage15}                   {stage7}\n' \
        f'           {stage6}                  {stage15} {stage14} {stage16}                   {stage7}\n' \
        f'           {stage6}                   {stage14}{stage14}{stage14}                    {stage7}                    {stage21}{stage19}{stage22}{stage19}{stage22}{stage19}{stage21}\n' \
        f'           {stage6}                   {stage12}{stage11}{stage13}                    {stage7}                    {stage21}{stage23}{stage21}\n' \
        f'           {stage6}                  {stage12} {stage11} {stage13}                   {stage7}                    {stage22} {stage24} {stage19}\n' \
        f'           {stage6}                 {stage12}  {stage11}  {stage13}                  {stage7}                    {stage19}  {stage20}  {stage22}\n' \
        f'           {stage6}                   {stage9} {stage10}                    {stage7}                   {stage19} {stage19}{stage25}{stage22} {stage22}\n' \
        f'           {stage6}                  {stage9}   {stage10}                   {stage7}                    {stage19}  {stage21}  {stage22}\n' \
        f'           {stage6}                 {stage9}     {stage10}                  {stage7}                     {stage19} {stage21} {stage22}\n' \
        f'           {stage6}                {stage9}       {stage10}                 {stage7}                      {stage19}{stage21}{stage22}\n' \
        f'           {stage6}{stage5}{stage7}{stage26}{stage21}\n' \
        f'          {stage1} {stage2}                                        {stage3} {stage4}                     {stage22} {stage19}\n' \
        f'         {stage1}   {stage2}                                      {stage3}   {stage4}                   {stage22}   {stage19}\n' \
        f'        {stage1}     {stage2}                                    {stage3}     {stage4}                 {stage22}     {stage19}\n' \
        f'       {stage1}       {stage2}                                  {stage3}       {stage4}               {stage22}       {stage19}\n' \
        f'      {stage1}         {stage2}                                {stage3}         {stage4}             {stage22}         {stage19}\n' \
        f'     {stage1}           {stage2}                              {stage3}           {stage4}\n'
    print(hangman)


def show_encrypted_word():
    for letter in encrypted:
        print(letter, end=' ')
    print()


def check_win_or_loose():
    global word, encrypted, mistakes, finish
    if word == encrypted:
        finish = True
        hangman(mistakes, finish)
        print('Wygrales')
        print('Slowo to:', ''.join(word))
    if mistakes == 14:
        hangman(mistakes)
        print('Przegrales')
        print('Szukane slowo:', ''.join(word))
        finish = True


while not finish:
    found = False
    os.system('cls')
    hangman(mistakes)
    print(message)
    print('Dostepne litery:\n', ' '.join(available_letters))
    show_encrypted_word()
    print(f'Pozostało prób: {14 - mistakes}')
    given = input('Podaj litere: ')
    if str(given) in all_letters:
        try:
            available_letters.remove(given)
        except ValueError:
            message = 'Juz podawałeś tą literę'
            mistakes += 1
            check_win_or_loose()
            continue
    else:
        message = 'Nieprawidłowa wartosć'
        mistakes += 1
        check_win_or_loose()
        continue
    for i in range(len(word)):
        if given == word[i]:
            encrypted[i] = given
            found = True
            message = f'Znalazłeś literę: {given}'
    if not found:
        message = 'Pudło :c'
        mistakes += 1
    check_win_or_loose()
