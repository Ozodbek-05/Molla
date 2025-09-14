from apps.pages.models import *


def run():
    def homework1_get_courses_without_enrollments():
        """Hech bir sectionida yozilish boâ€˜lmagan fanlarni qaytaradi"""
        return Course.objects.filter(sections__isnull=True)

    def homework2_get_students_not_enrolled_in_term(term_id):
        """Berilgan termda umuman yozilmagan talabalarni qaytaradi"""
        pass

    def homework3_get_instructors_with_full_sections(term_id):
        """Berilgan termda toâ€˜liq toâ€˜lgan (capacity ga teng) sectionlari bor oâ€˜qituvchilarni qaytaradi"""
        pass

    def homework4_get_overbooked_sections(term_id):
        """Capacity dan ortiq yozilgan sectionlarni (xato holat) topadi"""
        pass

    def homework5_get_top_students_in_course(course_code, term_id, limit=5):
        """Kurs boâ€˜yicha eng yuqori oâ€˜rtacha imtihon balliga ega talabalarni qaytaradi"""
        pass

    def homework6_get_all_active_students():
        """Faol (is_active=True) talabalarni qaytaradi"""
        return Student.objects.filter(is_active=True)

    def homework7_get_courses_in_department(department_id):
        """Berilgan kafedradagi fanlarni qaytaradi"""
        return Course.objects.filter(department__id=department_id)

    def homework8_get_instructors_in_department(department_name):
        """Berilgan kafedradagi oâ€˜qituvchilarni qaytaradi"""
        return Instructor.objects.filter(department__name=department_name)

    def homework9_get_students_by_year(year):
        """Berilgan kurs (year_of_study) dagi talabalarni qaytaradi"""
        return Student.objects.filter(year_of_study=year)

    def homework10_get_sections_for_course(course_code):
        """Berilgan kursga tegishli barcha sectionlarni qaytaradi"""
        return Section.objects.filter(course__code=course_code)

    def homework11_get_students_born_this_year():
        """Hozirgi yilda tugâ€˜ilgan talabalarni qaytaradi"""
        current_year = timezone.now().year
        return Student.objects.filter(birth_date__year=current_year)

    def homework12_get_courses_taught_by_instructor(instructor_id):
        """Berilgan instructor tomonidan oâ€˜tiladigan fanlarni qaytaradi"""
        return Course.objects.filter(section__instructor_id=instructor_id).distict()

    def homework13_get_courses_without_prerequisites():
        """Hech qanday prerequisite talab qilmaydigan fanlarni qaytaradi"""
        return Course.objects.filter(is_prereq_of__isnull=True)

    def homework14_get_enrollments_of_student(student_id):
        """Berilgan talabaning barcha yozilishlarini qaytaradi"""
        return Student.objects.filter(student_id=student_id)

    def homework15_get_exam_results_of_student(student_id):
        """Berilgan talabaning barcha imtihon natijalarini qaytaradi"""
        return ExamResult.objects.filter(student_id=student_id)

if __name__ == '__main__':
    run()