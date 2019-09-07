import csv
import os

#udemy_csv = "./Resources/web_starter.csv"
udemy_csv = os.path.join(".", "Resources", "web_starter.csv")
#The OS PATH is safer

#We want the title, the price, the suscribers
#Reviews, percent of review, length
title = []
price = []
subscribers = []
reviews = []
reviews_percent = []
length = []




with open(udemy_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # To iterate each row of the file
    for row in csvreader: 
        # add title
        title.append(row[1])

        price.append(row[4])
        #add subscribers
        subscribers.append(row[5])
        #reviews
        reviews.append(row[6])
        #percent of reviews
        percent = round(int(row[6]) / int(row[5]), 2)
        reviews_percent.append(percent)
        #length
        new_length = row[9].split(" ")
        length.append(float(new_length[0]))

#print(length)

cleanCsv = zip (title, price, subscribers, reviews, reviews_percent, length)

outputFile = os.path.join("webFinal.csv")

with open(outputFile, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews", "Percent of Reviews", "Length of Course"])
    writer.writerows(cleanCsv)
    #test = next(csvreader)

    #print(test)





