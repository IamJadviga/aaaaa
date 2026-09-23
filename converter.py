def km_to_m(km):
    return km * 1000


def tonn_to_kg(tonn):
    return tonn * 1000

def cels_to_fars(cels):
    return (cels * 9/5) + 32

if __name__ == "_main_":
    print(f"10 km = {km_to_m(10)}")
    print(f"10 tonn = {tonn_to_kg(10)}")
    print(f"10 cels = {cels_to_fars(10)}")
