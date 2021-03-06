# -*- coding: utf-8 -*-

# In an online library portal, there should be basically two things : 

# 1.)  List of books available in the library
# 2.)  Which book has been issued to which student

# Table 1 :  Books (book_id,name,avaialability,copies,author)

db.define_table('Books',
               Field('Book_id','integer'),
               Field('Book_Name','string'),
               Field('Book_Availability','string'),
               Field('Book_copies','integer'),
               Field('Book_author','string'))


# Table 2 : Issued (book_id,name,student-name,student-email,student-contact_details,student-submission detail)

db.define_table('Issued',
                Field('Book_id','integer'),
                Field('Book_Name','string'),
                Field('Student_Name','string'),
                Field('Student_Email','string'),
                Field('Student_Contact_No','string'),
                Field('Issued_Date','datetime'),
                Field('Submission_Date','datetime'))
