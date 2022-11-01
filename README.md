#Homework

##Django. Session

Main task:
>Сделать вьюшку с использованием хранилища сессии

All details:[HERE](https://lms.ithillel.ua/groups/62de6dfc9aec6f42f8454737/homeworks/634a134058914414b57dfd71)

Make all actions needed for run homework from zero `make homework-i-run`

```
$ make homework-i-run
```

Delete all created artifacts from run `make homework-i-purge`

```
$ make homework-i-purge
```

Main routes:

+ **/session** - view sessions


.PHONY: init-dev
# Init environment for development
init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements.txt && \
	pre-commit install


