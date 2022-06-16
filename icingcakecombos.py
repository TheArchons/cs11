icing = ["Chocolate", "Vanilla", "Cream Cheese", "no"]
cake = ["Red Velvet", "Confetti", "White", "Lemon"]
fruit = ["Blueberries", "Bananas", "Kiwi", "Peaches"]

#complete the program below so that it prints out all the possible combinations of icing, cake and fruit
for i in icing:
    for j in cake:
        for k in fruit:
            print("{} icing, {} cake, {} fruit".format(i, j, k))