import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--barbie', type=int, default=50)
    parser.add_argument('--cars', type=int, default=50)
    parser.add_argument('--movie', default='other')
    args = parser.parse_args()

    barbie = args.barbie if 0 <= args.barbie <= 100 else 50
    cars = args.cars if 0 <= args.cars <= 100 else 50

    movie = args.movie.lower()
    movie_value = 50
    if movie == 'melodrama':
        movie_value = 0
    elif movie == 'football':
        movie_value = 100

    boy = int((100 - barbie + cars + movie_value) / 3)
    girl = 100 - boy

    print(f"boy: {boy}\ngirl: {girl}")


if __name__ == "__main__":
    main()
