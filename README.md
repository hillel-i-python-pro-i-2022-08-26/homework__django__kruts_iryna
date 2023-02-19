#Homework

##DRF. Contacts and CRUD. 

Main task:
>Сделать CRUD для контактов, используя DRF. 

All details:[HERE](https://lms.ithillel.ua/groups/62de6dfc9aec6f42f8454737/homeworks/63debfc24671ad3a74b89fdc)

Make all actions needed for run homework from zero `d-make homework-i-run`

```
$ make d-homework-i-run
```

Delete all created artifacts from run `make d-homework-i-purge`

```
$ d-make homework-i-purge
```


Main routes:

+ **/api/v1/contacts_list/** - _Show all contacts_
+ **/api/v1/contacts/<int:pk>/** _Edit by id_
+ **/api/v1/contacts_delete/<int:pk>/** _Delete by id_




