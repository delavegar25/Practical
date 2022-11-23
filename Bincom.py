from random import randint

def find_mean_color(colors):
    pass

def mode_color(colors):
    maxCount = 0
    maxColor = ''
    
    for color in colors:
        count = len([c for c in colors if c == color])
        
        if count > maxCount:
            maxColor = color
            maxCount = count
            
        return maxColor
    
def median_color(colors):
    N = len(colors)
    
    mid = N//2
    
    if N % 2 == 0:
        return(colors[mid] + colors[mid+1])/2
    
    return colors[mid]

def find_red_probability(colors):
    return len([c for c in colors if c == 'red']) / len(colors)

def find_number(numbers, target):
    if target == numbers[0]:
        return True
    
    return find_number(numbers[1:], target)

def gen_rand_binary():
    digits = ''
    for i in range(4):
        digits += randint(0, 1)
    return int(digits, base=2)


def sum_fib(n=50):
    if n <= 2:
        return 1
    return sum_fib(n-1) + sum_fib(n-2)