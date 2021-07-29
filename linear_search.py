from datetime import datetime

def linearSearch(list, target):



    #returns the index position of the number we are searching
    #if not found returns None

    for i in range(0, len(list)):

        if list[i] == target:
            return i


    return None


def verify(list, target_num):
    start = datetime.now()
    linearSearch(list, target_num)
    end = datetime.now()
    time_taken = end - start
    print("Time taken to complete: ", time_taken )






targetNumber = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 33, 34, 35, 36, 37, 38, 39,40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 46, 47, 48, 49, 33, 34, 35, 36, 37, 38, 39,40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 46, 47, 48, 49, 33, 34, 35, 36, 37, 38, 39,40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 46, 47, 48, 49, 33, 34, 35, 36, 37, 38, 39,40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 46, 47, 48, 49, 33, 34, 35, 36, 37, 38, 39,40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 101]


verify(targetNumber, 101)
