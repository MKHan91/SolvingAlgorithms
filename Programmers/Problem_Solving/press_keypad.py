def solution(numbers, hand):
    answer = ''
    LeftHand = [1, 4, 7]
    RightHand = [3, 6, 9]
    NearbyNumber_dict = {0: ["8", "*", "#"], 1: ["2", "4"], 2: ["1", "5", "3"], 3: ["2", "6"], 4: ["1", "5", "7"], 5: ["2", "4", "6", "8"],
                         6: ["3", "5", "9"], 7: ["4", "8"], 8: ["5", "7", "9", "0"], 9: ["6", "8"]}
    left_pos = "*"
    right_pos = "#"
    for number in numbers:
        if number in LeftHand:
            answer += "L"
            left_pos += str(number)

        elif number in RightHand:
            answer += "R"
            right_pos += str(number)

        else:
            near_numbers = NearbyNumber_dict[number]
            if left_pos[-1] in near_numbers and right_pos[-1] in near_numbers:
                answer += hand.capitalize()[0]
                if hand == "right":
                    right_pos += str(number)
                elif hand == "left":
                    left_pos += str(number)

            elif left_pos[-1] in near_numbers:
                answer += "L"
                left_pos += str(number)

            elif right_pos[-1] in near_numbers:
                answer += "R"
                right_pos += str(number)

            else:
                if abs(number - int(left_pos[-1])) == 1 and abs(number - int(right_pos[-1])) == 1:
                    answer += hand.capitalize()[0]
                    if hand == "right":
                        right_pos += str(number)
                    elif hand == "left":
                        left_pos += str(number)
                else:
                    answer += answer[-1]
    return answer

def solution2(numbers, hand):
    answer = ''
    hand_loc = {
        "1" : (1,4),
        "2" : (2,4),
        "3" : (3,4),
        "4" : (1,3),
        "5" : (2,3),
        "6" : (3,3),
        "7" : (1,2),
        "8" : (2,2),
        "9" : (3,2),
        "*" : (1,1),
        "0" : (2,1),
        "#" : (3,1),
    }
    r_loc = (3,1)
    l_loc = (1,1)
    
    LeftHand = [1, 4, 7]
    RightHand = [3, 6, 9]
    for number in numbers:
        if number in LeftHand:
            answer += "L"
            l_loc = hand_loc[str(number)]
            
        elif number in RightHand:
            answer += "R"
            r_loc = hand_loc[str(number)]

        else:
            query_loc = hand_loc[str(number)]
            right = abs(query_loc[0] - r_loc[0]) + abs(query_loc[1] - r_loc[1])
            left = abs(query_loc[0] - l_loc[0]) + abs(query_loc[1] - l_loc[1])
            if right > left:
                answer += "L"
                l_loc = query_loc
                
            elif right < left:
                answer += "R"
                r_loc = query_loc
            
            else:
                answer += hand.capitalize()[0]
                if hand == "right":
                    r_loc = query_loc
                elif hand == "left":
                    l_loc = query_loc
                    
    return answer

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    # numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    # numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand = "right"
    # hand = "right"
    # hand = "left"
    result = solution2(numbers, hand)
    print(result)