from django.db import models


# Create your models here.
class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True)
    zipcode = models.IntegerField(null=True)
    tel_no = models.CharField(max_length=100, null=True)
    recommend_by = models.ForeignKey(
        "Author",
        on_delete=models.CASCADE,
        related_name="recommend_author",
        related_query_name="recommend_author",
        null=True
    )
    join_date = models.DateField()
    popularity_score = models.IntegerField()
    followers = models.ManyToManyField(
        "User", related_name="followed_authors", related_query_name="followed_authors"
    )

    def __str__(self):
        return self.firstname + " " + self.lastname


class Books(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=200)
    price = models.IntegerField(null=True)
    published_date = models.DateField()
    author = models.ForeignKey(
        "Author",
        on_delete=models.CASCADE,
        related_name="books",
        related_query_name="books",
    )
    publisher = models.ForeignKey(
        "Publisher",
        on_delete=models.CASCADE,
        related_name="books",
        related_query_name="books",
    )

    def __str__(self):
        return self.title


class Publisher(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    recommendedby = models.ForeignKey("Publisher", on_delete=models.CASCADE, null=True)
    joindate = models.DateField()
    popularity_score = models.IntegerField()

    def __str__(self):
        return self.firstname + " " + self.lastname


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.username


class Skill(models.Model):
    skill = models.CharField(max_length=50)


class Person(models.Model):
    person = models.CharField(max_length=50)
    skill = models.ForeignKey(
        Skill, on_delete=models.CASCADE, related_name="person_skill"
    )