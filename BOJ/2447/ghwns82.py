def draw_star(LEN):
    if LEN == 1:
        return ["*"]
    
    adult_star = []
    baby_star = draw_star(LEN//3)
    for i in baby_star:
        adult_star.append(i*3)
    for i in baby_star:
        adult_star.append(i+" "*(LEN//3)+i)
    for i in baby_star:
        adult_star.append(i*3)
    return adult_star
