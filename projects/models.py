import peewee
import peewee_async

database = peewee_async.PostgresqlDatabase('async-lab',
                                           user='async-lab',
                                           password='async-lab',
                                           host='postgres')


class Project(peewee.Model):
    """A project model

    Attributes:
        title (str): Title of project
    """
    title: str = peewee.CharField()

    class Meta:
        database = database
