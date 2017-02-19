import peewee
import peewee_async

database = peewee_async.PostgresqlDatabase(
    'postgres://async-lab@postgres/async-lab?password=async-lab'
)


class Project(peewee.Model):
    """A project model

    Attributes:
        title (str): Title of project
    """
    title: str = peewee.CharField()

    class Meta:
        database = database
