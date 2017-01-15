# CSFTranscriptCheck
Used to check if someone is eligible for SRV CSF membership.
Step	Instructions	CSF Requirements (for refrence)
1	Stores Last Name, ID Number, and Current Grade Level (E,F,&G)	"In order to qualify for CSF, your previous semester grades must meet the following guidelines.
(Full rules in CSF Bylaws: https://goo.gl/mRuxEX)

San Ramon Valley Class List: https://goo.gl/hQ8Jtg

1. You must earn a minimum of 10 points from last semester’s grades:
          • The first 4 points must be from List I (see class list above).
          • The first 7 points (including the four points described above) must be from Lists I and II.
          • The remaining points may come from Lists I, II, or III.

2. You must use no more than 5 courses to qualify.
          • Two courses must be from List I (see class list above).
          • Three course (including the two above) must be from Lists I and II.
          • The remaining courses may come from Lists I, II, or III.

3. No points are given for physical education, courses taken in lieu of physical education, subjects repeated to improve a grade, courses involving office/teacher aiding, and courses taken on a pass/fail basis.

4. Points are granted as follows:
          A = 3 points
          B = 1 point
          C = 0 points
*One additional CSF point shall be granted for a grade of A or B in an AP or Honors course, up to a maximum of two such points per semester.
*A grade of a D or F in any course disqualifies you from membership."
2	Opens link in column L, IF link doesn't work return "NO" in M and "Link doesn't work" in N	
3	Checks Last Name, ID Number, and Current Grade Level	
4	If correct, move to next step, else return "NO" in M and either "Name doesn't match", "ID doesn't match", or "Grade doesn't match" in N	
5	Find most recent semester of grades (Year 2016-2017 and Grade must match), IF doesn't match return "NO" in M and "Old Transcript" in N	
6	Record all classes and the associated letter grades (record classes by class "code" and grade by letter)	
7	Turn letter grades into numbers (A=3, B=1, C=0) and add +1 for up to 2 AP or Honors Classes (AP and Honors class codes end in "AP" or "H") -- prioritize List I classes	
8	If any grade is a C or F, return "NO" in M and "D or F in a course" in N	
9	Two courses should be from List I (match courses from List I) pick courses with highest #	
10	One more course should be from List I or List II -- pick courses with highest #	
11	Pick 2 more courses from List I, II, or III -- pick courses with highest # (if they don't have enough courses, its okay)	
12	IF not enough List I or II classes for 9, 10, return "NO" in M and either "< 2 List I Courses" or "< 3 List I & II Courses" in N	
13	From list generated above, add points from List I classes -- must be >= 4	
14	Add points from List I and II classes -- must be >= 7	
15	Add points from List I, II, and III classes -- must be >= 10	
16	IF not enough points, return "NO" in M and either "< 4 List I Points", "< 7 List I & II Points", "< 10 List I, II, & III Points"	
17	If all are true, return "YES" in M	
18	Move down one row and repeat 1-17	
19	Stop at last row	
