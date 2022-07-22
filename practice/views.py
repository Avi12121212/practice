import requests
from django.shortcuts import render, HttpResponse

apikey = "AIzaSyBbLTo3239yz8J1o0FNChHu3WxWf1MgVe4"


def home(request):
    return HttpResponse("hello avinash")


def books(request):
    sum = 0
    num1 = []
    num2 = []
    if request.GET:
        num1 = int(request.GET["fname"])
        num2 = int(request.GET["sname"])
        opt = request.GET["submit"]
        if opt == "add":
            sum = num1 + num2
        if opt == "sub":
            sum = num1 - num2
        if opt == "mul":
            sum = num1 * num2
        print(sum)
    # return f1(request, sum)
    return render(request, "a.html", {'sum': sum, 'num1': num1, 'num2': num2})


def f1(request, sum):
    return render(request, "result.html", {"sum": sum})


# def result(request):
#     sum = []
#     if request.GET:
#         sum = int(request.GET['sum'])
#     return render(request, "result.html", {'sum': sum})


def radio(request):
    sum = 0
    num1 = []
    num2 = []
    opt = ""
    if request.GET:
        num1 = int(request.GET["fname"])
        num2 = int(request.GET["sname"])
        opt = request.GET["submit"]
        print(opt)
        if opt == "add":
            sum = num1 + num2
        if opt == "sub":
            sum = num1 - num2
        if opt == "mul":
            sum = num1 * num2
        print(sum)

    return render(request, "b.html", {'sum': sum, 'num1': num1, 'num2': num2, 'submit': opt})


def api(request):
    response = requests.get('https://swapi.dev/api/')
    data = response.json()
    print(data)
    return render(request, "api.html", {'data': data})


def getdata(request):
    link = request.GET["value"]
    response = requests.get(link)
    data = response.json()
    print(data)
    return render(request, "getdata.html", {'link': data})


def test(request):
    qno = 0
    opt = ""
    l = []
    l1 = []
    right_ans = []
    score = 0
    questions = [{"question": "C is a programming language", "answer": True},
                 {"question": "Java is not a programming language", "answer": False},
                 {"question": "C is not a programming language", "answer": False},
                 {"question": "java contains opps concept", "answer": True},
                 {"question": "maths contains opps concept", "answer": False},
                 {"question": "maths is important for engineering", "answer": True},
                 {"question": "earth is the second largest planet", "answer": False},
                 {"question": "india is a democratic country", "answer": True},
                 {"question": "english is a universal language", "answer": True}]

    # print(questions[1]["answer"])

    if request.GET:
        qno = int(request.GET["qno"])
        opt = request.GET["option"]

        l1 = request.GET["l"]
        # print(l1, type(l1), "***************")
        l1 = l1[1:-1]
        # print(l1)
        l1 = l1.split(',')
        # print(l1)
        for i in l1:
            if i == '':
                continue
            l.append(int(i))

        # l.append(opt)
        print(l)

        if opt == "True" or opt == "False":
            if opt == "True":
                l.append(1)
            else:
                l.append(0)
            qno = int(request.GET["qno"])
            qno += 1
    if qno >= len(questions):
        for p in questions:
            if p["answer"] == True:
                right_ans.append(1)
            else:
                right_ans.append(0)
        for i in range(len(l)):
            if right_ans[i] == l[i]:
                score += 1

        return render(request, "resultpage.html", {"l": l, "right": right_ans, "score": score})
    question = questions[qno]

    return render(request, "test.html", {"qno": qno, "qnumber": qno + 1, "question": question, "opt": opt, "l": l})


def quiz(request):
    qno = 0
    questions = [{"question": "C is a programming language", "option1": "True", "option2": "False", "option3": "Yes",
                  "option4": "NO"},
                 {"question": "Java is not a programming language", "option1": True, "option2": False, "option3": "Yes",
                  "option4": "NO"},
                 {"question": "C is not a programming language", "option1": True, "option2": False, "option3": "Yes",
                  "option4": "NO"}]
    question = questions[qno]
    if request.GET:
        
    # print(question["option1"])
    return render(request, "newtest.html", {"question": question, "qnumber": qno + 1})
