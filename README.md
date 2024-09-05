# Simple Task Manager

A simple command-line task manager built with Python. Manage your tasks by adding, deleting, updating, and changing their status. Tasks are stored in a JSON file (`lista.json`).

## Features

- **Add** a new task
- **Delete** an existing task
- **Update** the title of a task
- **Mark** a task as in-progress or done
- **List** tasks based on their status

## Requirements

- Python 3.x

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/diegarlin/task-tracker-cli
    cd your-repo
    ```

2. **Install the package:**

    ```bash
    pip install .
    ```

    This will install the package and its dependencies as specified in `setup.py`.

## Usage

You can use the `task-cli` command to interact with the task manager.

### Commands

#### Add a New Task

Add a task with a title.

```bash
task-cli add "Task Title"
```

**Example:**

```bash
task-cli add "Buy groceries"
```

#### Delete a Task

Delete a task by its ID.

```bash
task-cli delete <id>
```

**Example:**

```bash
task-cli delete 1
```

#### Update a Task Title

Update the title of an existing task by its ID.

```bash
task-cli update <id> -t "New Task Title"
```

**Example:**

```bash
task-cli update 1 -t "Buy groceries and cook dinner"
```

#### Mark a Task as In-Progress

Mark a task as in-progress by its ID.

```bash
task-cli mark-in-progress <id>
```

**Example:**

```bash
task-cli mark-in-progress 1
```

#### Mark a Task as Done

Mark a task as done by its ID.

```bash
task-cli mark-done <id>
```

**Example:**

```bash
task-cli mark-done 1
```

#### List Tasks

List tasks based on their status. You can list all tasks or filter by status.

```bash
task-cli list [all|done|in-progress|todo]
```

**Examples:**

- List all tasks:

    ```bash
    task-cli list
    ```

- List done tasks:

    ```bash
    task-cli list done
    ```

- List in-progress tasks:

    ```bash
    task-cli list in-progress
    ```

- List todo tasks:

    ```bash
    task-cli list todo
    ```

## Data Storage

Tasks are stored in a `lista.json` file in the following format:

```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "05/09/2024, 12:34:56",
    "updatedAt": null
  },
  {
    "id": 2,
    "description": "Complete assignment",
    "status": "in-progress",
    "createdAt": "05/09/2024, 13:00:00",
    "updatedAt": "05/09/2024, 14:00:00"
  }
]
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For any questions or suggestions, feel free to contact [garcialinaresdiego@gmail.com](mailto:garcialinaresdiego@gmail.com).