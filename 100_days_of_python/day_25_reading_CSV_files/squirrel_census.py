import pandas 
data = pandas.read_csv("day_25_reading_CSV_files/Squirrel_Data.csv")
gray = 0
black =0
cinnamon = 0


for color in data['Main Color']:
    if color == "Gray":
        gray += 1
    if color == "Black":
        black +=1
    if color == "Cinnamon":
        cinnamon +=1
color_dictionary = {
   "fur color": ["Gray","Black","Cinnamon"],
   "count":[gray, black, cinnamon]
}
    
color_csv = pandas.DataFrame(color_dictionary)
color_csv.to_csv("day_25_reading_CSV_files/color_csv")

print(data['Main Color'])