
def is_in_list_iter(x, T):



  # for pos in range(len(T)):
  #   if T[pos] == x:
  #     return True
  # return False

T = [-2, 1, 1.0, 3, 8]
print(is_in_list_iter(0, T))
print(is_in_list_iter(3, T))
print(is_in_list_iter(-2, T))
print(is_in_list_iter(8, T))
print(is_in_list_iter(1, T))
print(is_in_list_iter(T, []))



def sum_in_list_iter(T, pos=0):
    if pos == len(T):
        return 0
    return T[pos] + sum_in_list_iter(T, pos+1)

print(sum_in_list_iter([1,2,3,4]))
print(sum_in_list_iter([100]))
print(sum_in_list_iter([]))
