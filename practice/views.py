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


# ************************************************************************************************
def f1(request, sum):
    return render(request, "result.html", {"sum": sum})


# def result(request):
#     sum = []
#     if request.GET:
#         sum = int(request.GET['sum'])
#     return render(request, "result.html", {'sum': sum})

# ************************************************************************************************
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


# ************************************************************************************************
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


# ************************************************************************************************
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
                pass
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


# *****************************************************************************************************
def quiz(request):
    qno = 0
    questions = [{"question": "C is a programming language", "option1": "True", "option2": "False", "option3": "Yes",
                  "option4": "NO", "correct": "4"},
                 {"question": "Java is not a programming language", "option1": "True", "option2": False,
                  "option3": "Yes",
                  "option4": "NO", "correct": "2"},
                 {"question": "C is not a programming language", "option1": "True", "option2": False, "option3": "Yes",
                  "option4": "NO", "correct": "1"}]

    if request.GET:
        sub = request.GET["submit"]
        qno = int(request.GET["qno"])
        option = request.GET["option"]
        correctanswer = questions[qno].get("correct")
        print(option, correctanswer)
        iscorrect = option == correctanswer
        print(iscorrect)
        qno += 1
        if qno >= len(questions):
            return render(request, "result.html")

    # print(question["option1"])
    question = questions[qno]
    return render(request, "newtest.html", {"question": question, "qno": qno, "qnumber": qno + 1})


# ********************************************************************************************************

def apiquiz(request):
    answers = request.session.get("answers")
    if answers == None:
        answers = []
    qno = 0
    if qno == 0:
        try:
            request.session.pop("answers")
        except:
            pass
    # p = ''
    response = requests.get(
        'https://gist.githubusercontent.com/champaksworldcreate/320e5af5ea9dbd31597d220637885587/raw/99f8f7a4df34ae477dcceb62598aa0bdde9ef685/tfquestions.json')
    data = response.json()
    data = data.get("questions")
    p = data[qno]["question"]
    # print(len(data))
    # print(data)
    if request.GET:
        option = int(request.GET["option"])
        if option == 1:
            option = "true"
        else:
            option = "false"

        correctanswer = data[qno].get("correctanswer")
        # print(option, correctanswer)
        iscorrect = option == correctanswer        # this will give us a boolean option
        answers.append(iscorrect)
        request.session["answers"] = answers
        # print((iscorrect))
        qno = int(request.GET["qno"])
        qno += 1
        if qno >= len(data):
            return render(request, "result.html", {"answer": answers})
        p = data[qno]["question"]

    # print(p)
    return render(request, "apitest.html", {"data": p, "qnumber": qno + 1, "qno": qno})


def session(request):
    key = ""
    value = ""
    if request.GET:
        submit = request.GET["submit"]
        key = request.GET["key"]

        value = request.GET["value"]
    session = request.session
    session[key] = value
    return render(request, "session.html", {"session": session, "key": key, "value": value})


def sessionview(request):
    return render(request, "sessionview.html", {"session": request.session.items()})


def sessionremove(request):
    key = ""
    if request.POST:
        key = request.POST["key"]
        try:
            request.session.pop(key)
        except:
            pass
    return render(request, "sessionremove.html", {"key": key})
