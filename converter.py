def km_to_m(km):
    return km * 1000

def tonn_to_kg(tonn):
    return tonn * 1000

def cels_to_fars(cels):
    return (cels * 9/5) + 32

def convert_from_file():
    try:
        with open("batch_input.txt", 'r', encoding = 'utf-8') as f:
            values = [float(line.strip()) for line in f if line.strip()]

        for val in values:
            print(f"{val} km = {km_to_m(val)}")
    except:
        print("error")

print(f"10 km = {km_to_m(10)}")
print(f"10 tonn = {tonn_to_kg(10)}")
print(f"10 cels = {cels_to_fars(10)}")
convert_from_file()

ROUND_DIGITS = 2
