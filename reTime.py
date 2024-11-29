import requests
import re


class MyTypeError(TypeError):
    def __init__(self, var_name, var):
        super().__init__(f"incorrect type for {var_name}: {type(var)}")


def search_time(text: str) -> list:
    if not isinstance(text, str):
        raise MyTypeError("text", text)
    pattern_time = r"\b(?:0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]\b"
    matched_list = re.findall(pattern_time, text)

    return matched_list

def user_input():
    while True:
        text = input(
            "Введите время в формате ЧЧ:ММ:СС или Тусова для окончания ввода\n")

        if text == "Тусова":
            break

        if len(search_time(text)) == 1:
            print("Correct\n")
        else:
            print("Incorrect\n")

def main():
    try:
        user_input()

    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()