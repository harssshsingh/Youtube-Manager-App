# 🎥 YouTube Manager App

A simple command-line application built with **Python** to manage a list of YouTube videos. This project demonstrates basic CRUD (Create, Read, Update, Delete) operations using JSON for data storage.

## 📌 Features

* 📋 View all saved YouTube videos
* ➕ Add a new video
* ✏️ Update an existing video's details
* 🗑️ Delete a video
* 💾 Automatically save data using JSON

## 🛠️ Technologies Used

* Python 3
* JSON
* File Handling

## 📂 Project Structure

```
youtube_manager_app/
│── app.py            # Main application
│── youtube.txt       # Stores video data in JSON format
└── README.md         # Project documentation
```

> **Note:** Although the file is named `youtube.txt`, it stores data in JSON format. You can rename it to `youtube.json` if you prefer.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/youtube-manager-app.git
```

### 2. Navigate to the project folder

```bash
cd youtube-manager-app
```

### 3. Run the application

```bash
python app.py
```

or

```bash
python3 app.py
```

## 📖 Menu Options

```
1. List all YouTube videos
2. Add a YouTube video
3. Update a YouTube video's details
4. Delete a YouTube video
5. Exit
```

## 📁 Data Format

The application stores data in JSON format.

Example:

```json
[
    {
        "name": "Python Tutorial",
        "time": "15:30"
    },
    {
        "name": "Git Basics",
        "time": "12:45"
    }
]
```

## 🎯 Learning Objectives

This project helped practice:

* Python functions
* Lists and dictionaries
* File handling
* JSON serialization and deserialization
* Exception handling
* CRUD operations
* User input handling
* Python `match-case` statement

## 🔮 Future Improvements

* Search videos by name
* Sort videos alphabetically
* Sort videos by duration
* Mark videos as favorites
* Store upload date
* Add categories
* Improve input validation
* Add colored terminal output
* Build a graphical user interface (GUI)

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Harsh Singh**

GitHub: https://github.com/harssshsingh
