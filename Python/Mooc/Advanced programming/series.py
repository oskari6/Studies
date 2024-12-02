class Series:
    def __init__(self, title, seasons, genres):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def __str__(self):
        if self.ratings:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genres)}\n{len(self.ratings)} ratings, average {sum(self.ratings) / len(self.ratings):.1f} points"
        return f"{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genres)}\nno ratings"

    def rate(self, rating):
        if rating >= 0 and rating <= 5:
            self.ratings.append(rating)
    
def minimum_grade(rating: float, series_list: list):
    wanted = []
    for series in series_list:
        if sum(series.ratings) / len(series.ratings) >= rating:
            wanted.append(series)
    return wanted

def includes_genre(genre: str, series_list: list):
    wanted = []
    for series in series_list:
        if genre in series.genres:
            wanted.append(series)
    return wanted

if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)