import mean
import median
import range
import standard_deviation
import math

def main():
    x = []
    print("Input x anytime to stop")
    while True:
        temp = input("Next Value: ")
        if temp == "x":
            break

        else:
            x.append(float(temp))

    result = standard_deviation.get(x)
    print("\nResults\nVariance = ", result)
    print("Standard Deviation = ", math.sqrt(result))



if __name__ == "__main__":
    main()

