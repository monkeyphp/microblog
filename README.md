# microblog
the-flask-mega-tutorial from blog.miguelgrinberg.com

Part 1: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

```bash
$ source venv/bin/activate
```

```bash
(venv) $ export FLASK_APP=microblog.py
```

```bash
(venv) $ export FLASK_DEBUG=1
```

```bash
(venv) $ deactivate
```

To run the Python debugging mail server...

```bash
(venv) $ python -m smtpd -n -c DebuggingServer localhost:8025
```
