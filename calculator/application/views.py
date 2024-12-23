from django.shortcuts import render

def calculator(request):  # sourcery skip: assign-if-exp, switch
    c = ""
    if request.method == "POST":
        n1 = request.POST.get("num1")
        n2 = request.POST.get("num2")  
        opr = request.POST.get("opr")

        # Validate inputs
        if n1.isdigit() and n2.isdigit():
            n1 = int(n1)
            n2 = int(n2)
            if opr == "+":
                c = n1 + n2
            elif opr == "-":
                c = n1 - n2
            elif opr == "/":
                if n2 != 0:
                    c = n1 / n2
                else:
                    c = "Error: Division by zero"
            elif opr == "*":
                c = n1 * n2
            else:
                c = "Invalid operation"
        else:
            c = "Error: Please enter valid numbers."
    print(n1,opr,n2,"=",c)
    return render(request, "calculator.html", {"c": c})
