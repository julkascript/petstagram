from django.db import models


class Pet(models.Model):
    DOG, CAT, PARROT = "dog", "cat", "parrot"
    animals = (
        (DOG, 'dog'),
        (CAT, 'cat'),
        (PARROT, 'parrot'),
    )
    type = models.CharField(max_length=6, choices=animals)
    name = models.CharField(max_length=6)
    age = models.PositiveIntegerField()
    description = models.TextField()
    image_url = models.ImageField(upload_to='images')


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.comment}"
