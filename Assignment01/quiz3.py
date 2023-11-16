'''
input 
calculate leg/total leg
method
output
'''
num_zrogs = int(input("Enter number of zrog: "))
num_zmus = int(input("Enter number of zmu: "))
num_zharks = int(input("Enter number of zhark: "))

legs_per_zrog = 2
legs_per_zmu = 5
legs_per_zhark = 10

total_legs = (num_zrogs * legs_per_zrog) + (num_zmus * legs_per_zmu) + (num_zharks * legs_per_zhark)

print("\nLeg calculation")
print(f"Zrog legs = {num_zrogs} x {legs_per_zrog} = {num_zrogs * legs_per_zrog}")
print(f"Zmu legs = {num_zmus} x {legs_per_zmu} = {num_zmus * legs_per_zmu}")
print(f"Zhark legs = {num_zharks} x {legs_per_zhark} = {num_zharks * legs_per_zhark}")
print(f"Total legs = {num_zrogs * legs_per_zrog} + {num_zmus * legs_per_zmu} + {num_zharks * legs_per_zhark} = {total_legs}")
