#Context Manager

## Creating Custom Context Managers

To create a custom context manager we just need to implement the `__enter__` and `__exit__` methods.

### SQLite Example
```Python
import sqlite3


class SQLiteConn:
    """"""

    def __init__(self, db_name):
        """Constructor"""
        self.db_name = db_name

    def __enter__(self):
        """
        Open the database connection
        """
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the connection
        """
        self.conn.close()
        if exc_val:
            raise


if __name__ == "__main__":
    db = "test.db"
    # Now we can access it with a with statement
    with SQLite(db) as conn:
        cursor = conn.cursor()
```

## ExitStack and Reentrant
ExitStack maintains a stack of registered callbacks taht will call in reverse order to close a series of contexts automatically. 
```Python
from contextlib import ExitStack

filenames = []
with ExitStack() as stack:
    file_objects = [stack.enter_context(open(filename))
        for filename in filenames]
```

Reentrant allows us to use a context more than once. 

This will produce an error: 

```Python
from contextlib import contextmanager

@contextmanager
def single():
    print("Hello")
    yield
    print("Exiting context manager")

context = single()
with context:
    pass

with context:
    pass
```
This will not: 

```Python
from contextlib import redirect_stdout
from io import StringIO

stream = StringIO()
write_to_stream = redirect_stdout(stream)
with write_to_stream:
    print("Write something to the stream")
    with write_to_stream:
        print("Write something else to stream")

print(stream.getvalue())
```