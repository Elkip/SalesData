import matplotlib.pyplot as plt
import datetime
import csv


def sales_30_days(filename):
    x = []
    y = []
    y_bySeg = {}
    
    date_format = "%m/%d/%Y"
    with open(filename, "r") as csvfile:
        plots = csv.reader(csvfile, delimiter=",")
        header_row = next(plots)
        print(header_row)
        for row in plots:
            if row[0] == '':
                break
            print(row)
            x.append(datetime.datetime.strptime(row[0], date_format))
            seg = row[1]    # department
            money = row[2]  # transaction amount
            
            # new segment
            if seg not in y_bySeg:
                y_bySeg[seg] = 0
            
            # check if negative
            if money[0] == '(':
                amount = 0-float(row[2].replace(',', '')[1:-1])
                y.append(amount)
                y_bySeg[seg] += amount
            else:
                y.append(float(row[2].replace(',', '')))
                y_bySeg[seg] += amount
    # Line Graph            
    plt.plot(x, y, label="Sales")
    plt.xlabel(header_row[0])
    plt.ylabel(header_row[2])
    plt.title('Sales in the last 30 days')
    plt.legend()
    plt.show()
    # Pie Chart
    val = []
    for v in y_bySeg.values():
        val.append(abs(v))
    print(y_bySeg)
    plt.pie(val, labels=[k for k in y_bySeg.keys()], autopct=None)
    plt.show()


sales_30_days("sales.csv")
