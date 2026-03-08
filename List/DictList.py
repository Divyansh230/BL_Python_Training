students=[
    {"name":"Divyansh Singh","score":95},
    {"name":"Bulbul Singh","score":85},
    {"name":"Omi","score":85},
    {"name":"Dhruv","score":100}
]

students.sort(key=lambda x:x["score"],reverse=True)
print(students)