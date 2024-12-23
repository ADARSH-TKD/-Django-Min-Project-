from django.shortcuts import render

def calculator2(request):
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1', 0))
            num2 = float(request.POST.get('num2', 0))
            operation = request.POST.get('operation')

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Division by zero"
        except ValueError:
            result = "Error: Invalid input"
    
    return render(request, 'calculator2.html', {'c': result})
