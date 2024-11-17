import unittest
from unittest.mock import patch
from io import StringIO
import random

# Импортируем функцию quiz из вашего основного файла
from main import quiz  # Замените 'ваш_файл' на имя вашего файла без .py

class TestQuiz(unittest.TestCase):

    @patch('builtins.input', side_effect=['да', 'тихий', 'кенгуру', 'фиолетовый', 'париж'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_quiz_correct_answers(self, mock_stdout, mock_input):
        random.seed(0)  # Устанавливаем начальное значение для воспроизводимости
        quiz()
        
        output = mock_stdout.getvalue()
        self.assertIn('Верно!', output)
        self.assertIn('Спасибо за игру! Вы ответили на 4 вопроса(ов) из 4', output)

    @patch('builtins.input', side_effect=['да', 'неверный ответ', 'неверный ответ', 'неверный ответ', 'неверный ответ'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_quiz_incorrect_answers(self, mock_stdout, mock_input):
        random.seed(0)  # Устанавливаем начальное значение для воспроизводимости
        quiz()
        
        output = mock_stdout.getvalue()
        self.assertIn('Неверно :(', output)
        self.assertIn('Спасибо за игру! Вы ответили на 0 вопроса(ов) из 4', output)

    @patch('builtins.input', side_effect=['нет'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_quiz_decline(self, mock_stdout, mock_input):
        quiz()
        
        output = mock_stdout.getvalue()
        self.assertIn("Добро пожаловать на Quiz!", output)
        self.assertIn("Готовы сыграть ? (да/нет): ", output)

if __name__ == '__main__':
    unittest.main()