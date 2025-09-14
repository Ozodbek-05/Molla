from django.db import models
from django.utils import timezone


class ContactModel(models.Model):
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=15, null=True, blank=True
    )
    subject = models.CharField(
        max_length=255, null=True, blank=True
    )
    message = models.TextField()

    is_read = models.BooleanField(default=False)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

class Department(models.Model):
    """Kafedra"""
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class Instructor(models.Model):
    """Oâ€˜qituvchi"""
    full_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="instructors")
    hire_date = models.DateField()

    class Meta:
        ordering = ["full_name"]
        indexes = [models.Index(fields=["department"])]

    def __str__(self):
        return self.full_name


class Student(models.Model):
    """Talaba"""
    full_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    year_of_study = models.PositiveSmallIntegerField()  # 1-4
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name


class Course(models.Model):
    """Fan"""
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=160)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="courses")
    credits = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.code} - {self.title}"


class Prerequisite(models.Model):
    """Fan uchun old shart (prereq)"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="prereqs_for")
    prerequisite = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="is_prereq_of")

    class Meta:
        unique_together = [("course", "prerequisite")]


class Term(models.Model):
    """Oâ€˜quv davri (yil+semestr)"""
    year = models.PositiveIntegerField()
    semester = models.CharField(max_length=16, choices=[("SPRING", "SPRING"), ("FALL", "FALL"), ("SUMMER", "SUMMER")])

    class Meta:
        unique_together = [("year", "semester")]

    def __str__(self):
        return f"{self.year} {self.semester}"


class Section(models.Model):
    """Fan kesimidagi guruh (section)"""
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name="sections")
    instructor = models.ForeignKey(Instructor, on_delete=models.PROTECT, related_name="sections")
    term = models.ForeignKey(Term, on_delete=models.PROTECT, related_name="sections")
    capacity = models.PositiveIntegerField(default=30)

    class Meta:
        unique_together = [("course", "instructor", "term")]
        indexes = [models.Index(fields=["term"])]

    def __str__(self):
        return f"{self.course.code} - {self.term}"


class Enrollment(models.Model):
    """Talabaning section ga yozilishi"""
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="enrollments")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrollments")
    enrolled_at = models.DateTimeField(default=timezone.now)
    grade = models.CharField(
        max_length=2, null=True, blank=True,
        choices=[("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"), ("F", "F")]
    )

    class Meta:
        unique_together = [("section", "student")]
        indexes = [models.Index(fields=["student", "section"])]

    def __str__(self):
        return f"{self.student} -> {self.section}"


class Exam(models.Model):
    """Imtihon (midterm/final)"""
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="exams")
    kind = models.CharField(max_length=10, choices=[("MID", "MID"), ("FIN", "FIN"), ("QUIZ", "QUIZ")])
    date = models.DateField()
    max_score = models.PositiveIntegerField(default=100)

    class Meta:
        unique_together = [("section", "kind")]


class ExamResult(models.Model):
    """Imtihon natijasi"""
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="results")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="exam_results")
    score = models.FloatField()

    class Meta:
        unique_together = [("exam", "student")]
        indexes = [models.Index(fields=["student"])]