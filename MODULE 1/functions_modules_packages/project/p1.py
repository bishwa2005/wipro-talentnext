def sort_colors(colors):
    color_list = colors.split("-")
    color_list.sort()
    return "-".join(color_list)


colors = input("Enter colors separated by hyphen: ")

result = sort_colors(colors)

print(result)