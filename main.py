import random

# Словарь азбуки Морзе
alphabet_dotted = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}

# Список, используемых слов и правильных ответов пользователя (True)
words = ["cat", "dog", "bird", "turtle", "snake"]  #список слов для перевода
answers = []   # список для правильных ответов


# Переводчик слов с англиского в Морзе (метод translate, maketrans)
def morse_encode(word_new):
  str = " ".join(word_new)
  word_translate = str.maketrans(alphabet_dotted)
  word_translate_end = str.translate(word_translate)
  return word_translate_end

# Другое декодирование(где поставить разделение по пробелам?)
#def symbol_to_word(word_new):
    #result = ""
   # for i in str(word_new):
        #result += alphabet_dotted[i]
    #return result


# Случайный выбор слова из списка words (метод random.choice)
def get_word():
    word_new = random.choice(words)
    return word_new

while True:
    input(f"Сегодня мы потренируемся расшифровывать азбуку Морзе. Нажмите Enter и начнем.")
    get_word()


# Вопросы пользователю (5 вопросов - 5ответов)
    for word_count in range(len(words)):
        word_new = get_word()
        answer = str(input(f"{word_count + 1} - {morse_encode(word_new)}!"))
        is_answer_true = answer == word_new
        answers.append(is_answer_true)
        if is_answer_true:
            print(f"Верно, {word_new}!")
        else:
            print(f"Неверно, {word_new}!")


# Статистика
    print(f"Всего задач: {len(words)} \n Отвечено верно: {answers.count(True)} \n Отвечено неверно: {answers.count(False)}")
    break
