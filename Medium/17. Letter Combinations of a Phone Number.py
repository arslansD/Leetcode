from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        interpret_digit = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        all_combinations = [
            ""] if digits else []  # если есть цифры, то список с пустой строкой, если нет, то пустой вывод
        for digit in digits:  # для каждой цифры
            current_combinations = []  # нынешняя комбинация пустая
            for letter in interpret_digit[digit]:  # для каждой буквы в нынешней цифре
                for combination in all_combinations:  # создаем комбинацию
                    current_combinations.append(combination + letter)  # добавляем старые буквы к нынешней
            all_combinations = current_combinations  # после прохода, переопределяем старый список комбинаций
        return all_combinations  # выводим все комбинации
