import csv

if __name__=="__main__":
    csv_file=open("apple.csv","w")

    cw=csv.writer(csv_file,delimiter=',',quotechar='|')
    rows=[["사과",30000,3000,50000],
        ["오렌지",80000,2000,10000],
        ["바나나",20000,6000,55000]]

    cw.writerows(rows)
    csv_file.close()

with open('apple.csv','r') as f:
    reader=csv.reader(f,quotechar='|')
    for row in reader:
        if','.join(row).strip()=="":
            continue
        hap=int(row[1])+int(row[2])+int(row[3])
        print("%s: %d"%(row[0],hap))
