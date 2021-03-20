import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_campus_guide.settings')

import django
django.setup()
from guide.models import Category, Course, Lecturer, CourseComment, LecturerComment, CourseRating, LecturerRating

def populate():
    course_pages = [
        {
            'name': 'Web App Development 2',
            'school': 'Computing Science',
            'year': 2021, 
            'requirements': 'GPA of B3 or better in level 1 courses at first sitting.',
            'currentlecturer': 'Alistair Morrison',
            'description': 'The aim of this course is to provide students with a comprehensive overview of web application development. It will provide students with the skills to design and develop distributed web applications in a disciplined manner, using a range of tools and technologies. It will also strengthen their understanding of the context and rationale of distributed systems.',
            'views' : 10
        },
        {
            'name': 'Algorithms and Data Structures 2',
            'school': 'Computing Science',
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

    for cat, cat_data in coursecats.items():
        c = add_cat(cat, cat_data["views"])
        for p in cat_data["pages"]:
            add_coursepage(c, p["name"], p["school"], p["year"], p["requirements"], p["currentlecturer"], p["description"], p["views"])

    for cat, cat_data in lecturercats.items():
        c = add_cat(cat, cat_data["views"])
        for p in cat_data["pages"]:
            add_coursepage(c, p["name"], p["teaching"], p["description"], p["picture"], p["views"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_coursepage(cat, name, school, year, requirements, currentlecturer, desciption, views):
    p = Page.objects.get_or_create(category=cat, name=name)[0]
    p.school = school
    p.year = year
    p.requirements = requirements
    p.currentlecturer = currentlecturer
    p.description = description
    p.views = views
    p.save()
    return p


def add_lecturerpage(cat, name, teaching, description, picture, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
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


if __name__ == '__main__':
    print("Starting Campus population script...")
    populate()