import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    infile = sys.argv[1]
    outfile = sys.argv[2]

    try:
        with open(infile, "r") as file:
            reader = csv.DictReader(file) 
            students = []
            for row in reader:
                last, first = row["name"].split(",")
                students.append({
                    "first": first.strip(),
                    "last": last.strip(),
                    "house": row["house"].strip()
                })
    except FileNotFoundError:
        sys.exit(f"Could not read {infile}")

    with open(outfile, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)

if __name__ == "__main__":
    main()