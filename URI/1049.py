animals = [input(), input(), input()]
animal = [animals == ["vertebrado", "ave", "carnivoro"], animals == ["vertebrado", "ave", "onivoro"],
          animals == ["vertebrado", "mamifero", "onivoro"], animals == ["vertebrado", "mamifero", "herbivoro"],
          animals == ["invertebrado", "inseto", "hematofago"], animals == ["invertebrado", "inseto", "herbivoro"],
          animals == ["invertebrado", "anelideo", "hematofago"], animals == ["invertebrado", "anelideo", "onivoro"]]
family = ["aguia", "pomba", "homem", "vaca", "pulga", "lagarta", "sanguessuga", "minhoca"]
print(family[animal.index(True)])