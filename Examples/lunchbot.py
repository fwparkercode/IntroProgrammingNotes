import PyPDF2
import requests
from pathlib import Path
import datetime


url = "https://fwparker.myschoolapp.com/ftpimages/1048/download/download_3453838.pdf"
response = requests.get(url)

filename = Path('lunch.pdf')
response = requests.get(url)
filename.write_bytes(response.content)
print(url)



# creating a pdf reader object
file_object = open(filename, 'rb')

# creating a page object
reader = PyPDF2.PdfFileReader(file_object)
page_object = reader.getPage(0)
menu_text = page_object.extractText()
print(menu_text)


menu_list = []
done = False

while not done:
    try:
        menu_text.index("\n")
    except:
        done = True
        break
    line = menu_text[:(menu_text.index("\n"))]
    menu_text = menu_text[menu_text.index("\n") + 1:]
    menu_list.append(line.strip())

print(menu_list)

monday_list = []
tuesday_list = []
wednesday_list = []
thursday_list = []
friday_list = []

#print(menu_list)

for i in range(len(menu_list)):
    if "tues" in menu_list[i].lower():
        tuesday_index = i
        break

for i in range(len(menu_list)):
    if "wedn" in menu_list[i].lower():
        wednesday_index = i
        break

for i in range(len(menu_list)):
    if "thur" in menu_list[i].lower():
        thursday_index = i
        break

for i in range(len(menu_list)):
    if "fri" in menu_list[i].lower():
        friday_index = i
        break

final_index = len(menu_list)  # make it end of doc unless we see second page
for i in range(len(menu_list)):
    if "second" in menu_list[i].lower():
        final_index = i
        break


print("indices are", tuesday_index, wednesday_index, thursday_index, friday_index, final_index)



monday_list.append(menu_list[2:tuesday_index])
tuesday_list.append(menu_list[tuesday_index:wednesday_index])
wednesday_list.append(menu_list[wednesday_index:thursday_index])
thursday_list.append(menu_list[thursday_index:friday_index])
friday_list.append(menu_list[friday_index:final_index])


# closing the pdf file object
#pdfFileObj.close()

monday_list = monday_list[0]
tuesday_list = tuesday_list[0]
wednesday_list = wednesday_list[0]
thursday_list = thursday_list[0]
friday_list = friday_list[0]


monday = (" ".join(monday_list)) + "."
tuesday = (" ".join(tuesday_list)) + "."
wednesday = (" ".join(wednesday_list)) + "."
thursday = (" ".join(thursday_list)) + "."
friday = (" ".join(friday_list)) + "."

weekday = datetime.date.today().strftime("%A")

f = open("menu.py", "w")

day_list = [monday, tuesday, wednesday, thursday, friday]
print("\n\n\nDAYLIST")
print(day_list)

f.write("my_list = " + str(day_list))
f.close()
