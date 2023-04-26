from temperature_converter import temperature_conversion


def main():
    result, unit = temperature_conversion()
    print(f"Temperature is {result: .2f} {unit}")


if __name__ == '__main__':
    main()
