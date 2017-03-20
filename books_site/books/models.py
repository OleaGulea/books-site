from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name='books')
    cover = models.ImageField(null=True, blank=True)
    description = models.TextField()
    price = models.FloatField(default=0)

    def __str__(self):
        return '%s' % self.title


class Chapter(models.Model):
    book = models.ForeignKey(Book, related_name='chapters')
    title = models.CharField(max_length=200, blank=True)
    text = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField()

    def __str__(self):
        return '%s %s %s' % (self.book.title, self.order, self.title)



