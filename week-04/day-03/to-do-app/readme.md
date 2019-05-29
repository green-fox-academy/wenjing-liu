### To-Do app

Write a command-line todo application to easily keep track of your day-to-day
tasks. Implement the following features:

- List tasks
  - A todo task has (at least) a completed state and a description
- Add new task
- Check task
- Remove task

#### List tasks

```
$ python3 todo.py -l

1 - Walk the dog
2 - Buy milk
3 - Do homework
```

#### Add task

```
$ python3 todo.py -a "Feed the monkey"
```

#### Check task

```
$ python3 todo.py -c 2
```

#### Remove task

```
$ python3 todo.py -r 2
```