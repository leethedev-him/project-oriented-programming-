'''

F = (C * 9/5) + 32
C = (F - 32) * 5/9

30c => 86f


'''
def to_Fheit(celcius):
    result = celcius * (9/5) + 32
    return (int(result) if result.is_integer() else round(result, 2))


def to_Celcius(fheit):
    result = (fheit - 32) * 5/9
    return (int(result) if result.is_integer() else round(result, 2))


def main():
    while True:
        try:
            temper = input("Enter the temperature value you want to convert: ").strip()

            temp = float(temper)

            dest = input("Enter the temperature you want to convert to. \n'c' for Celcius, 'f' for Fahrenheit: ").strip().lower()

            

            if (dest != 'c'  and dest != "f") or len(dest) != 1:
                raise ValueError("Enter either 'f' or 'c' as temperature destination")
            
            if dest == 'c':
                result = to_Celcius(temp)
                sign = '℃'
                deste = "Celcius"
            else:
                result = to_Fheit(temp)
                sign = '℉'
                deste = "Fahrenheit"
                
                

            print(f"{temper} to {deste} is {result}{sign}")
            
            break

        except Exception as e:
            print(f"{e} Please try again\n")

if __name__ == "__main__":
    while True:
        main()
        repeat = input("Do you want to run the program again?  y to continue, anything else to quit: ").strip().lower()
        if repeat != "y":
            break
