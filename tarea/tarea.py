class Todo:
    # doctest, statuses, and __init__ omitted

    statuses = {False: 'Incomplete', True: 'Complete'}

    def __init__(self, name, description, points, completed=False):
        self.name = name
        self.description = description
        self.points = points
        self.completed = completed

    def __repr__(self):
        return f"{self.name} ({self.statuses[self.completed]} - {self.points} points): {self.description}"


class TodoList:
    # doctest omitted
    def __init__(self, todos):
        self.todos = todos

    def average_points(self):
        total = 0
        for todo in self.todos:
            total += todo.points
        return total / len(self.todos)

    def completed(self):
        results = []
        for todo in self.todos:
            if todo.completed:
                results.append(todo)
        return results

    def incomplete(self):
        results = []
        for todo in self.todos:
            if not todo.completed:
                results.append(todo)
        return results