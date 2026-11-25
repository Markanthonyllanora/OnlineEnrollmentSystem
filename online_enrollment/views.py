
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q

from .models import Student
from .forms import StudentForm


# ==========================
# SAMPLE STUDENT DATA
# ==========================

def add_sample_students():

    # STUDENT 1
    Student.objects.get_or_create(
        student_number="2026-001",
        defaults={
            # STUDENT INFORMATION
            "full_name": "Juan Dela Cruz",
            "course": "BS Information Technology",
            "year_level": "1st Year",
            "section": "A",
            "email": "juan@gmail.com",
            "contact_number": "09123456789",
            "birth_date": "2005-05-15",
            "address": "Mabitac, Laguna",

            # FATHER INFORMATION
            "father_name": "Pedro Dela Cruz",
            "father_occupation": "Farmer",
            "father_contact": "09111111111",

            # MOTHER INFORMATION
            "mother_name": "Ana Dela Cruz",
            "mother_occupation": "Teacher",
            "mother_contact": "09222222222",
        }
    )

    # STUDENT 2
    Student.objects.get_or_create(
        student_number="2026-002",
        defaults={
            # STUDENT INFORMATION
            "full_name": "Maria Santos",
            "course": "BS Information Technology",
            "year_level": "2nd Year",
            "section": "B",
            "email": "maria@gmail.com",
            "contact_number": "09987654321",
            "birth_date": "2004-08-20",
            "address": "Siniloan, Laguna",

            # FATHER INFORMATION
            "father_name": "Jose Santos",
            "father_occupation": "Driver",
            "father_contact": "09333333333",

            # MOTHER INFORMATION
            "mother_name": "Rosa Santos",
            "mother_occupation": "Housewife",
            "mother_contact": "09444444444",
        }
    )


# ==========================
# LOGIN
# ==========================

def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_staff:
            login(request, user)
            return redirect("dashboard")

        messages.error(request, "Invalid username or password.")

    return render(request, "login.html")


# ==========================
# SKIP REGISTRATION
# DEMO USE ONLY
# ==========================

def skip_registration(request):

    if request.method != "POST":
        return redirect("login")

    demo_user, created = User.objects.get_or_create(
        username="demo_admin",
        defaults={
            "is_staff": True,
            "is_active": True,
        }
    )

    if created:
        demo_user.set_unusable_password()
        demo_user.save()

    if not demo_user.is_active or not demo_user.is_staff:
        messages.error(request, "Admin access unavailable.")
        return redirect("login")

    login(
        request,
        demo_user,
        backend="django.contrib.auth.backends.ModelBackend"
    )

    return redirect("dashboard")


# ==========================
# DASHBOARD
# ==========================

@login_required(login_url="login")
def dashboard_view(request):

    if not request.user.is_staff:
        return redirect("login")

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Student added successfully!"
            )

            return redirect("dashboard")

        students = Student.objects.all().order_by("full_name")

        return render(request, "dashboard.html", {
            "students": students,
            "form": form,
        })

    students = Student.objects.all().order_by("full_name")

    search = request.GET.get("search", "").strip()
    year = request.GET.get("year", "")
    section = request.GET.get("section", "")

    if search:
        students = students.filter(
            Q(full_name__icontains=search) |
            Q(student_number__icontains=search)
        )

    if year:
        students = students.filter(year_level=year)

    if section:
        students = students.filter(section__iexact=section)

    sections = (
        Student.objects
        .exclude(section="")
        .values_list("section", flat=True)
        .distinct()
        .order_by("section")
    )

    context = {
        "students": students,
        "sections": sections,
        "search": search,
        "selected_year": year,
        "selected_section": section,
        "form": StudentForm(),
    }

    return render(request, "dashboard.html", context)


# ==========================
# STUDENT PROFILE
# ==========================

@login_required(login_url="login")
def student_detail(request, student_id):

    if not request.user.is_staff:
        return redirect("login")

    student = get_object_or_404(
        Student,
        id=student_id
    )

    return render(
        request,
        "student_detail.html",
        {"student": student}
    )


# ==========================
# EDIT STUDENT
# ==========================

@login_required(login_url="login")
def edit_student(request, student_id):

    if not request.user.is_staff:
        return redirect("login")

    student = get_object_or_404(
        Student,
        id=student_id
    )

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Student information updated successfully!"
            )

            return redirect(
                "student_detail",
                student_id=student.id
            )

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        "student_edit.html",
        {
            "form": form,
            "student": student,
        }
    )


# ==========================
# LOGOUT
# ==========================

def logout_view(request):

    if request.method == "POST":
        logout(request)

    return redirect("login")
