Link To Project: [\[link\]](https://yatridholakia.pythonanywhere.com/)

# Puddle - Your Online Marketplace

Puddle is an online marketplace that allows users to buy and sell items in a user-friendly environment. This project is based on the structure of a YouTube tutorial by CodeWithStein[\[link\]](https://www.youtube.com/watch?v=ZxMB6Njs3ck), but it has been extensively customized and improved to include additional features and enhancements.

## Features

- **User Authentication**: Users can create accounts, log in, and log out. User sessions are maintained securely.

- **Item Management**: Users can upload items for sale, view their uploaded items in a dashboard, and mark items as sold.

- **Dashboard**: The dashboard also allows users to view items they have sold and edit or delete their listings.

- **Browse and Search**: Users can browse items for sale, search by item name or description, filter by category, and sort by newest, oldest, most expensive, and cheapest.

- **Conversations**: Prospective buyers can contact sellers by initiating a conversation. Conversations can be viewed in the inbox, and messages can be exchanged between buyers and sellers in real-time.

- **Responsive Design**: Puddle features a fully responsive design, ensuring a seamless user experience on various devices.

## Usage

1.  Create a user account or log in if you already have one.
    
2.  Explore the dashboard to manage your items for sale and view sold items.
    
3.  Browse available items, filter by category, and use the search and sorting features to find what you're looking for.
    
4.  Contact sellers by initiating conversations. Access your conversations in the inbox.
    

## Customizations and Enhancements

This project was initially inspired by a YouTube tutorial by CodeWithStein[\[link\]](https://www.youtube.com/watch?v=ZxMB6Njs3ck). However, it has been significantly customized and enhanced with additional features, including but not limited to:

-   User logout functionality.
-   Additional styling and improvements to the user interface.
-   The ability to view sold-out items in the dashboard.
-   Enhanced item sorting options on the browse page.

## Technologies Used

- Python: Backend scripting  
- Django: Backend framework
- JavaScript: Frontend scripting 
- Django Template Language (DTL): Used for server-side templates 
- HTML: Frontend markup
- SQLite: Database
- Tailwind CSS: Styling


## Steps to run Dockerfile
- setup docker desktop
### run the following commands in the project directory
    - docker build -t my-django-app .
    - docker run -p 8000:8000 my-django-app
