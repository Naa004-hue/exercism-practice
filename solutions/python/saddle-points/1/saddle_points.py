def saddle_points(matrix):
    if any(len(row)!=len(matrix[0]) for row in matrix[1:]):
        raise ValueError("irregular matrix")
    columns=[[*col] for col in zip(*matrix)]
    points=[]
    for r, row in enumerate(matrix, start=1):  
        for c, value in enumerate(row, start=1):
            if value == max(row) and value == min(columns[c-1]):
                points.append({"row": r, "column": c})
    return points
    
    