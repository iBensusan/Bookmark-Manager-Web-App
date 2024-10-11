# Bookmark Manager Web App

## Description

This project is a Bookmark Manager Web App developed using **Django** for the back-end and **Bootstrap** for the front-end styling. The main function of the app is to allow users to add, view, and delete website bookmarks.

## Features

- Add new bookmarks (title and URL).
- View a list of saved bookmarks.
- Delete bookmarks from the list.
- Responsive and clean design using Bootstrap.

## Project Structure

The project follows a typical Django structure with a main app called `bookmarks` that handles all bookmark-related functionality.

- **Backend**:
  - `bookmarks/models.py`: Defines the `Bookmark` model, which stores the title and URL of each bookmark.
  - `bookmarks/views.py`: Manages the logic for displaying, adding, and deleting bookmarks.
  - `bookmarks/urls.py`: Maps URLs to the appropriate views.
  
- **Frontend**:
  - `bookmarks/templates/bookmarks/bookmark_list.html`: The HTML file that uses **Bootstrap** to display the user interface, such as forms and lists.

## Development

### 1. **Django Backend**:
The backend is powered by Django. A simple `Bookmark` model is used to store the title and URL of each bookmark. The model looks like this:

### 2. **Bootstrap Frontend**:

The user interface is styled using **Bootstrap**, a popular CSS framework. This helps provide a clean and responsive design without the need for custom CSS. The main Bootstrap components used include:

- **Form Controls**: The form fields (title and URL) are styled using Bootstrap's `form-control` class for a consistent appearance.
- **Buttons**: Buttons for adding and deleting bookmarks are styled using the `btn` and `btn-primary` (for adding) and `btn-danger` (for deleting) classes.
- **List Group**: The saved bookmarks are displayed in a styled list using Bootstrap's `list-group` and `list-group-item` classes to ensure a clean, organized layout.

### 3. **How It Works**:

- Users can add a new bookmark by entering a title and URL and clicking the **Add Bookmark** button.
- The saved bookmarks are displayed as a list below the form, where each bookmark is a clickable link that opens in a new tab.
- Each bookmark has a **Delete** button that allows users to remove it from the list.

## How to Run the Project

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run migrations to set up the database: `python manage.py migrate`.
4. Start the development server: `python manage.py runserver`.
5. Open the app in your browser at `http://127.0.0.1:8000/`.
