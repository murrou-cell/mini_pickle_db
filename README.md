<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/murrou-cell/mini_pickle_db">
    <img src="https://github.com/murrou-cell/mini_pickle_db/raw/main/images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Mini-Pickle-Database-Framework</h3>

  <p align="center">
    An easy way to build your very own small database!
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This framework is used to create a light, easy to use and versatile database that fits perfectly in small projects or in larger tasks requiring a small database for some sort of data management.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

Below you can find a list of all major frameworks/libraries used to bootstrap this project:

* [Python](https://www.python.org/)
* [Python Pickle](https://docs.python.org/3/library/pickle.html)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->

### Prerequisites

* Python version 3.9 or above
* Pickle
* IDE (VS Code, PyCharm, Thonny etc.)

## Installation
  ```sh
  python -m pip install mini_pickle_db
  ```

<!-- USAGE EXAMPLES -->
## Usage

Here is how to framework actually functions: 

1. Initial steps:

  ```sh
  from mini_pickle_db.pickle_db import db
  ```
  1.1. You can initiate the database class using the: 
  ```sh
    database = db()
  ```
  1.2. You should specify the file path of the database document as shown below: 
  ```sh
    database.db_file = 'file_path'
  ```
  Note: The Wrapper will automatically create the file, but not the folder, so one must be created manually. 



2. Document Structure: 

  2.1. The documents follow a simple Python dictionary format as shown below: 
  ```sh
    example_doc = {
      "key_1": "value_1",
      "key_2": "value_2"
      }
  ```


3. Database Usage:
  2.1. How to insert a single document in the database: 
  ```sh
  single_doc = {
"key_1": "value_1",
"key_2": "value_2"
}
db.insert(single_doc)
  ```
  2.2. How to insert multiple documents in the database: 
  ```sh
  multiple_docs = [
    {
        "key_1": "value_1",
        "key_2": "value_2"
    },
    {
        "key_3":  "value_3",
        "key_4":  "value_4"
    }
  ]
  db.insert(multiple_docs)
  ```
  Note: The database automatically assigns an ID to every document and is autoincremented.
  ```sh
    [
      {"key_1": "value_1", "key_2": "value_2", "id": 0}, 
      {"key_1": "value_1", "key_2": "value_2", "id": 1}
    ]
  ```
  Note: The data type of the multiple document database is a list of dictionaries.

  2.3. How to load the database: 
  ```sh
    database.load()
  ```
  Note: It returns a list of dictionaries. 

  2.4. How to query the database:

  2.4.1. Query a single document: 
  ```sh
    database.query_one({'key_2': 'value'})
  ```
  Note: It will return only the first document it finds. 

  2.4.2. Query a multiple documents:
  ```sh
    database.query_many({'key_2': 'value'})
  ```
  Note: It will return all the documents matching the querry in a list format.

  2.5. How to delete document:
  ```sh
    database.delete({'key': 'value'})
  ```
  Note: It will delete all the documents matching the querry in a list format.
_For more examples, please refer to the [Documentation](https://docs.python.org/3/library/pickle.html)_

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Marin Dragolov - murrou13@gmail.com

Project Link: [https://github.com/murrou-cell/mini_pickle_db](https://github.com/murrou-cell/mini_pickle_db)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
<!--
Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Configuration Parser Framework](https://github.com/murrou-cell/configuration_parser)

* [ I've used 2](link)
* [ I've used 3](link)
* [ I've used 4](link)
* [ I've used 5](link)
-->

<p align="right">(<a href="#top">back to top</a>)</p>
