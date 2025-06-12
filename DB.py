
from pypdf import PdfReader, PdfWriter
from datetime import datetime

# Load the original PDF
reader = PdfReader("C:\\Users\\orfor\\OneDrive\\Desktop\\Or's\\Learning\\The Hebrew University of Jerusalem\\"
                   "Second Year\\Semester B\\Courses\\67506 Databases\\Summaries\\To_W10.pdf")
writer = PdfWriter()
writer.add_metadata({
    "/Author": "Noam Kimhi, OF8, DB Course Staff HUJI 2025B",
    "/Creator": "OF8",
    "/Title": "Databases HUJI Course Summary 2025B, Edited by OF8",
    "/ModDate": datetime.now().strftime("D:%Y%m%d%H%M%S"),
    "/CreationDate": "D:20250613000000"
})

# Copy pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Add bookmarks (titles, page numbers start at 0)
w1 = writer.add_outline_item("Week 1: ER Diagrams", 1)
writer.add_outline_item("1.1 Introduction", 1, parent=w1)
writer.add_outline_item("1.2 ERD1: Entities, Attributes, Relationships", 1, parent=w1)
writer.add_outline_item("1.3 Multiplicities in Relationships", 4, parent=w1)
writer.add_outline_item("1.4 Referential Integrity", 6, parent=w1)
writer.add_outline_item("1.5 Inheritance ירושה", 8, parent=w1)
writer.add_outline_item("1.6 Weak Entity Sets", 9, parent=w1)
writer.add_outline_item("1.7 תרגום דיאגרמות לקשרים", 11, parent=w1)
writer.add_outline_item("Week 1 Quizzes", 15, parent=w1)
writer.add_outline_item("TA 1: ER Diagrams", 29, parent=w1)

w2 = writer.add_outline_item("Week 2: Relational Algebra", 56)
writer.add_outline_item("2.1 SQL1: Creating Tables", 56, parent=w2)
writer.add_outline_item("2.2 RA1: Projection, Selection", 58, parent=w2)
writer.add_outline_item("2.3 RA2: Union, Difference, Cartesian Product", 60, parent=w2)
writer.add_outline_item("2.4 RA3: Intersection, Join", 62, parent=w2)
writer.add_outline_item("2.5 RA4: Division", 63, parent=w2)
writer.add_outline_item("2.6 RA5: Equivalences Among RA Expressions", 65, parent=w2)
writer.add_outline_item("Week 2 Quizzes", 67, parent=w2)
writer.add_outline_item("TA 2: Relational Algebra", 77, parent=w2)

w3 = writer.add_outline_item("Week 3: SQL", 103)
writer.add_outline_item("3.1 SQL2: Intro to Queries", 103, parent=w3)
writer.add_outline_item("3.2 SQL3: SELECT, WHERE", 103, parent=w3)
writer.add_outline_item("3.3 SQL4: FROM, JOIN", 106, parent=w3)
writer.add_outline_item("3.4 SQL5: UNION, EXCEPT, INTERSECT", 107, parent=w3)
writer.add_outline_item("3.5 SQL6: Subqueries", 109, parent=w3)
writer.add_outline_item("Week 3 Quizzes", 114, parent=w3)
writer.add_outline_item("TA 3: SQL", 125, parent=w3)

w4 = writer.add_outline_item("Week 4: SQL", 149)
writer.add_outline_item("4.1 SQL7: Aggregation", 149, parent=w4)
writer.add_outline_item("4.2 SQL8: Null Values", 153, parent=w4)
writer.add_outline_item("4.3 SQL9: Modifications", 156, parent=w4)
writer.add_outline_item("4.4 SQL10: Views", 157, parent=w4)
writer.add_outline_item("4.5 SQL11: Recursion", 160, parent=w4)
writer.add_outline_item("Week 4 Quizzes", 164, parent=w4)
writer.add_outline_item("TA 4: SQL", 178, parent=w4)

w5 = writer.add_outline_item("Week 5: Indexes", 194)
writer.add_outline_item("5.1 IND1: Intro to Query Processing", 194, parent=w5)
writer.add_outline_item("5.2 IND2: Files", 195, parent=w5)
writer.add_outline_item("5.3 IND3: B+ Trees", 196, parent=w5)
writer.add_outline_item("IND4: Cost Estimation", 198, parent=w5)
writer.add_outline_item("IND5: Execution Plans", 201, parent=w5)
writer.add_outline_item("IND6: Multicolumn Indexes", 203, parent=w5)
writer.add_outline_item("Week 5 Quizzes", 206, parent=w5)
writer.add_outline_item("TA 5: Storing, Indexing and Accessing Data", 217, parent=w5)

w6 = writer.add_outline_item("Week 6: Joins and Sorting", 232)
writer.add_outline_item("6.1 JOIN1: Intro", 232, parent=w6)
writer.add_outline_item("6.2 JOIN2: BNL Join", 234, parent=w6)
writer.add_outline_item("6.3 JOIN3: INL Join", 237, parent=w6)
writer.add_outline_item("6.4 JOIN4: Sort", 240, parent=w6)
writer.add_outline_item("Week 6 Quizzes", 244, parent=w6)
writer.add_outline_item("TA 6: Query Processing: Join Algorithms", 253, parent=w6)

w7 = writer.add_outline_item("Week 7: Query Plans and Optimization", 266)
writer.add_outline_item("7.1 OPT: Intro", 266, parent=w7)
writer.add_outline_item("7.2 OPT2: Size Estimation", 267, parent=w7)
writer.add_outline_item("7.3 OPT3: Query Plans", 270, parent=w7)
writer.add_outline_item("7.4 OPT4: Choosing Selection", 273, parent=w7)
writer.add_outline_item("7.5 OPT: Join Casts", 275, parent=w7)
writer.add_outline_item("7.6 OPT6: Optimal Plan", 278, parent=w7)
writer.add_outline_item("Week 7 Quizzes", 282, parent=w7)
writer.add_outline_item("TA 7: Query Processing: Query Plans", 297, parent=w7)

w8 = writer.add_outline_item("Week 8: Framework (Design Theory)", 309)
writer.add_outline_item("8.1 FD1: Intro", 309, parent=w8)
writer.add_outline_item("8.2 FD2: Functional Dependencies", 310, parent=w8)
writer.add_outline_item("8.3 FD3: Implications", 312, parent=w8)
writer.add_outline_item("8.4 FD4: Closure", 314, parent=w8)
writer.add_outline_item("8.5 FD5: Keys and Superkeys", 316, parent=w8)
writer.add_outline_item("Week 8 Quizzes", 318, parent=w8)
writer.add_outline_item("TA 8: Design Theory", 327, parent=w8)

w9 = writer.add_outline_item("Week 9: Normal Forms (Design Theory)", 359)
writer.add_outline_item("9.1 FD6: All Key", 359, parent=w9)
writer.add_outline_item("9.2 FD7: Normal Forms", 361, parent=w9)
writer.add_outline_item("9.3 FD8: Decomposition", 365, parent=w9)
writer.add_outline_item("9.4 FD9: Lossless Join (2 Relations)", 368, parent=w9)
writer.add_outline_item("9.5 FD10: Lossless Join (N Relations)", 370, parent=w9)
writer.add_outline_item("Week 9 Quizzes", 375, parent=w9)
writer.add_outline_item("TA 9: Design Theory", 384, parent=w9)

w10 = writer.add_outline_item("Week 10: Decompositions", 400)
writer.add_outline_item("10.1 FD11: Dependency Preservation", 400, parent=w10)
writer.add_outline_item("10.2 FD12: Decomposition Normal Forms", 402, parent=w10)
writer.add_outline_item("10.3 FD13: Minimal Cover", 404, parent=w10)
writer.add_outline_item("10.4 FD14: 3NF Decomposition", 406, parent=w10)
writer.add_outline_item("10.5 FD15: BCNF Decomposition", 408, parent=w10)
writer.add_outline_item("Week 10 Quizzes", 410, parent=w10)
writer.add_outline_item("TA 10: Design Theory", 417, parent=w10)

# Save to a new PDF
with open("To_W10.pdf", "wb") as f:
    writer.write(f)

print("Done! Bookmarks added.")