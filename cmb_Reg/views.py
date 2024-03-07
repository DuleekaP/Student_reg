from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm, BioDataForm, EmergencyContactFrom
from django.contrib.auth.decorators import login_required
from .models import BioData, Qualifications, Employment, Publication, refrees, Application
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from django.utils import timezone


# Create your views here.
# Home page
def index(request):
    return render(request, 'cmb_Reg/index.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'cmb_Reg/signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'cmb_Reg/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

def user_details(request):
    user = request.user   
    if request.method == "POST":
        fullname = request.POST['fullname']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        birthday = request.POST['birthday']
        nic = request.POST['nic'] 
        gender = request.POST['gender']
        marital_status = request.POST['marital_status']
        contact = request.POST['contact']
        address = request.POST['address'] 
        email = request.POST['email']
        scanned_nic = request.POST['scanned_nic']
        profile_pic = request.POST['profile_pic']
        e_name = request.POST['e_name']
        e_relationship = request.POST['e_relationship']
        e_contact = request.POST['e_contact']
        e_address = request.POST['e_address']
        ins = BioData(user = user, fullname = fullname, firstname = firstname, lastname = lastname, birthday = birthday, nic = nic, 
        gender = gender, marital_status = marital_status, contact = contact, address = address, email = email, scanned_nic = scanned_nic, 
        profile_pic = profile_pic, e_name = e_name, e_relationship = e_relationship, e_contact = e_contact, e_address = e_address
        )
        ins.save()
        print('data has been written to DB')
        return redirect('profile')
    else:
        try:
            # Attempt to retrieve the record from the database
            record = BioData.objects.get(user=request.user)
                       
            return render(request, 'cmb_Reg/taskbar_profile.html', {'record': record})
        except BioData.DoesNotExist:
                       
            return render(request, 'cmb_Reg/taskbar_profile.html')
        


def display_record(request, user):
    # Query the database to retrieve the specific record
    record = BioData.objects.get(id=user_id)  # Replace YourModel with your actual model name and id with the correct field name

    # Pass the record to the template
    return render(request, 'your_template.html', {'record': record})


def user_qualification(request):
    user = request.user
    if request.method == "POST":   
        al_year = request.POST['al_year']
        stream = request.POST['stream']
        subject1 = request.POST['subject1']
        subject2 = request.POST['subject2']
        subject3 = request.POST['subject3']
        subject4 = request.POST['subject4']
        result1 = request.POST['result1']
        result2 = request.POST['result2']
        result3 = request.POST['result3']
        result4 = request.POST['result4']
        resultSheet = request.POST['resultSheet']
        degreeName = request.POST['degreeName']
        institute = request.POST['institute']
        gpa = request.POST['gpa']
        degreeClass = request.POST['degreeClass']
        degreestartYear = request.POST['degreestartYear']
        graduateYear = request.POST['graduateYear']
        transcript = request.POST['transcript']

        ins = Qualifications(user=user,stream=stream, al_year=al_year, subject1=subject1, subject2=subject2, subject3=subject3,
                            subject4=subject4, result1=result1, result2=result2, result3=result3, result4=result4,
                            resultSheet=resultSheet, degreeName=degreeName, institute=institute, gpa=gpa,
                            degreeClass=degreeClass, degreestartYear=degreestartYear, graduateYear=graduateYear,
                            transcript=transcript)
        ins.save()
        print('Education Qualification data has been written to DB')
        return redirect('education')
    else:
        try:
            # Attempt to retrieve the record from the database
            record = Qualifications.objects.get(user=request.user)
            return render(request, 'cmb_Reg/taskbar_education.html', {'record': record})
        except Qualifications.DoesNotExist:
            
            return render(request, 'cmb_Reg/taskbar_education.html')
        
def user_employement(request):
    user = request.user
    if request.method == "POST":   
        c_name = request.POST['c_name']
        c_designation = request.POST['c_designation']
        c_duties = request.POST['c_duties']
        c_contact = request.POST['c_contact']
        c_email = request.POST['c_email']
        c_fax = request.POST['c_fax']
        c_address = request.POST['c_address']
        p_name = request.POST['p_name']
        p_designation = request.POST['p_designation']
        p_duties = request.POST['p_duties']
        p_startDate = request.POST['p_startDate']
        p_endDate = request.POST['p_endDate']
        p_address = request.POST['p_address']

        # Create Employment instance
        ins = Employment.objects.create(user=user, c_name=c_name, c_designation=c_designation, c_duties=c_duties,
                                            c_contact=c_contact, c_email=c_email, c_fax=c_fax, c_address=c_address,
                                            p_name=p_name, p_designation=p_designation, p_duties=p_duties,
                                            p_startDate=p_startDate, p_endDate=p_endDate, p_address=p_address)
        ins.save()
        print('Employement data has been written to DB')
        return redirect('employement')
    else:
        try:
            # Attempt to retrieve the record from the database
            record = Employment.objects.get(user=request.user)
            return render(request, 'cmb_Reg/taskbar_employement.html', {'record': record})
        except Employment.DoesNotExist:
            
            return render(request, 'cmb_Reg/taskbar_employement.html')
        
def user_publication(request):
    user = request.user
    if request.method == "POST":   
        title = request.POST['title']
        authors = request.POST['authors']
        journal = request.POST['journal']
        doi = request.POST['doi']
        abstract = request.POST['abstract']
        title2 = request.POST['title2']
        authors2 = request.POST['authors2']
        journal2 = request.POST['journal2']
        doi2 = request.POST['doi2']
        abstract2 = request.POST['abstract2']

        # Create Publications instance
        ins = Publication.objects.create(user=user, title=title, authors=authors, journal=journal,
                                                    doi=doi, abstract=abstract, title2=title2,
                                                    authors2=authors2, journal2=journal2, doi2=doi2,
                                                    abstract2=abstract2)
        ins.save()
        print('publication data has been written to DB')
        return redirect('publications')
    else:
        try:
            # Attempt to retrieve the record from the database
            record = Publication.objects.get(user=request.user)
            print(record.title)
            return render(request, 'cmb_Reg/taskbar_publications.html', {'record': record})
        except Publication.DoesNotExist:
            #record = Publication.objects.get(id=1)
            #print(record.title)
            return render(request, 'cmb_Reg/taskbar_publications.html')
        
def user_refrees(request):
    user = request.user
    if request.method == "POST":   
        r1_name = request.POST['r1_name']
        r1_designation = request.POST['r1_designation']
        r1_organization = request.POST['r1_organization']
        r1_contact = request.POST['r1_contact']
        r1_address = request.POST['r1_address']
        r1_email = request.POST['r1_email']
        r2_name = request.POST['r2_name']
        r2_designation = request.POST['r2_designation']
        r2_organization = request.POST['r2_organization']
        r2_contact = request.POST['r2_contact']
        r2_address = request.POST['r2_address']
        r2_email = request.POST['r2_email']

        # Create refrees instance
        ins = refrees.objects.create(user=user, r1_name=r1_name, r1_designation=r1_designation, r1_organization=r1_organization,
                                     r1_contact=r1_contact, r1_address=r1_address, r1_email=r1_email,
                                     r2_name=r2_name, r2_designation=r2_designation, r2_organization=r2_organization,
                                     r2_contact=r2_contact, r2_address=r2_address, r2_email=r2_email)
        ins.save()
        print('referee data has been written to DB')
        return redirect('referees')
    else:
        try:
            # Attempt to retrieve the record from the database
            record = refrees.objects.get(user=request.user)
            
            return render(request, 'cmb_Reg/taskbar_referees.html', {'record': record})
        except refrees.DoesNotExist:
                        
            return render(request, 'cmb_Reg/taskbar_referees.html')

def user_profile(request):
    # Get the current user
    user = request.user
    
    # Retrieve user data from different models
    bio_data = BioData.objects.get(user=user)
    qualifications = Qualifications.objects.filter(user=user)
    employments = Employment.objects.filter(user=user)
    publications = Publication.objects.filter(user=user)
    referees = refrees.objects.filter(user=user)
    
    # Pass user data to the template
    context = {
        'user': user,
        'bio_data': bio_data,
        'qualifications': qualifications,
        'employments': employments,
        'publications': publications,
        'referees': referees
    }
    return render(request, 'cmb_Reg/all_details.html', context)

# ------------- Application ------------------

def user_application(request):
    # Get the current user
    user = request.user
    if request.method == "POST":   
        course_name = request.POST['course_name']
        payment_type = request.POST['payment_type']
        reference_number = request.POST['reference_number']
        applied_date = timezone.now()

        # Create refrees instance
        ins = Application.objects.create(user=user, course_name=course_name, payment_type=payment_type, 
                                     reference_number=reference_number,applied_date=applied_date )
        ins.save()
        print('application data has been written to DB')
        return redirect('apply')
    
    applications = Application.objects.filter(user=user)
    return render(request, 'cmb_Reg/taskbar_apply.html', {'applications': applications})

# ----------- End of Application ---------------------

def generate_pdf(request):

    user = request.user
    bio_data = BioData.objects.get(user=user)
    qualifications = Qualifications.objects.get(user=user)
    employments = Employment.objects.get(user=user)
    publications = Publication.objects.get(user=user)
    referees = refrees.objects.get(user=user)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Application_CMB_Law_{bio_data.firstname}{bio_data.lastname}.pdf"'

    # Create a canvas object
    p = canvas.Canvas(response, pagesize=A4)

    # Write the details to the PDF
    p.drawImage("C:\\Users\\dulee\\Downloads\\logo_law_cmb.jpg", 35, 750, width=70, height=70)  # Adjust the path and dimensions as needed
    p.setFont("Helvetica-Bold", 18)  # Set font to Helvetica-Bold with size 18
    p.drawString(130, 790, "Faculty of Law - University of Colombo")  # Heading / Center
    p.drawString(120, 770, "Application for External Course Programs")  # Heading / Center
    p.line(100, 750, 500, 750)  # Horizontal Line

    # Bio Data section
    p.setFont("Helvetica-Bold", 12)
    p.drawString(80, 730, "Bio Data")  # Subsection Title
    p.drawString(90, 710, "Full Name:")
    p.drawString(90, 690, "First Name:")
    p.drawString(320, 690, "Last Name:")
    p.drawString(90, 670, "Birthday:")
    p.drawString(320, 670, "NIC:")
    p.drawString(90, 650, "Gender:")
    p.drawString(320, 650, "Marital Status:")
    
    # Displaying values
    p.setFont("Helvetica", 12)
    p.drawString(180, 710, bio_data.fullname)
    p.drawString(180, 690, bio_data.firstname)
    p.drawString(410, 690, bio_data.lastname)
    p.drawString(180, 670, bio_data.birthday.strftime("%Y-%m-%d"))
    p.drawString(410, 670, bio_data.nic)
    p.drawString(180, 650, bio_data.gender)
    p.drawString(410, 650, bio_data.marital_status)


    # Horizontal line
    p.line(100, 630, 500, 630)

    # Contact Details section
    p.setFont("Helvetica-Bold", 12)
    p.drawString(80, 610, "Contact Details")  # Subsection Title
    p.drawString(90, 590, "Contact:")
    p.drawString(320, 590, "E-Mail")
    p.drawString(90, 570, "Address")

    # Displaying values
    p.setFont("Helvetica", 12)
    p.drawString(180, 590, bio_data.contact)
    p.drawString(410, 590, bio_data.email)
    p.drawString(180, 570, bio_data.address)

    p.line(100, 550, 500, 550)

    #Emergency Contact Details
    p.setFont("Helvetica-Bold", 12)
    p.drawString(80, 530, "Emergency Contact Details")  # Subsection Title
    p.drawString(90, 510, "Name")
    p.drawString(320, 510, "Contact")
    p.drawString(90, 490, "Address")

    # Displaying values
    p.setFont("Helvetica", 12)
    p.drawString(180, 510, bio_data.e_name)
    p.drawString(410, 510, bio_data.e_contact)
    p.drawString(180, 490, bio_data.e_address)

    p.line(100, 470, 500, 470)

    #AL results
    p.setFont("Helvetica-Bold", 12)
    p.drawString(80, 450, "Advanced Level Examination Results")  # Subsection Title
    p.drawString(90, 430, "Year")
    p.drawString(320, 430, "Stream")
    p.drawString(90, 410, qualifications.subject1)
    p.drawString(320, 410, qualifications.subject2)
    p.drawString(90, 390, qualifications.subject3)
    p.drawString(320, 390, qualifications.subject4)

    #Displaying values
    p.setFont("Helvetica", 12)
    p.drawString(180, 430, qualifications.al_year)
    p.drawString(410, 430, qualifications.stream)
    p.drawString(250, 410, qualifications.result1)
    p.drawString(480, 410, qualifications.result2)
    p.drawString(250, 390, qualifications.result3)
    p.drawString(480, 390, qualifications.result4)

    p.line(100, 370, 500, 370)

    #1st Degree Results
    p.setFont("Helvetica-Bold", 12)
    p.drawString(80, 350, "First Degree Results")  # Subsection Title
    p.drawString(90, 330, "Degree Name")
    p.drawString(320, 330, "Institute")
    p.drawString(90, 310, "GPA")
    p.drawString(320, 310, "Class")
    p.drawString(90, 290, "Start Year")
    p.drawString(320, 290, "Graduated Year")

    # Displaying values
    p.setFont("Helvetica", 12)
    p.drawString(180, 330, qualifications.degreeName)
    p.drawString(410, 330, qualifications.institute)
    p.drawString(180, 310, qualifications.gpa)
    p.drawString(410, 310, qualifications.degreeClass)
    p.drawString(180, 290, qualifications.degreestartYear)
    p.drawString(410, 290, qualifications.graduateYear)

    p.line(100, 270, 500, 270)

    #Current Employement
    p.setFont("Helvetica-Bold", 12)
    p.drawString(80, 250, "Current Employement")  # Subsection Title
    p.drawString(90, 230, "Employer")
    p.drawString(320, 230, "Designation")
    p.drawString(90, 210, "Contact")
    p.drawString(320, 210, "Fax")
    p.drawString(90, 190, "Duties")
    p.drawString(90, 170, "Address")

    # Displaying values
    p.setFont("Helvetica", 12)
    p.drawString(180, 230, employments.c_name)
    p.drawString(410, 230, employments.c_designation)
    p.drawString(180, 210, employments.c_contact)
    p.drawString(410, 210, employments.c_fax)
    p.drawString(180, 190, employments.c_duties)
    p.drawString(180, 170, employments.c_address)

    p.line(100, 150, 500, 150)

    #previous Employement
    p.setFont("Helvetica-Bold", 12)
    p.drawString(80, 130, "Previous Employement")  # Subsection Title
    p.drawString(90, 110, "Employer")
    p.drawString(320, 110, "Designation")
    p.drawString(90, 90, "Start Date")
    p.drawString(320, 90, "End Date")
    p.drawString(90, 70, "Duties")
    p.drawString(90, 50, "Address")

    # Displaying values
    p.setFont("Helvetica", 12)
    p.drawString(180, 110, employments.p_name)
    p.drawString(410, 110, employments.p_designation)
    p.drawString(180, 90, employments.p_startDate.strftime("%Y-%m-%d"))
    p.drawString(410, 90, employments.p_endDate.strftime("%Y-%m-%d"))
    p.drawString(180, 70, employments.p_duties)
    p.drawString(180, 50, employments.p_address)


    p.rect(25, 25, 575 - 25, 825 - 25)

    p.showPage()
    #Refree Details Employement
    p.setFont("Helvetica-Bold", 12)
    p.drawString(80, 800, "Referee Details - 1")  # Subsection Title
    p.drawString(90, 780, "Name")
    p.drawString(90, 760, "Organization")
    p.drawString(320, 760, "Designation")
    p.drawString(90, 740, "Contact")
    p.drawString(320, 740, "E-Mail")
    p.drawString(90, 720, "Address")
    
    # Displaying values
    p.setFont("Helvetica", 12)
    p.drawString(180, 780, referees.r1_name)
    p.drawString(180, 760, referees.r1_organization)
    p.drawString(410, 760, referees.r1_designation)
    p.drawString(180, 740, referees.r1_contact)
    p.drawString(410, 740, referees.r1_email)
    p.drawString(180, 720, referees.r1_address)

    p.line(100, 700, 500, 700)

    #Refree Details Employement
    p.setFont("Helvetica-Bold", 12)
    p.drawString(80, 680, "Referee Details - 2")  # Subsection Title
    p.drawString(90, 660, "Name")
    p.drawString(90, 640, "Organization")
    p.drawString(320, 640, "Designation")
    p.drawString(90, 620, "Contact")
    p.drawString(320, 620, "E-Mail")
    p.drawString(90, 600, "Address")
    
    # Displaying values
    p.setFont("Helvetica", 12)
    p.drawString(180, 660, referees.r2_name)
    p.drawString(180, 640, referees.r2_organization)
    p.drawString(410, 640, referees.r2_designation)
    p.drawString(180, 620, referees.r2_contact)
    p.drawString(410, 620, referees.r2_email)
    p.drawString(180, 600, referees.r2_address)

    p.save()

    return response