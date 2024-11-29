import requests
import re


class MyTypeError(TypeError):
    def __init__(self, var_name, var):
        super().__init__(f"incorrect type for {var_name}: {type(var)}")


class HTTPRequestsError(Exception):
    def __init__(self, requests_code: int, requests_message: str):
        super().__init__(f"{requests_code}: {requests_message}")


def search_time(text: str) -> list:
    if not isinstance(text, str):
        raise MyTypeError("text", text)
    pattern_time = r"(?:0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]"
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

def url_data(url: str):
    raw_text = requests.get(url)
    if raw_text.status_code != 200:
        raise HTTPRequestsError(raw_text.status_code, raw_text.reason)
    times = search_time(raw_text.text)

    print("From url: ", times)

def main():
    try:
        user_input()
        url_data("https://time100.ru")

    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()