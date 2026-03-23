import pandas

# store csv in a variable called data
data = pandas.read_csv("squirrel data/squirrel_data.csv")

# calculate total number of rows that contain each color key word
num_gray = len(data[data["Primary Fur Color"] == "Gray"])
num_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
num_black = len(data[data["Primary Fur Color"] == "Black"])

# create a dictionary to store color data
colors_dict = {
    "Fur Colors": ["Gray", "Cinnamon", "Black"],
    "Count": [num_gray, num_cinnamon, num_black]
}

# convert data to a csv
colors_data = pandas.DataFrame(colors_dict)
colors_data.to_csv("squirrel_colors.csv")