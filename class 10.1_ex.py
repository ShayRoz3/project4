def bulls_cows(str1, str2):
    cow = ""
    if sorted(str1) == sorted(str2):
        for i in str1:
            for j in str2:
                if i == j:
                    cow += i
                    cow_count= cow.count(cow)
                    print(cow_count)

bulls_cows("sta", "ats")