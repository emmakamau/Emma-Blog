#### Sincerely Emma

Personal blog website where I can create and share my opinions and other users can read and comment on them. Additionally, has a feature that displays random quotes to inspire my users.

## Technology used
1. Python
2. Flask
3. HTML
4. CSS3
5. PostgresSQL

## Requirements
An IDE such as VS code with Python version 3 installed,a terminal and a browser. 

## Setup and Instruction
1. Clone the repository at [here](https://github.com/emmakamau/Emma-Blog.git).
2. Extract and open the folder on VS code or navigate to the folder on your terminal.
3. On the terminal, create a virtual environment `python3 -m venv virtual` and activate it `source virtual/bin/activate`. NB **virtual** is the name of the environment.
4. Pip install dependancies highlighted on the **requirements.txt** by running `pip install -r requirements.txt`
5. Create a **start.sh** file in the root directory of the folder and define the **secret key,email address and email password**.
6. Run `chmod +x start.sh` and `./start.sh` respectively on the terminal.
7. View the application on your browser through `http://127.0.0.1:5000`.


## Behaviour Driven Development

BDD focuses on how the user will interact with the application.
What you will see and experience:
1. A landing page with a quote,background and a navigation bar.
2. The Navbar has three routes to view blogs based on category. Also includes a route to sign in to the application.
3. Click on the sign in, if user does not have an account, they can click on sign up.
4. On the sign up form, the user is required to enter an email,unique username and a password. Upon registration the user receives a welcome email and is redirected to the sign in page.
5. After the user signs in, they can navigate to their profile through the navbar and update their profile pic and bio. They can add a new blog post as well. They also have an option to delete and edit a blog post.
6. On the blog display pages, a user can view other blogs.Click on the view more to get redirected to a particular blog with comments from other users displayed, ability to upvote,downvote and comment. If a user is an an author of a particular blog, they can delete undesired comments.
7. Click on the new comment and add a comment as well.
8. Click on signout to logout of the application.

## Development
To fix a bug or enhance an existing module, follow these steps:
- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request

## Known Bugs
- A user can vote more than once.
- Images do not display from db. 
- A user can only delete a blog post where it's yet to be voted or commented on

If you find a bug or would like to request a new function, reach out to me via Email: emmaculatewkamau@gmail.com or on [LinkedIn](https://www.linkedin.com/in/emmaculate-k-987353104/)

## Future Plans
- Ensure a user can only vote once for a particular blog.
- Display the owner of the blog.
- Ability to delete blog posts that have been voted or commented on.
- Save and display images from AWS S3 buckets
- Ability to navigate to other users profiles if any.

## License

[MIT](https://choosealicense.com/licenses/mit/)

Copyright (c) 2022 **Emmaculate Kamau**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.