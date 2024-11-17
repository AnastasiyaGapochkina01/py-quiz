#!/usr/bin/python3
import random
QUESTIONS = [
          ("Какой океан является самым большим на Земле", "тихий"),
          ("Какое животное является символом Австралии", "кенгуру"),
          ("Какой цвет получается при смешивании красного и синего", "фиолетовый"),
          ("Как называется столица Франции", "париж"),
        ]

def quiz():
    print("Добро пожаловать на Quiz!")
    answer=input('Готовы сыграть ? (да/нет): ')
    score=0
    total_questions=4

    if answer.lower()=='да':
      random.shuffle(QUESTIONS)
      for question, correct_answer in QUESTIONS:
          answer = input(f"{question}? ")
          if answer.strip().lower() == correct_answer:
              print('Верно!')
              score += 1
          else:
              print('Неверно :(') 

      print(f'Спасибо за игру! Вы ответили на {score} вопроса(ов) из {total_questions}')
      print('До новых встреч!')

if __name__ == "__main__":
    quiz()