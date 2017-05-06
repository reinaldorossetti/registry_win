import re
# a brincadeira eh formatar os numeros seguindo a ordem abaixo, dos ultimos valores.
#s = "004-448-555-583-61" # - > 14 number - mod=2
#s = "022-198-53-24" # - > 10 number - mod=1
s = "555 /- @372 $- 654" # -> 9 number - mod=0

result = ''.join(re.findall(r'\d+', s))
list_numbers = [int(i) for i in result]
total_number = len(list_numbers)
mod = total_number%3
value, y = "", 0
decremento=total_number

for x in list_numbers:
    y=y+1
    decremento=decremento-1
    if (mod==0 or mod==2) and y%3==0 and y<total_number:
        value=value+str(x)+"-"
    elif mod==1 and y%3==0 and y<total_number and decremento>=4:
        value=value+str(x)+"-"
    elif mod==1 and decremento<4 and decremento%2==0 and y<total_number:
        value=value+str(x)+"-"
    else:
        value=value+str(x)

print(value)
