def describe_pet(first_name,last_name,midlle_name=''):
    if midlle_name:
        full_name = first_name + ' ' + midlle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musican = describe_pet('vova','pishicov')
print(musican)
musican = describe_pet('vova','pishicov','nicolaewich')
print(musican)