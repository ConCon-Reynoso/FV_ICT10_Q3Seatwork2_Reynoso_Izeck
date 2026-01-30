from pyscript import document, display

def intramurals_eligibility_&_team(e):

registration = document.getElementById('registration').value
grade = document.getElementById('grade').value
section = document.getElementById('section').value

if grade == 7 and section == 'Emerald':
    display('Congratulations! You are part of the Blue Bears!')
elif grade == 7 and section == 'Ruby':
    display('Congratulations! You are part of the Yellow Tigers!')
elif grade == 7 and section == 'Sapphire':
    display('Congratulations! You are part of the Red Bulldogs!')
elif grade == 7 and section == 'Topaz':
    display('Congratulations! You are part of the Green Hornets!')
elif grade == 8 and section == 'Emerald':
    display('Congratulations! You are part of the Yellow Tigers!')
elif grade == 8 and section == 'Ruby':
    display('Congratulations! You are part of the Red Bulldogs!')
elif grade == 8 and section == 'Sapphire':
    display('Congratulations! You are part of the Green Hornets!')
elif grade == 8 and section == 'Topaz':
    display('Congratulations! You are part of the Blue Bears!')
elif grade == 8 and section == 'Jade':
    display('Congratulations! You are part of the Blue Bears!')
elif grade == 9 and section == 'Emerald':
    display('Congratulations! You are part of the Green Hornets!')
elif grade == 9 and section == 'Ruby':
    display('Congratulations! You are part of the Blue Bears!')
elif grade == 9 and section == 'Sapphire':
    display('Congratulations! You are part of the Yellow Tigers!')
elif grade == 9 and section == 'Topaz':
    display('Congratulations! You are part of the Red Bulldogs!')
elif grade == 9 and section == 'Jade':
    display('Congratulations! You are part of the Green Hornets!')
elif grade == 10 and section == 'Emerald':
    display('Congratulations! You are part of the Red Bulldogs!')
elif grade == 10 and section == 'Ruby':
    display('Congratulations! You are part of the Green Hornets!')
elif grade == 10 and section == 'Sapphire':
    display('Congratulations! You are part of the Yellow Tigers!')
elif grade == 10 and section == 'Topaz':
    display('Congratulations! You are part of the Blue Bears!')