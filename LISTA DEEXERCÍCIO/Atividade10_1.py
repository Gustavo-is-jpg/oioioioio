qual = input('Digite C ou F:')

if qual == 'c' or qual == 'C':
    f = float(input('Digite a temperatura em °F\t'))
    c = ((f - 32) / 1.8)
    print(f'a temperatura em Celsius é °{c}')

elif qual == 'f' or qual == 'F':
    c = float(input('Digite a temperatura em °C\t'))
    f = ((1.8* c) + 32)
    print(f'a temperatura em Fahrenheit é °{f}')