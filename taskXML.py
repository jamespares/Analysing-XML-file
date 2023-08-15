import xml.etree.ElementTree as ET

tree = ET.parse('movie.xml')
root = tree.getroot()

favorite_count = 0
non_favorite_count = 0

for movie in root.iter("movie"):

    # Check if the movie is a favorite
    if movie.attrib.get("favorite") == "True":
        favorite_count += 1
    else:
        non_favorite_count += 1

    # Print movie title
    print(f"Movie: {movie.attrib['title']}")

    # Iterate through child tags of the movie element and print them
    for child in movie:
        print(child.tag + ":", ''.join(child.itertext()).strip())
    print('------')

print(f"Number of favorite movies: {favorite_count}")
print(f"Number of non-favorite movies: {non_favorite_count}")
