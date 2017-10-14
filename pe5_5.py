def gemiddelde(zin):
    text = zin.split(" ")
    som = 0

    for x in range(len(text)):
        som = som + len(text[x])
    gem = som / len(text)
    print("De gemiddelde lengte van de woorden in deze zin is:", gem)


gemiddelde(input("Voer een zin in: "))
