from unittest import TestCase
from main import folder_creation, first_task, second_task, third_task

class HomeworkTester(TestCase):

    def test_homework_task1(self):
        russia_logs = first_task()
        expected = [
            {'visit1': ['Москва', 'Россия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ]
        self.assertEquals(expected, russia_logs)

    def test_homework_task2(self):
        list = second_task()
        check_list = [98, 35, 213, 54, 119, 15]
        self.assertEquals(list, check_list)

    def test_homework_task3(self):
        company = third_task()
        check = 'yandex'
        self.assertEquals(company, check)

    def test_create_folder(self):
        token = 'y0_AgAAAAAzTKoOAADLWwAAAADirnYaBAZfFooQRhSQlYuCtLWT-UTLq6U'
        res = folder_creation(token)
        success_responce = 201 #папка успешно создана
        self.assertEquals(res, success_responce)


    def test_created_folder(self):
        token = 'y0_AgAAAAAzTKoOAADLWwAAAADirnYaBAZfFooQRhSQlYuCtLWT-UTLq6U'
        res = folder_creation(token)
        created_responce = 409 #папка уже существует
        self.assertEquals(res, created_responce)
