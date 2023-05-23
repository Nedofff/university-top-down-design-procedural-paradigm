from random import randint

# Агенство советует выбрать countTips мест с различным комфортом
def get_travel_agency_tips(countTips):
    map_places = ["Istanbul", "Ankara", "Sochi", "Gelendzhik", "Denpasar", "Paris"]
    degree_of_comfort = [1, 2, 3, 4, 5]

    all_tips = []
    for n in range(int(countTips)):
        all_tips.append(
            [
                map_places[randint(0, len(map_places) - 1)],
                degree_of_comfort[randint(0, len(degree_of_comfort) - 1)],
            ]
        )

    return all_tips


# Турист выбирает место с максимальным комфортом
def get_tourist_choice(tips):
    tourist_choice = tips[0]
    for tip in tips[1:]:
        if tourist_choice[1] < tip[1]:
            tourist_choice = tip

    return tourist_choice


def main():
    travel_agency_tips = get_travel_agency_tips(10)
    print(get_tourist_choice(travel_agency_tips))


if __name__ == "__main__":
    main()
