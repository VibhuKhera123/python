import csv


def main():
 
    data = [('William Smith', 34, 'Toronto'), ('Jane Blake', 25, 'Las Vegas')]

    with open("data.csv", "w") as f:
        writer = csv.writer(f)
        
        writer.writerows(data)
        
    with open("data.csv", "r") as f:
            reader = csv.reader(f)
            headers = next(reader)

            print("Headers:", headers)

            for row in reader:
                print("Row:", row)


if __name__ == "__main__":
    main()



