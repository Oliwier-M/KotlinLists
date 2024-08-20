def yet_the_largest(list_num):

    if not isinstance(list_num, list):
        raise TypeError("Must be a list")

    if list_num == []:
        return []

    result = [list_num[0]]

    for x in list_num[1:]:  # [x:y] checks from index x to index y, if y not included - checks till the end
        if x > result[-1]:
            result.append(x)

    return result
