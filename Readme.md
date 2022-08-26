# Pay-Ed

PayEd is a digital payment solution for students as well as an ERP for the management of digital payment collections for students or members of academic institutions and the entities respectively.



## Language and Libraries

- Python 3.9
- Django 3.2

## Installation

Clone this repository and open it in an editor.

```bash
git clone https://github.com/Festus-Kwafo/PayEd.git
```

```bash
cd PayEd/src

py -m venv venv
call venv/scripts/activate

pip install -r requirements.txt

py manage.py makemigrations
py manage.py migrate
```

Install npm packages for preprocessing static files.

```bash
npm install
```

## Running

Run this command to spin up the django development server.

```bash
py manage.py runserver

```

Then run the command below to run the static files preprocessor.

```bash
npm start

```
