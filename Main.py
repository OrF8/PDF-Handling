
from pypdf import PdfReader, PdfWriter

# Load the original PDF
reader = PdfReader("C:\\Users\\orfor\\OneDrive\\Desktop\\Or's\\Learning\\The Hebrew University of Jerusalem\\"
                   "Second Year\\Semester B\\Courses\\67506 Databases\\Summaries\\To_W10.pdf")
writer = PdfWriter()

# Copy pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Add bookmarks (titles, page numbers start at 0)
w1 = writer.add_outline_item("Week 1: ER Diagrams", 1)
writer.add_outline_item("Week 1 Quizzes", 15)
writer.add_outline_item("TA 1: ER Diagrams", 29)

w2 = writer.add_outline_item("Week 2: Relational Algebra", 56)
writer.add_outline_item("Week 2 Quizzes", 67)
writer.add_outline_item("TA 2: Relational Algebra", 77)

w3 = writer.add_outline_item("Week 3: SQL", 103)
writer.add_outline_item("Week 3 Quizzes", 114)
writer.add_outline_item("TA 3: SQL", 125)

w4 = writer.add_outline_item("Week 4: SQL", 149)
writer.add_outline_item("Week 4 Quizzes", 164)
writer.add_outline_item("TA 4: SQL", 178)

w5 = writer.add_outline_item("Week 5: Indexes", 194)
writer.add_outline_item("Week 5 Quizzes", 206)
writer.add_outline_item("TA 5: Storing, Indexing and Accessing Data", 217)

w6 = writer.add_outline_item("Week 6: Joins and Sorting", 232)
writer.add_outline_item("Week 6 Quizzes", 244)
writer.add_outline_item("TA 6: Query Processing: Join Algorithms", 253)
writer.add_outline_item("Week 7: Query Plans and Optimization", 266)
writer.add_outline_item("Week 7 Quizzes", 282)
writer.add_outline_item("TA 7: Query Processing: Query Plans", 297)
writer.add_outline_item("Week 8: Framework (Design Theory)", 309)
writer.add_outline_item("Week 8 Quizzes", 318)
writer.add_outline_item("TA 8: Design Theory", 327)
writer.add_outline_item("Week 9: Normal Forms (Design Theory)", 359)
writer.add_outline_item("Week 9 Quizzes", 375)
writer.add_outline_item("TA 9: Design Theory", 384)
writer.add_outline_item("Week 10: Decompositions", 400)
writer.add_outline_item("Week 10 Quizzes", 410)
writer.add_outline_item("TA 10: Design Theory", 417)

# Save to a new PDF
with open("output_with_bookmarks.pdf", "wb") as f:
    writer.write(f)

print("Done! Bookmarks added.")