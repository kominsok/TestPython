import csv
import codecs

class CustomFormat(csv.excel):
    quoting=csv.QUOTE_ALL
    #delimeter=''

if __name__=="__main__":
    csvFile=codecs.open("ch14.csv","w","shift_jis")
    writer=csv.writer(csvFile,CustomFormat())

    row=("python","-","ver.","1")
    writer.writerow(row)

    rows=[]
    rows.append(("python","-","ver.","2"))
    rows.append(("python","-","ver.","3"))
    rows.append(("python","-","ver.","4"))
    writer.writerows(rows)
    csvFile.close()
