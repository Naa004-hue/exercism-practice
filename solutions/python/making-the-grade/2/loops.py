"""Functions for organizing and calculating student exam scores."""

def round_scores(student_scores):
    """Round all provided student scores."""
    result=[]
    for score in student_scores:
        result.append(round(score))
    return result

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided."""
    fail=0
    for score in student_scores :
        if score <= 40:
            fail+=1
    return fail
            
def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' """
    the_best=[]
    for score in student_scores:
        if score>=threshold:
            the_best.append(score)
    return the_best

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade."""
    high=[]
    step=(highest-40)//4
    for indexx in range(4):
        grade=(step*indexx)+41
        high.append(grade)
    return high

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order."""
    rankings=[]
    com=list(zip(student_scores, student_names))
    for index, (score, name) in enumerate(com,start=1):
        rankings.append(f'{index}. {name.title()}: {score}')
    return rankings

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student """
    for student in student_info :
        if student[-1]==100:
            return student
    return[ ]