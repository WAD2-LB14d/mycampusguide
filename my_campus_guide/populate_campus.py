import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_campus_guide.settings')

import django
django.setup()

import datetime
from guide.models import Category, Course, Lecturer, CourseComment, LecturerComment, CourseRating, LecturerRating
from django.contrib.auth.models import User

def populate():
    course_pages = [
        {
            'name': 'Web App Development 2',
            'school': 'Computing Science',
            'credits': 10, 
            'year': 2021, 
            'requirements': 'GPA of B3 or better in level 1 courses at first sitting.',
            'currentlecturer': 'Alistair Morrison',
            'description': 'The aim of this course is to provide students with a comprehensive overview of web application development. It will provide students with the skills to design and develop distributed web applications in a disciplined manner, using a range of tools and technologies. It will also strengthen their understanding of the context and rationale of distributed systems.',
            'views' : 10
        },
        {
            'name': 'Algorithms and Data Structures 2',
            'school': 'Computing Science',
            'credits': 10, 
            'year': 2021, 
            'requirements': 'GPA of B3 or better in level 1 courses at first sitting.',
            'currentlecturer': 'Michele Sevegnani',
            'description': 'To familiarise students with fundamental data types and data structures used in programming, with the design and analysis of algorithms for the manipulation of such structures, and to provide practice in the implementation and use of these structures and algorithms in a Java context.',
            'views' : 15
        },
        {
            'name': 'Java Programming 2',
            'school': 'Computing Science',
            'credits': 10, 
            'year': 2021, 
            'requirements': 'GPA of B3 or better in level 1 courses at first sitting.',
            'currentlecturer': 'Mary Ellen Foster',
            'description': 'This course extends students experience in programming using a strongly typed language (Java) and strengthens their problem solving skills.',
            'views' : 12
        },
        {
            'name': 'Networks and Operating Systems Essentials 2',
            'school': 'Computing Science',
            'credits': 10, 
            'year': 2021, 
            'requirements': 'GPA of B3 or better in level 1 courses at first sitting.',
            'currentlecturer': 'Angelos Marnerides',
            'description': 'The course will introduce students to essential topics in computer networks and operating systems.',
            'views' : 5
        },
        {
            'name': 'Algorithmic Foundations',
            'school': 'Computing Science',
            'credits': 10, 
            'year': 2021, 
            'requirements': 'GPA of B3 or better in level 1 courses at first sitting.',
            'currentlecturer': 'Gethin Norman',
            'description': 'To introduce the foundational mathematics needed for Computing Science; To make students proficient in their use; To show how they can be applied to advantage in understanding computational phenomena.',
            'views' : 25
        },
        {
            'name': 'Science Skills',
            'school': 'Science and Engineering',
            'credits': 20, 
            'year': 2021, 
            'requirements': 'None.',
            'currentlecturer': 'Eric Yao',
            'description': 'This level 1 course is intended for science students. It is cross-curricular in nature, using topics within Astronomy, Chemistry, Geography & Earth Sciences, and Physics to develop students scientific problem solving skills and graduate attributes.',
            'views' : 1
        },
        {
            'name': 'Electronic Engineering 1X',
            'school': 'Science and Engineering',
            'credits': 20, 
            'year': 2021, 
            'requirements': 'None.',
            'currentlecturer': 'Martin Lavery',
            'description': 'You will study methods for calculating the behaviour of analogue and digital electronic circuits.',
            'views' : 2
        }
    ]

    lecturer_pages = [
        {
            'name': 'Alistair Morrison',
            'teaching': 'Web App Development 2',
            'description': 'Teaches Web App Development and Interactive Systems at Glasgow University.', 
            'picture': 'lecturer_images/AlistairMorrison.png',
            'views': 5
        },
        {
            'name': 'Michele Sevegnani',
            'teaching': 'Algorithms and Data Structures 2',
            'description': 'Teaches Algorithms and Data Structures 2 and Programming Languages at Glasgow University.', 
            'picture': 'lecturer_images/MicheleSevegnani.jpg',
            'views': 10
        },
        {
            'name': 'Mary Ellen Foster',
            'teaching': 'Java Programming 2',
            'description': 'Teaches Java Programming 2 at Glasgow University.', 
            'picture': 'lecturer_images/MaryEllenFoster.jpg',
            'views': 15
        },
        {
            'name': 'Angelos Marnerides',
            'teaching': 'Networks and Operating Systems Essentials 2',
            'description': 'Teaches Networks and Operating Systems Essentials at Glasgow University.', 
            'picture': 'lecturer_images/AngelosMarnerides.jpg',
            'views': 4
        },
        {
            'name': 'Gethin Norman',
            'teaching': 'Algorithmic Foundations',
            'description': 'Teaches Algorithmic Foundations at Glasgow University.', 
            'picture': 'lecturer_images/GethinNorman.jpg',
            'views': 10
        },
        {
            'name': 'Eric Yao',
            'teaching': 'Science Skills',
            'description': 'Teaches Science Skills at Glasgow University.', 
            'picture': 'lecturer_images/EricYao.jpg',
            'views': 5
        },
        {
            'name': 'Martin Lavery',
            'teaching': 'Electronic Engineering 1X',
            'description': 'Teaches Electronic Engineering 1X at Glasgow University.', 
            'picture': 'lecturer_images/MartinLavery.jpg',
            'views': 2
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

    for cat, cat_data in coursecats.items():
        c = add_cat(cat, cat_data["views"])
        for p in cat_data["pages"]:
            add_coursepage(c, p["name"], p["school"], p["credits"], p["year"], p["requirements"], p["currentlecturer"], p["description"], p["views"])

    for cat, cat_data in lecturercats.items():
        c = add_cat(cat, cat_data["views"])
        for p in cat_data["pages"]:
            add_lecturerpage(c, p["name"], p["teaching"], p["description"], p["picture"], p["views"])


    user_profiles = [
        {
            'email' : "johndoe33@gmail.com",
            'username' : "johndoe33",
            'major' : "Computing Science",
            'degreeprogram' : "BSc",
            'startedstudying' : datetime.date.today,
            'expectedgraduation' : datetime.date.today,
        },
         {           
            'email' : "foobar@gmail.com",
            'username' : "foobar",
            'major' : "Computing Science",
            'degreeprogram' : "MSci",
            'startedstudying' : datetime.date.today,
            'expectedgraduation' : datetime.date.today,
        },
        {           
            'email' : "abc@gmail.com",
            'username' : "abc",
            'major' : "Computing Science",
            'degreeprogram' : "MSci",
            'startedstudying' : datetime.date.today,
            'expectedgraduation' : datetime.date.today,
        },
        {           
            'email' : "JohnSmith@gmail.com",
            'username' : "JohnSmith",
            'major' : "Physics",
            'degreeprogram' : "BSc",
            'startedstudying' : datetime.date.today,
            'expectedgraduation' : datetime.date.today,
        },
    ]

    usercats = {
        "User Profiles" : {
            "pages" : user_profiles
        }
    }

    for cat, cat_data in usercats.items():
        c = add_usercat(cat)
        for p in cat_data["pages"]:
            add_userprofile(c, p["username"])


    course_comments = [
        {
            'date': datetime.datetime(2020, 5, 17),
            'comment': "I love it",
            'user': User.objects.get(username='johndoe33'),
            'page': Course.objects.get(name='Web App Development 2')
        },
        {
            'date': datetime.datetime(2021, 5, 17),
            'comment': "I hated it",
            'user': User.objects.get(username='foobar'),
            'page': Course.objects.get(name='Web App Development 2')
        },
        {
            'date': datetime.datetime(2020, 5, 31),
            'comment': "Best course at UofG",
            'user': User.objects.get(username='foobar'),
            'page': Course.objects.get(name='Algorithms and Data Structures 2')
        },
        {
            'date': datetime.datetime(2021, 3, 20),
            'comment': "Very good",
            'user': User.objects.get(username='abc'),
            'page': Course.objects.get(name='Java Programming 2')
        },
        {
            'date': datetime.datetime(2021, 4, 3),
            'comment': "Could be better",
            'user': User.objects.get(username='JohnSmith'),
            'page': Course.objects.get(name='Networks and Operating Systems Essentials 2')
        },
        {
            'date': datetime.datetime(2021, 1, 2),
            'comment': "Great course",
            'user': User.objects.get(username='foobar'),
            'page': Course.objects.get(name='Networks and Operating Systems Essentials 2')
        },
        {
            'date': datetime.datetime(2021, 2, 1),
            'comment': "Alright, could be better",
            'user': User.objects.get(username='abc'),
            'page': Course.objects.get(name='Algorithmic Foundations')
        }
    ]

    lecturer_comments = [
        {
            'date': datetime.datetime(2020, 4, 17),
            'comment': "I absolutely hated him",
            'user': User.objects.get(username='foobar'),
            'page': Lecturer.objects.get(name='Alistair Morrison')
        },
        {
            'date': datetime.datetime(2021, 5, 15),
            'comment': "I loved the style of teahing",
            'user': User.objects.get(username='johndoe33'),
            'page': Lecturer.objects.get(name='Alistair Morrison')
        },
        {
            'date': datetime.datetime(2020, 5, 11),
            'comment': "Best lecturer at UofG",
            'user': User.objects.get(username='johndoe33'),
            'page': Lecturer.objects.get(name='Alistair Morrison')
        },
        {
            'date': datetime.datetime(2021, 1, 8),
            'comment': "Good lecturer",
            'user': User.objects.get(username='JohnSmith'),
            'page': Lecturer.objects.get(name='Michele Sevegnani')
        },
        {
            'date': datetime.datetime(2021, 2, 7),
            'comment': "Passionate lecturer",
            'user': User.objects.get(username='JohnSmith'),
            'page': Lecturer.objects.get(name='Mary Ellen Foster')
        },
        {
            'date': datetime.datetime(2021, 4, 6),
            'comment': "Great lecturer",
            'user': User.objects.get(username='abc'),
            'page': Lecturer.objects.get(name='Gethin Norman')
        },
        {
            'date': datetime.datetime(2021, 3, 12),
            'comment': "Bad",
            'user': User.objects.get(username='abc'),
            'page': Lecturer.objects.get(name='Gethin Norman')
        }
    ]


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

    for cat, cat_data in lecturercommentcats.items():
        c = add_cat(cat, cat_data["views"])
        for p in cat_data["pages"]:
            add_lecturercomment(c, p["date"], p["comment"], p["user"], p["page"])

    for cat, cat_data in coursecommentcats.items():
        c = add_cat(cat, cat_data["views"])
        for p in cat_data["pages"]:
            add_coursecomment(c, p["date"], p["comment"], p["user"], p["page"])
    
    lecturer_ratings = [
        {
            'date': datetime.datetime(2020, 4, 17),
            'rating': 4,
            'user': User.objects.get(username='foobar'),
            'page': Lecturer.objects.get(name='Alistair Morrison')
        },
        {
            'date': datetime.datetime(2021, 5, 15),
            'rating': 3,
            'user': User.objects.get(username='johndoe33'),
            'page': Lecturer.objects.get(name='Alistair Morrison')
        },
        {
            'date': datetime.datetime(2021, 5, 11),
            'rating': 2,
            'user': User.objects.get(username='johndoe33'),
            'page': Lecturer.objects.get(name='Alistair Morrison')
        },
        {
            'date': datetime.datetime(2021, 4, 1),
            'rating': 4,
            'user': User.objects.get(username='abc'),
            'page': Lecturer.objects.get(name='Gethin Norman')
        },
        {
            'date': datetime.datetime(2021, 1, 1),
            'rating': 5,
            'user': User.objects.get(username='JohnSmith'),
            'page': Lecturer.objects.get(name='Gethin Norman')
        },
        {
            'date': datetime.datetime(2021, 2, 4),
            'rating': 3,
            'user': User.objects.get(username='JohnSmith'),
            'page': Lecturer.objects.get(name='Mary Ellen Foster')
        },
        {
            'date': datetime.datetime(2021, 3, 8),
            'rating': 2,
            'user': User.objects.get(username='JohnSmith'),
            'page': Lecturer.objects.get(name='Michele Sevegnani')
        },
    ]

    course_ratings = [
        {
            'date': datetime.datetime(2020, 4, 17),
            'rating': 5,
            'user': User.objects.get(username='foobar'),
            'page': Course.objects.get(name='Algorithms and Data Structures 2')
        },
        {
            'date': datetime.datetime(2021, 5, 15),
            'rating': 4,
            'user': User.objects.get(username='johndoe33'),
            'page': Course.objects.get(name='Algorithms and Data Structures 2')
        },
        {
            'date': datetime.datetime(2021, 5, 11),
            'rating': 5,
            'user': User.objects.get(username='johndoe33'),
            'page': Course.objects.get(name='Web App Development 2')
        },
        {
            'date': datetime.datetime(2021, 1, 11),
            'rating': 2,
            'user': User.objects.get(username='abc'),
            'page': Course.objects.get(name='Algorithms and Data Structures 2')
        },
        {
            'date': datetime.datetime(2021, 1, 2),
            'rating': 2,
            'user': User.objects.get(username='abc'),
            'page': Course.objects.get(name='Networks and Operating Systems Essentials 2')
        },
        {
            'date': datetime.datetime(2021, 4, 12),
            'rating': 4,
            'user': User.objects.get(username='JohnSmith'),
            'page': Course.objects.get(name='Networks and Operating Systems Essentials 2')
        },
        {
            'date': datetime.datetime(2021, 2, 26),
            'rating': 2,
            'user': User.objects.get(username='JohnSmith'),
            'page': Course.objects.get(name='Algorithmic Foundations')
        },
    ]

    lecturerratingcats = {
        "Lecturer Comments": {
            "views": 15,
            "pages": lecturer_ratings
        }
    }

    courseratingcats = {
        "Course Comments": {
            "views": 15,
            "pages": course_ratings
        }
    }
    
    for cat, cat_data in lecturerratingcats.items():
        c = add_cat(cat, cat_data["views"])
        for p in cat_data["pages"]:
            add_lecturerrating(c, p["date"], p["rating"], p["user"], p["page"])

    for cat, cat_data in courseratingcats.items():
        c = add_cat(cat, cat_data["views"])
        for p in cat_data["pages"]:
            add_courserating(c, p["date"], p["rating"], p["user"], p["page"])
    

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

def add_usercat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_lecturercomment(cat, date, comment, user, name):
    c = LecturerComment.objects.get_or_create(date=date, comment=comment, user=User.objects.get(username=user), page=Lecturer.objects.get(name=name))[0]
    return c

def add_coursecomment(cat, date, comment, user, course_name):
    c = CourseComment.objects.get_or_create(date=date, comment=comment, user=User.objects.get(username=user), page=Course.objects.get(name=course_name))[0]
    return c

def add_lecturerrating(cat, date, rating, user, name):
    c = LecturerRating.objects.get_or_create(date=date, rating=rating, user=User.objects.get(username=user), page=Lecturer.objects.get(name=name))[0]
    return c

def add_courserating(cat, date, rating, user, course_name):
    c = CourseRating.objects.get_or_create(date=date, rating=rating, user=User.objects.get(username=user), page=Course.objects.get(name=course_name))[0]
    return c

def add_userprofile(cat, username):
    c = User.objects.get_or_create(username=username)[0]
    return c

if __name__ == '__main__':
    print("Starting Campus population script...")
    populate()
