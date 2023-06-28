# Trackify Documentation

Trackify is a student involvement tracking system designed for schools. It allows educators to monitor and manage student participation in various school activities. This README provides an overview of Trackify, its features, and installation instructions.

<img src="https://i.imgur.com/Wmpnp5l.png" alt="Trackify Logo" width="650" height="650">

## Features
- **Student Involvement Tracking**: Trackify enables schools to monitor and record student participation in extracurricular activities, clubs, events, and more.
- **Attendance Management**: Keep track of student attendance in school activities and events.
- **Performance Analytics**: Gain insights into student involvement patterns and identify areas for improvement.
- **Secure Login**: Users can securely log in to Trackify using their username and password. 
- **Teacher Confirmation**: Teachers can review and confirm student involvement records using a unique confirmation code.

## Requirements
- **Operating System**: Trackify is compatible with Windows 10 and 11.
- **Internet Connection**: A stable internet connection is required to access and use Trackify. 

## Installation
To install and run Trackify on your computer, please follow these steps:

1. Download the latest version of Python from the [Microsoft Store](https://www.microsoft.com/store/productId/9NRWMJP3717K)
2. Navigate to the [GitHub repository](https://github.com/xIntensity9/FBLA-22-23/)
3. Download the Trackify source code ZIP package from the latest release.
4. Extract the ZIP package to a desired location on your computer.
5. Ensure that the extracted folder contains all the necessary files as seen in the [GitHub repository](https://github.com/xIntensity9/FBLA-22-23/).
6. Run the `run.bat` file.
7. All necessary packages will be installed.
8. Once the setup is complete, you can start using Trackify to track student involvement in your school.

**Note:**
- It is essential to have a stable internet connection for Trackify to function properly.
- A student would normally login using their last name as the username, followed by their Student ID as the password.
- Teachers have their own sign in, they can use any username and password on creation.
- For testing purposes, the login for student view is Username: **Student**, Password: **123**
- The login for teacher view is Username: **Admin**, Password **123**

## License
Trackify is released under the [MIT License](https://github.com/xIntensity9/FBLA-22-23/blob/main/LICENSE).


---

# Trackify Data Storage

## MongoDB

In the development of Trackify, MongoDB was seamlessly integrated to efficiently store and manage the data related to student involvement in school activities. MongoDB is a popular NoSQL database that offers flexibility and scalability, making it a suitable choice for handling the diverse and evolving nature of the application's data.

The incorporation of MongoDB in Trackify involved several key aspects:

**Data Modeling**: A schema was designed to represent the Event Data, Student Data, and Teacher Data in a structured format. MongoDB's flexible document-based model allowed for the creation of collections to store these data entities, with each document representing an individual record.

**Document Structure**: Each event, student, and teacher record was stored as a document in its respective collection. The document structure followed a JSON-like format, allowing for easy retrieval and manipulation of data. The fields in the document were defined based on the specific data attributes required for each entity, such as event details (name, date, location), student information (name, grade, activities participated), and teacher information (name, subjects taught).

**Indexing**: To optimize data retrieval performance, appropriate indexes were created on fields that were frequently queried, such as student info (id, name, points, etc.), event info, or teacher info. Indexing allows for faster searching and sorting of data, improving the overall efficiency of the application.

# Trackify Functionality

**Register**
At the "Register" function, users can choose whether they want to register as a teacher or a student by selecting a checkbox. The registration process involves filling out input boxes with relevant information. If registering as a student, they provide their name, last name, and grade. If registering as a teacher, they only need to provide a username and password.

**View Requests**
The "View Requests" function allows users to see all incoming event requests made by students. The requests are presented in a treeview format, displaying relevant details. Users have the ability to take action on these requests, including approving all requests, approving a single request, or denying a single request.

**Create Report**
The "Create Report" function generates a window where users can select which report they want to generate. The reports are based on each grade individually and an additional report that combines all grades. The reports utilize the matplotlib library to generate graphs representing the data. Additionally, users can export all the generated graphs to a PDF file, which is stored in the program's directory.

**Prizes**
The "Prizes" function generates a window that determines the prizes for each grade. For each grade, there is one winner with the highest number of points and one winner chosen randomly. The prizes are determined based on the number of points accumulated. The lowest point tier starts at 100 and increases by 50 until reaching a cap of 250. Participants with less than 100 points receive a free snack from the school store.

**View Entries**
The "View Entries" function allows teachers/admins to view all currently registered students in the database. Teachers can edit student information and remove students from the database if necessary.

**Add Event**
The "Add Event" function enables teachers/admins to create events by providing the event name and assigning an initial amount of points to it. The initial point value represents the worth of the event. The function also includes a calendar feature that allows teachers to select the date and time of the event. Once the event details are filled in, the teacher can confirm the event creation.

**Student View Events**
In the student view, the "Student View Events" function displays upcoming events to the logged-in students. The events show the initial point count and indicate whether the student participated in the event or simply attended. If a student participates, an additional 10 points are added to the initial point count. However, it's important to note that event participation requires approval from teachers, which is done through the "View Entries" function mentioned earlier.

**Leaderboard**
The "Leaderboard" function creates a new window showing the top students sorted by their point value. The leaderboard specifically focuses on students within the same grade, providing a fair comparison of achievements and points earned.

