from functools import total_ordering
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

#------------------------------------Profile----------------------------------------------------------------------------#
class Degree (models.Model):
    degree_choice = (
        ('ปริญญาตรี' , 'ปริญญาตรี'),
        ('ปริญญาโท', 'ปริญญาโท'),
        ('ปริญญาเอก', 'ปริญญาเอก')
    )
    degree = models.CharField(max_length=50, blank=True, null=True, choices=degree_choice)
    faculty = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    province = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    study_date = models.DateField(blank=True , default=None)
    graduate = models.DateField(blank=True , default=None)
    gpa = models.FloatField()
    honors = models.CharField(max_length=100)
    use_choice = (
        ('ใช้','ใช้'),
        ('ไม่ใช้','ไม่ใช้')
    )
    def __str__(self):
        return f'{self.faculty}' f' {self.degree}'

class User_Degee(models.Model):
    name = models.CharField(max_length=100)
    degree = models.ForeignKey(Degree , on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Faculty(models.Model):
    faculty = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.faculty

class Profile (models.Model):
    # username = models.OneToOneField(User , on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    id_Position = models.CharField(max_length=20)
    title_choice = (
        ('นาย','นาย'),
        ('นาง','นาง'),
        ('นางสาว','นางสาว'),
    )
    title_name = models.CharField(max_length=10, blank=True, null=True, choices=title_choice)
    name_th = models.CharField(max_length=100)
    name_eng = models.CharField(max_length=100)
    personal_choice = (
        ('พนักงานมหาวิทยาลัย','พนักงานมหาวิทยาลัย'),
        ('ลูกจ้างชั่วคราว','ลูกจ้างชั่วคราว')
    )
    personal_type = models.CharField(max_length=255, blank=True, null=True, choices=personal_choice)
    line_of_work_choice = (
        ('วิชาการ','วิชาการ'),
        ('สนับสนุน','สนับสนุน')
    )
    line_of_work = models.CharField(max_length=100, blank=True, null=True, choices=line_of_work_choice)
    position_choice = (
        ('อาจารย์','อาจารย์'),
        ('เจ้าหน้าที่บริหารงานทั้วไป','เจ้าหน้าที่บริหารงานทั้วไป'),
        ('บุคลากร','บุคลากร'),
        ('นักวิชาการศึกษา','นักวิชาการศึกษา'),
        ('นักวิเคราะห์นโยบายและเเผน','นักวิเคราะห์นโยบายและเเผน'),
        ('นักประชาสัมพันธ์','นักประชาสัมพันธ์'),
        ('นักวิทยาศาสตร์','นักวิทยาศาสตร์'),
        ('นักวิชาการโสตทัศนศึกษา','นักวิชาการโสตทัศนศึกษา'),
        ('นักวิชาการคอมพิวเตอร์','นักวิชาการคอมพิวเตอร์'),
        ('ครู','ครู')
    )
    position = models.CharField(max_length=100, blank=True, null=True, choices=position_choice)
    academic_choice = (
        ('ศาสตราจารย์','ศาสตราจารย์'),
        ('รองศาสตราจารย์','รองศาสตราจารย์'),
        ('ผู้ช่วยศาสตราจารย์','ผู้ช่วยศาสตราจารย์'),
        ('เชี่ยวชาญ','เชี่ยวชาญ'),
        ('ชำนาญการพิเศษ','ชำนาญการพิเศษ'),
        ('ชำนาญการ','ชำนาญการ')
    )
    academic_position = models.CharField(max_length=100, blank=True, null=True, choices=academic_choice)
    director_choice = (
        ('คณบดี','คณบดี'),
        ('รองคณบดี','รองคณบดี'),
        ('ผู้ช่วยคณบดี','ผู้ช่วยคณบดี'),
        ('ประธานหลักสูตร','ประธานหลักสูตร'),
        ('หัวหน้างาน','หัวหน้างาน')
    )
    director_position = models.CharField(max_length=100, blank=True, null=True, choices=director_choice)
    start_work_date = models.DateField(blank=True , default=None)
    placement_date = models.DateField(blank=True , default=None)
    status_job = models.DateField(blank=True , default=None)
    date_birth = models.DateField(blank=True , default=None)
    nationality = models.CharField(max_length=100)

    religion_choice = (
        ('พุทธ','พุทธ'),
        ('คริสต์','คริสต์'),
        ('อิสลาม','อิสลาม'),
        ('ยิว','ยิว'),
        ('ซิกข์','ซิกข์'),
        ('บาไฮ','บาไฮ'),
        ('โซโรอัสเตอร์','โซโรอัสเตอร์'),
        ('พราหมณ์-ฮินดู','พราหมณ์-ฮินดู'),
        ('เชน','เชน'),
        ('ไม่มีศาสนา','ไม่มีศาสนา')
    )
    religion_con = models.CharField(max_length=100, blank=True, null=True, choices=religion_choice)

    phone = models.CharField(max_length=10)
    email_UP = models.EmailField(max_length=255)
    email_private = models.EmailField(max_length=255)
    address = models.TextField()
    id_degree = models.ManyToManyField(User_Degee)
    faculty_id = models.ManyToManyField(Faculty)



