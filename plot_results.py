import argparse
import csv
import matplotlib.pyplot as plt


def read_csv(file):
    x, y = [], []
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            x.append(row[0])
            y.append(row[1])
    return [float(i) for i in x[1:]], [float(i) for i in y[1:]]


if __name__ == '__main__':

    prs = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                    description="""TCP Server""")                   
    prs.add_argument("-f", dest="files", nargs='+', type=str, required=True, help="CSV files.\n")
    args = prs.parse_args()

    plt.figure()
    for csv_file in args.files:
        x, y = read_csv(csv_file)
        plt.plot(x, y, label=csv_file)
        plt.title('TCP Fairness')
        plt.xlabel('time (seconds)')
        plt.ylabel('traffic (bits/seconds)')
        plt.grid(True)
        plt.legend()
    plt.show()

    
    
