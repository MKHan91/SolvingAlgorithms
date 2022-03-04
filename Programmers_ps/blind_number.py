def solution(phone_number):
    # answer = "*" * len(phone_number[:-4]) + phone_number[len(phone_number[:-4]):]
    answer = phone_number.replace(phone_number[:-4], "*" * len(phone_number[:-4]))
    return answer

if __name__ == "__main__":
    phone_number = "01033334444"
    print(solution(phone_number))