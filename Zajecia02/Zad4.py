#1.Jak sprawdzić czy ciąg znaków składa się tylko z cyfr?

num = '74658437658'
num.isdigit()
num.isnumeric()

txt = 'mum'
txt.center(10)
txt.center(10, '*')

txt = 'mummum'
txt.rstrip('*')


#4. Jak sprawdzić czy ciąg ma conajmniej jedną literę?
txt='adffjSndfjWnjfh'
txt.isalnum() and not txt.islower()

#5.Jak policzyć ciąg?
txt='adffjSndadfjWnjfh'
print(txt.count('ad'))
