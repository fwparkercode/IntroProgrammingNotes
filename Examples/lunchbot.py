#!/usr/bin/python3.7


import PyPDF2
import requests
from pathlib import Path

'''
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
print(THIS_FOLDER)
filename = os.path.join(THIS_FOLDER, 'lunch.pdf')
'''

url = "https://fwparker.myschoolapp.com/ftpimages/1048/download/download_3652074.pdf?_=1573492018660"
response = requests.get(url)

lunch_file = Path('/home/sciencelee/fwp_menu/lunch.pdf')
lunch_file.write_bytes(response.content)
print(url)


# creating a pdf reader object
file_object = open(lunch_file, 'rb')

# creating a page object
reader = PyPDF2.PdfFileReader(file_object)
page_object = reader.getPage(0)

# grab the text from the page object
menu_text = page_object.extractText()


# make a list to dump the menus in
menu_list = []
done = False

i = 0
while i < (len(menu_text) - 1):
    if menu_text[i] == "\n":
        menu_text = menu_text[0:i] + menu_text[i + 1:]
        i = 0
        print("cut")
    i += 1



# loop through and add the extracted text to the menu list
while not done:
    try:
        menu_text.index("\n")
    except:
        done = True
        break  # if there are no more lines, we out!
    line = menu_text[:(menu_text.index("\n"))]  # read up to the line break
    menu_text = menu_text[menu_text.index("\n") + 1:]  # make the text everything after the break
    #print(menu_text)
    menu_list.append(line.strip())  # throw it in the list

print(menu_list)

'''
# We decided to make a list for each day because of the weird formatting of the pdf
monday_list = []
tuesday_list = []
wednesday_list = []
thursday_list = []
friday_list = []


# we look for the day in the menu list, and use that to mark an index for that day.

for i in range(len(menu_list)):
    if "tuesd" in menu_list[i].lower() or "uesday" in menu_list[i].lower():
        tuesday_index = i
        break

for i in range(len(menu_list)):
    if "wedne" in menu_list[i].lower() or "ednesday" in menu_list[i].lower():
        wednesday_index = i
        break

for i in range(len(menu_list)):
    if "thursd" in menu_list[i].lower() or "hursda" in menu_list[i].lower():
        thursday_index = i
        break

for i in range(len(menu_list)):
    if "frida" in menu_list[i].lower() or "riday" in menu_list[i].lower():
        friday_index = i
        break

final_index = len(menu_list)  # make it end of doc unless we see second page
for i in range(len(menu_list)):
    if "second" in menu_list[i].lower():
        #  "second" is sometimes at the top of page 2 for some weeks.  Not sure the reason
        final_index = i
        break
'''

print(menu_list)

#print("indices are", tuesday_index, wednesday_index, thursday_index, friday_index, final_index)

# now we use the indices to get each of the days
#monday_list.append(menu_list[2:tuesday_index])
#tuesday_list.append(menu_list[tuesday_index:wednesday_index])
#wednesday_list.append(menu_list[wednesday_index:thursday_index])
#thursday_list.append(menu_list[thursday_index:friday_index])
#friday_list.append(menu_list[friday_index:final_index])


# closing the pdf file object
#pdfFileObj.close()

# just doing this beacuse it is inside two lists.  Not sure why.  Part of extraction.
monday_list = monday_list[0]
tuesday_list = tuesday_list[0]
wednesday_list = wednesday_list[0]
thursday_list = thursday_list[0]
friday_list = friday_list[0]

# got some extra artifacts on page 1 before monday.  Cycle through til we hit monday, then commit the list.
for i in range(len(monday_list)):
    if "mon" in monday_list[i].lower():
        monday_list = monday_list[i:]
        break


# write all the lists as a single piece of text suitable for SMS
monday = (" ".join(monday_list)) + "."
tuesday = (" ".join(tuesday_list)) + "."
wednesday = (" ".join(wednesday_list)) + "."
thursday = (" ".join(thursday_list)) + "."
friday = (" ".join(friday_list)) + "."


print()
print(monday)
print()
print(tuesday)
print()
print(wednesday)
print()
print(thursday)
print()
print(friday)



f = open("/home/sciencelee/mysite/menu.py", "w")

# make a single 2d list to write to my_menu
day_list = [monday, tuesday, wednesday, thursday, friday]

f.write("my_menu = " + str(day_list))
f.close()

# END OF PROGRAM
