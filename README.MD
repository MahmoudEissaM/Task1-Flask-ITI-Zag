# Flask Company Project

This is a simple Flask web application that displays a list of companies and their details. The application uses an HTML template to render the data in a table format.

## Features

- Displays a list of companies with their name, location, description, and employee count.
- Uses Flask for backend routing and Jinja2 for HTML templating.

## Project Structure

```
flask_company_project/
├── app.py
├── templates/
│   └── company_list.html
└── README.md
```

## Prerequisites

- Python 3.x installed on your system.
- Flask library installed. You can install it using pip:
  ```bash
  pip install flask
  ```

## How to Run the Project

1. Clone the repository or download the project files.
2. Navigate to the project directory:
   ```bash
   cd "/media/mahmoud/New Volume/My CS College/ITI/BackEnd/Flask/flask_company_project"
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Open your web browser and go to `http://127.0.0.1:5000/companies` to view the list of companies.

## File Descriptions

- **app.py**: The main Flask application file that defines the routes and serves the data.
- **templates/company_list.html**: The HTML template used to render the list of companies in a table format.
- **README.md**: This file, which provides an overview of the project and instructions for running it.

## Example Output

When you visit the `/companies` route, you will see a table displaying the following details for each company:

| Company Name | Location         | Description                                | Employees Count |
|--------------|------------------|--------------------------------------------|-----------------|
| TechVision   | Cairo, Egypt     | A leading tech company specialized in AI.  | 120             |
| GreenFarm    | Alexandria, Egypt| Agricultural company focusing on organic. | 85              |

## License

This project is for educational purposes and does not include a specific license.