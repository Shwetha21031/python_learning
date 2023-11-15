# comma seperated values
# used to store tabular data in spreadsheet or database
# each line of file = record
# each record has fields seperated by comma (delimiter)
# csv are PT format makes easy for web dev to create
# easy to import


# operations
# reading - csv file , csv file as dictionary , csv file as pandas
# writing - csv file , csv file as dictionary , csv file as pandas

# standard lib so no need to install it
import csv

# read to a file

with open('color_srgb.csv','r') as csv_file:
    # var = csv.reader method(file)
    # to read the file, which returns an iterable reader object. 
    csv_reader = csv.reader(csv_file)
    # iterate through files line by line
    # for i in csv_reader:
    #     print(i)

# write to a file

l = [['Navy','#000080',"rgb(0,0,50)"],['Fuchsia','#FF00FF',"rgb(100,0,100)"]]
with open('color_srgb.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('color_srgb.csv','a') as new_file:
        csv_writer = csv.writer(new_file,delimiter=',')
        # for i in l:
        #     csv_writer.writerow(i)


# ordered dictionary reading
with open('color_srgb.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # for i in csv_reader:
        # print(i)

# writing to a file using dictionaries
mydict = [{'Name': 'Purple','HEX':'#800080','RGB':"rgb(50,0,50)"},
        {'Name': 'White','HEX':'#FFFFFF','RGB':"rgb(100,100,100)"},]
fields = ['Name','HEX','RGB']
filename = 'color_rgb.csv'

with open(filename,'w') as file:
    writer = csv.DictWriter(file,fieldnames=fields,delimiter=';')
    writer.writeheader()
    writer.writerows(mydict)



# writerow(): This method writes a single row at a time. Field row can be written using this method.

# writerows(): This method is used to write multiple rows at a time. This can be used to write rows list