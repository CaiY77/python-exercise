print ('hello world');

# variables, tricks, functions

someone = "Bob";
print ('hello ' + someone);

phrase = "This is just a long sentence"

print (len(phrase))
print (phrase.index('just'))

number_array = ['one', 'two', 'three', 'four', 'five', 'six']
print(number_array[1:3])

#mutable array
real_numbers = [ 1, 2, 3, 4, 5, 6]
number_array.extend(real_numbers)
print(number_array)

another_one = 7

number_array.append(another_one)
print(number_array)

insert_num = 4.5
real_numbers.insert(4,insert_num)
print (real_numbers)
