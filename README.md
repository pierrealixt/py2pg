# py2pg


- [ ] Write your Python functions in your favorite IDE.
- [ ] Tests them with your favorite testing library.
- [ ] Deploy them to your Postgres server.

It should be a command-line app:
```bash
py2pg --help
```

It should deploy a function to a database
```bash
py2pg deploy py_function_file --database='fbf-production'
```

It should have a config file to add database
```json
DATABASES = {
    'fbf-production': {
        'USER', 'PASS', 'HOST', 'DB', 'PORT'
    }
}
```

It should have one file per function (py_function_file)
```py

def answer_of_life(guess):
    assert guess == 42

class Test(unittest.TestCase):
    def test_yes(self):
        self.assertTrue(answer_of_life(42))

    def test_no(self):
        self.assertTrue(answer_of_life(26))


config = {
    'imports': {
        ''
    }
    'arguments': {
        'guess': {
            'type': 'integer'
        }
    },
    'return': {
        'type': 'boolean'
    }
}
```

It should transpile a python function into plpython function

```bash
py2pg transpile py_function_file
```

```sql
CREATE OR REPLACE FUNCTION answer_of_life(gues INTEGER)
RETURNS BOOLEAN
AS $$
import sys
sys.path.insert(0, '/var/lib/postgresql/.local/lib/python3.7/site-packages/')

return assert guess == 42

$$ LANGUAGE plpython3u;
```

It should be able to call another plpython function
```python
def foo(bar):
  return bar
```


```python
from py2pg import call_func

def hello(world):
    call_func('foo', 'bar')
```
=>
```sql
CREATE OR REPLACE FUNCTION hello(world VARCHAR)
RETURNS BOOLEAN
AS $$
import sys
sys.path.insert(0, '/var/lib/postgresql/.local/lib/python3.7/site-packages/')

plpy.execute("select * from foo('bar')")


$$ LANGUAGE plpython3u;
```