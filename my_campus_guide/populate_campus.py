import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_campus_guide.settings')

import django
django.setup()

import datetime
from guide.models import Category, Course, Lecturer, CourseComment, LecturerComment, CourseRating, LecturerRating

def populate():
    course_pages = [
        {
            'name': 'Web App Development 2',
            'school': 'Computing Science',
            'credits': 20, 
            'year': 2021, 
            'requirements': 'GPA of B3 or better in level 1 courses at first sitting.',
            'currentlecturer': 'Alistair Morrison',
            'description': 'The aim of this course is to provide students with a comprehensive overview of web application development. It will provide students with the skills to design and develop distributed web applications in a disciplined manner, using a range of tools and technologies. It will also strengthen their understanding of the context and rationale of distributed systems.',
            'views' : 10
        },
        {
            'name': 'Algorithms and Data Structures 2',
            'school': 'Computing Science',
            'credits': 20, 
            'year': 2021, 
            'requirements': 'GPA of B3 or better in level 1 courses at first sitting.',
            'currentlecturer': 'Michele Sevegnani',
            'description': 'To familiarise students with fundamental data types and data structures used in programming, with the design and analysis of algorithms for the manipulation of such structures, and to provide practice in the implementation and use of these structures and algorithms in a Java context.',
            'views' : 15
        }
    ]

    lecturer_pages = [
        {
            'name': 'Alistair Morrison',
            'teaching': 'Web App Development 2',
            'description': 'Teaches Web App Development and Interactive Systems at Glasgow University.', 
            'picture': None,
            'views': 5
        },
        {
            'name': 'Michele Sevegnani',
            'teaching': 'Algorithms and Data Structures 2',
            'description': 'Teaches Algorithms and Data Structures 2 and Programming Languages at Glasgow University.', 
            'picture': None,
            'views': 10
        }
    ]
    
    course_comments = [
        {
            'date': datetime.datetime(2020, 5, 17),
            'comment': "I love it",
            'user': "John Doe",
            'page': "Web App Development 2"
        },
        {
            'date': datetime.datetime(2021, 5, 17),
            'comment': "I hated it",
            'user': "Foo Bar",
            'page': "Web App Development 2"
        },
        {
            'date': datetime.datetime(2000, 5, 31),
            'comment': "Best course at UofG",
            'user': "Jim Brown",
            'page': "Algorithms and Data Structures 2"
        },
    ]

    lecturer_comments = [
        {
            'date': datetime.datetime(2020, 4, 17),
            'comment': "I absolutely hated him",
            'user': "John Doe",
            'page': "Michele Sevegnani"
        },
        {
            'date': datetime.datetime(2021, 5, 15),
            'comment': "I loved the style of teahing",
            'user': "Foo Bar",
            'page': "Michele Sevegnani"
        },
        {
            'date': datetime.datetime(2000, 5, 11),
            'comment': "Best lecturer at UofG",
            'user': "Jim Brown",
            'page': "Alistair Morrison"
        },
    ]

    coursecats = {
        "Course Pages": {
            "views": 20,
            "pages": course_pages
        }
    }

    lecturercats = {
        "Lecturer Pages": {
            "views": 25,
            "pages": lecturer_pages
        }
    }


    lecturercommentcats = {
        "Lecturer Comments": {
            "views": 15,
            "pages": lecturer_comments
        }
    }

    coursecommentcats = {
        "Course Comments": {
            "views": 15,
            "pages": course_comments
        }
    }

    for cat, cat_data in coursecats.items():
        c = add_cat(cat, cat_data["views"])
        for p in cat_data["pages"]:
            add_coursepage(c, p["name"], p["school"], p["credits"], p["year"], p["requirements"], p["currentlecturer"], p["description"], p["views"])

    for cat, cat_data in lecturercats.items():
        c = add_cat(cat, cat_data["views"])
        for p in cat_data["pages"]:
            add_lecturerpage(c, p["name"], p["teaching"], p["description"], p["picture"], p["views"])

    for cat, cat_data in lecturercommentcats.items():
        c = add_cat(cat, cat_data["views"])
        for p in cat_data["pages"]:
            add_lecturercomment(c, p["date"], p["comment"], p["user"], p["page"])

    for cat, cat_data in coursecommentcats.items():
        c = add_cat(cat, cat_data["views"])
        for p in cat_data["pages"]:
            add_lecturercomment(c, p["date"], p["comment"], p["user"], p["page"])

    for c in Category.objects.all():
        for p in Course.objects.filter(category=c):
            print(f'- {c}: {p}')
        for p in Lecturer.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_coursepage(cat, name, school, credits, year, requirements, currentlecturer, description, views):
    p = Course.objects.get_or_create(category=cat, name=name)[0]
    p.school = school
    p.credits = credits
    p.year = year
    p.requirements = requirements
    p.currentlecturer = currentlecturer
    p.description = description
    p.views = views
    p.save()
    return p


def add_lecturerpage(cat, name, teaching, description, picture, views):
    p = Lecturer.objects.get_or_create(category=cat, name=name)[0]
    p.teaching = teaching
    p.description = description
    p.picture = picture
    p.views = views
    p.save()
    return p

def add_cat(name, views):
    c = Category.objects.get_or_create(name=name, views=views)[0]
    c.save()
    return c

def add_lecturercomment(cat, date, comment, user, name):
    c = LecturerComment.objects.get_or_create(date=date, comment=comment, user=User.objects.get(name=user), page=Lecturer.objects.get(name=name))[0]
    return c


def add_coursecomment(cat, date, comment, user, course_name):
    c = CourseComment.objects.get_or_create(date=date, comment=comment, user=User.objects.get(name=user), page=Course.objects.get(name=course_name))[0]
    return c

if __name__ == '__main__':
    print("Starting Campus population script...")
    populate()
